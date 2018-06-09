import RPi.GPIO as GPIO
import time

class LDR:
    __PinLDR__ = 4
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def SetLDRPin(self, pin):
        self.__PinLDR__ = pin

    def GetLDRCount(self):
        count = 0

        GPIO.setup(self.__PinLDR__, GPIO.OUT)
        GPIO.output(self.__PinLDR__, GPIO.LOW)

        time.sleep(0.1)
        GPIO.setup(self.__PinLDR__, GPIO.IN)

        while (GPIO.input(self.__PinLDR__) == GPIO.LOW):
            count += 1

        return count