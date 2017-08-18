import RPi.GPIO as GPIO
import time

led_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(100)

try:
    while True:
        duty = int(input("Enter Brightness (0 to 100) :"))
        pwm_led.ChangeDutyCycle(duty)        
finally:
    print("Cleaning up")
    GPIO.cleanup()
