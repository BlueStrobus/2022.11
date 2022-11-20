import serial
from threading import Thread

import datetime
import time

class Comm:
    
    def __init__(self, port, baud, win):
        self.win = win
        self.srl = serial.Serial(port, baud, timeout=1)
        
        self.isRunning = True

        srlThread = Thread(target=self.run, args=(self.srl,))
        srlThread.daemon = True
        srlThread.start()

    def run(self, srl):

        while self.isRunning:
            try:
                if srl.isOpen():
                    read = srl.readline().decode("utf-8").strip()
                    if read:
                        self.read_serial(read)
            except Exception as e:
                print(e)
            
            # 100ms sleep
            time.sleep(0.1)

    def stop(self):
        self.isRunning = False
        self.srl.close()

    def read_serial(self, data):
        print(datetime.datetime.now(), data)
        self.win.displayMsg(data, "Recv")

    def send_serial(self, data):
        if self.srl.isOpen():
            print("data send = {}".format(data))
            self.srl.write(data.encode(encoding='utf-8'))
            self.win.displayMsg(data, "Send")

    def __del__(self):
        self.stop()