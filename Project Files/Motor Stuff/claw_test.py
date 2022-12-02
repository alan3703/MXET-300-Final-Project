from gpiozero import Servo
from time import sleep

claw = Servo(24)

try:
	while True:
		claw.min()
		sleep(2)
		claw.max()
		sleep(2)
except KeyboardInterrupt:
	print("Program stopped")