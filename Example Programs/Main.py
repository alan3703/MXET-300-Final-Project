import cv2              # For image capture and processing
import numpy as np

import time
import L1_log
import L1_lidar
import L2_vector

import L2_speed_control as sc
import L2_inverse_kinematics as ik
import L2_kinematics as kin
import netifaces as ni
from time import sleep
from math import radians, pi

print("Ready")


xdot = 10

while True:
    distanceValues = L2_vector.getNearest()
    distanceMeters = distanceValues[0]
    distanceAngle = distanceValues[1]
    
    print(distanceMeters)
    print(distanceAngle)
    
    if distanceMeters < .1:
    
        if ((distanceAngle < 0) and (distanceAngle > -100)):
            # Move Left
            print("Move Left")
            motions = [
                [0.1, 1.5, 1.5], # (turning 90º to the left)        
                [0.2, 0.0, 1.0], # (Go forward)         
                [0.1, -1.5, 1.5] # (turning 90º to the right)
            ]
            
            for  count, motion in enumerate(motions):
                print("Motion: ", count+1, "\t Chassis Forward Velocity (m/s): {:.2f} \t Chassis Angular Velocity (rad/s): {:.2f} \t Duration (sec): {:.2f}".format(motion[0], motion[1], motion[2]))
                wheel_speeds = ik.getPdTargets(motion[:2])                  # take the forward speed(m/s) and turning speed(rad/s) and use inverse kinematics to deterimine wheel speeds
                sc.driveOpenLoop(wheel_speeds)                              # take the calculated wheel speeds and use them to run the motors
                sleep(motion[2])            
            
        elif ((distanceAngle > 0) and (distanceAngle < 100)):
            # Move Right
            print("Move Right")
            motions = [
                [0.1, -1.5, 1.5], # (turning 90º to the right)        
                [0.2, 0.0, 1.0], # (Go forward)         
                [0.1, 1.5, 1.5] # (turning 90º to the left)
            ]
            
            for  count, motion in enumerate(motions):
                print("Motion: ", count+1, "\t Chassis Forward Velocity (m/s): {:.2f} \t Chassis Angular Velocity (rad/s): {:.2f} \t Duration (sec): {:.2f}".format(motion[0], motion[1], motion[2]))
                wheel_speeds = ik.getPdTargets(motion[:2])                  # take the forward speed(m/s) and turning speed(rad/s) and use inverse kinematics to deterimine wheel speeds
                sc.driveOpenLoop(wheel_speeds)                              # take the calculated wheel speeds and use them to run the motors
                sleep(motion[2])        

    else:
        print("forward")
        wheel_measured = kin.getPdCurrent() 
        wheel_speed = ik.getPdTargets(np.array([6, 0]))
        sc.driveClosedLoop(wheel_speed, wheel_measured, 0)
