import RPi.GPIO as GPIO
import time

class EAModul:
   def __init__(self):
       self.taster1 = 36
       self.taster2 = 35
       self.led1 = 40
       self.led2 = 38
       self.led3 = 37

       GPIO.setmode(GPIO.BOARD)
       GPIO.setup(self.taster1, GPIO.IN)
       GPIO.setup(self.taster2, GPIO.IN)
       GPIO.setup(self.led1, GPIO.OUT)
       GPIO.setup(self.led2, GPIO.OUT)
       GPIO.setup(self.led3, GPIO.OUT)


   def start(self):
       try:
           while True:
               GPIO.output(self.led1, False)
               invalue = GPIO.input (self.taster1)
               print ("Funktioniert :", invalue)
               if invalue:
                  GPIO.output(self.led2, True)
                  time.sleep(1)
                  GPIO.output(self.led2, False)
                  GPIO.output(self.led3, True)
                  time.sleep(1)
                  GPIO.output(self.led3, False)
               invalue = GPIO.input (self.taster2)
               print ("Funktioniert :", invalue)
               if invalue:
                  GPIO.output(self.led2, True)
                  time.sleep(1)
                  GPIO.output(self.led2, False)
                  GPIO.output(self.led1, True)
                  time.sleep(1)
                  GPIO.output(self.led1, False)
       except KeyboardInterrupt:
               print("Schoenen Tag noch!")
               GPIO.cleanup()

def main():
   eam = EAModul()
   eam.start()

if __name__ == "__main__":
   main()


#With this code you will be able to test if the 'Button' work properly.
#You need to put the Button in to the order how it is said at the top of the code.
# Taster = Button
# led = LED
#Added master 2
