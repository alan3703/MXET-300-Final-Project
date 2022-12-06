# Motors Program for SCUTTLE running RasPi
# Motors Program for SCUTTLE running RasPi
# This example sends commands to two motors on the appropriate pins for H-bridge
# For pin mapping, see Wiring Guide Pi on the SCUTTLE webpage.
# Last update: 2020.11 with improved PWM method

# Import external libraries
import gpiozero                             # used for PWM outputs
from gpiozero import PWMOutputDevice as pwm # for driving motors, LEDs, etc
import time                                 # for keeping time
import numpy as np                          # for handling arrays

frq = 20                                   # motor driving frequency
# Broadcom (BCM) pin numbering for RasPi is as follows: PHYSICAL:       NAME:

ARM_chA = pwm(6, frequency=frq,initial_value=0)     # PIN 31        GPIO6
ARM_chB = pwm(12, frequency=frq,initial_value=0)    # PIN 32        GPIO12(PWM0)

def compute_PWM(speed):              # take an argument in range [-1,1]
    if speed == 0:
        x = np.array([0,0])         # set all PWM to zero
    else:
        x = speed + 1.0             # change the range to [0,2]
        ch_A = 0.5 * x               # channel A sweeps low to high
        ch_B = 1 - (0.5 * x)         # channel B sweeps high to low
        x = np.array([ch_A, ch_B])    # store values to an array
        x = np.round(x,2)           # round the values
    return(x)

def sendarm(mySpeed):          # takes at least 0.3 ms
    my_PWM = compute_PWM(mySpeed)
    ARM_chB.value = my_PWM[0]
    ARM_chA.value = my_PWM[1]


# THIS LOOP ONLY RUNS IF THE PROGRAM IS CALLED DIRECTLY
def rotate_arm():
    if __name__ == "__main__":
        my_Rate = 0.
        while(1):
            print("yes")
            #Motor will move to pick up
            sendarm(-0.76)
            time.sleep(0.2)                       # run fwd for 4 seconds
            sendarm(0)                      # stops for claw to do its job
            time.sleep(1)

            #Motor will move to normal position

            sendarm(0.3)
            time.sleep(0.2)                       # run reverse for 4 seconds
            sendarm(0)
            time.sleep(2)
        
        #stops the motor
    sendarm(0)
    time.sleep(4)
        
        
        