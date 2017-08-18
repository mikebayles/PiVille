import RPi.GPIO as GPIO
import time

led_pin = 18
delay = 0.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        GPIO.output(led_pin, True)
        time.sleep(delay)
        GPIO.output(led_pin, False)
        time.sleep(delay)
finally:
    print("Cleaning up")
    GPIO.cleanup()
