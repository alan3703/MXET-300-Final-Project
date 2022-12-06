import cv2              # For image capture and processing
import numpy as np      
import L2_speed_control as sc
import L2_inverse_kinematics as ik
import L2_kinematics as kin
import netifaces as ni
from time import sleep
from math import radians, pi


def turning(angle):
    
    wheel_measured = kin.getPdCurrent() 
    wheel_speed = ik.getPdTargets(np.array([0, -1.1*angle]))
    sc.driveClosedLoop(wheel_speed, wheel_measured, 0) 
    
    return 0
    
def straight():
    
    wheel_measured = kin.getPdCurrent() 
    wheel_speed = ik.getPdTargets(np.array([1, 0]))
    sc.driveClosedLoop(wheel_speed, wheel_measured, 0)
    sleep(.5)
    wheel_measured = kin.getPdCurrent() 
    wheel_speed = ik.getPdTargets(np.array([0, 0]))
    sc.driveClosedLoop(wheel_speed, wheel_measured, 0)
    return 0


straight()