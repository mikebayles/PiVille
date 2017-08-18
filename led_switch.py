import RPi.GPIO as GPIO
import time

led_pin = 18
switch_pin = 23
delay = 0.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if not GPIO.input(switch_pin):
        print("Button pressed")
        time.sleep(0.2)
        
GPIO.cleanup()
