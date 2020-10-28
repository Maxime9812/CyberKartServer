import threading
import time
import picamera
import io
from Server import *

threadLock = threading.Lock()


class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = threading.Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)


class Camera:
    def __init__(self):
        self.thread = threading.Thread(target=self.Send, args=())
        self.isRunning = False

    def start(self):
        print("Start Camera")
        self.isRunning = True
        self.thread.start()

    def stop(self):
        print("Stop Camera")
        self.isRunning = False

    def Send(self):
        while self.isRunning:
            if Server._instance.client is not None:
                try:

                    with picamera.PiCamera(resolution='640x480', framerate=30) as camera:
                        output = StreamingOutput()

                        camera.start_recording(output, format='mjpeg')
                        while Server._instance.client is not None:
                            with output.condition:
                                output.condition.wait()
                                frame = output.frame
                                packet = io.BytesIO()
                                packetToSend = io.BytesIO()

                                packet.write(struct.pack('i', 2))
                                packet.write(struct.pack('i', len(frame)))
                                packet.write(frame)

                                packetToSend.write(struct.pack('i', len(packet.getvalue())))
                                packetToSend.write(packet.getvalue())

                                print(Server._instance.client.send(packetToSend.getvalue()))

                except socket.timeout:
                    Server._instance.client = None
