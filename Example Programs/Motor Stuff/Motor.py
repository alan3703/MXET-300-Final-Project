import RPi.GPIO as GPIO
import time

servoPIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 20) # GPIO 17 for PWM with 50Hz
p.start(1) # Initialization
try:
  while True:
    p.ChangeDutyCycle(1)
    time.sleep(0.5)
    p.ChangeDutyCycle(3)
    time.sleep(0.5)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()