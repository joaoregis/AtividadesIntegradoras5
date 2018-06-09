import RPi.GPIO as GPIO
import time


class LED:
    __pinled__ = 14
    __durationtime__ = 2
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.__pinled__,GPIO.OUT)

    def setpinled(self, pin):
        self.__pinled__ = pin
        GPIO.setup(self.__pinled__,GPIO.OUT)

    def setdurationtime(self, time):
        self.__durationtime__ = time
    
    def sendsignalled(self, typeofsignal):
        if typeofsignal == "on":
            GPIO.output(self.__pinled__,GPIO.HIGH) # Liga o led
            time.sleep(self.__durationtime__)
            GPIO.output(self.__pinled__,GPIO.LOW)

        elif typeofsignal == "off":
            time.sleep(self.__durationtime__)

        elif typeofsignal == "blink":

            blinktime = self.__durationtime__/5

            for i in range(0, 5):
                GPIO.output(self.__pinled__,GPIO.HIGH) # Liga o led
                time.sleep(blinktime)
                GPIO.output(self.__pinled__,GPIO.LOW)

            blinktime = self.__durationtime__/4
            for i in range(0, 4):
                GPIO.output(self.__pinled__,GPIO.HIGH) # Liga o led
                time.sleep(blinktime/2)
                GPIO.output(self.__pinled__,GPIO.LOW)
                time.sleep(blinktime/2)

