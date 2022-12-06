# this code is intended to be used to create a path utilising inverse kinematics
# use this code as a template to create pre-determined paths using known chassis forward velocity (x dot) in m/s, 
# chassis angular velocity (theta dot) in rad/s, and motion duration in sec for each motion to create the path

import L1_log as log
import L2_inverse_kinematics as ik
import L2_speed_control as sc
import numpy as np
from time import sleep


# define some variables that can be used to create the path
# make use of these definitions in the motions list
pi = np.pi                  # utilize the numpy library to define pi
d1 = 1                      # distance in meters of segment 1 in the path
d2 = 1                      # distance in meters of segment 2 in the path
forward_velocity = 0.0      # forward velocity (x dot) in m/s of SCUTTLE. NOTE that the max forward velocity of SCUTTLE is 0.4 m/s

# below is a list setup to run through each motion segment to create the path.
# the list elements within each list are in order as follows: chassis forward velocity (m/s), chassis angular velocity (rad/s), and motion duration (sec)
# enter the chassis forward velocity (x dot) in m/s, chassis angular velocity (theta dot) in rad/s, and motion duration in sec for each motion to create the path
motions = [
    [0.2, 0.0, 2.0],            # Motion 1 (DIRECTION: straight), first value represents velocity in which the robot will be travelling in a straight path, the next is the degrees that it will turn and the last is the time that it should take to perform the action
    [0.1, 1.5, 1.5],            # Motion 2 (DIRECTION: turning 90º to the left), first value represents velocity in which the robot will be travelling in while turning left, the next is the degrees that it will turn and the last is the time that it should take to perform the action 
    [0.2, 0.0, 2.0],            # Motion 3 (DIRECTION: straight), first value represents velocity in which the robot will be travelling in a straight path, the next is the degrees that it will turn and the last is the time that it should take to perform the action
    [0.1, 1.5, 1.5],            # Motion 4 (DIRECTION: turning 90º to the left), first value represents velocity in which the robot will be travelling in while turning left, the next is the degrees that it will turn and the last is the time that it should take to perform the action 
    [0.2, 0.0, 2.0],            # Motion 5 (DIRECTION: straight), first value represents velocity in which the robot will be travelling in a straight path, the next is the degrees that it will turn and the last is the time that it should take to perform the action
    [0.1, -1.5, 1.2],           # Motion 6 (DIRECTION: turning 90º to the right), first value represents velocity in which the robot will be travelling in while turning right, the next is the degrees that it will turn and the last is the time that it should take to perform the action
    [0.2, 0.0, 2.0],            # Motion 7 (DIRECTION: straight), first value represents velocity in which the robot will be travelling in a straight path, the next is the degrees that it will turn and the last is the time that it should take to perform the action
    [0.1, -1.5, 1.4],           # Motion 8 (DIRECTION: turning 90º to the right), first value represents velocity in which the robot will be travelling in while turning right, the next is the degrees that it will turn and the last is the time that it should take to perform the action
    [0.2, 0.0, 2.0],            # Motion 9 (DIRECTION: straight), first value represents velocity in which the robot will be travelling in a straight path, the next is the degrees that it will turn and the last is the time that it should take to perform the action
    [0.0, 0.0, 1.4]             # Motion 10 (stops), first value represents velocity, but since is stopping the velocity is 0. 
]

# iterate through and perform each open loop motion and then wait the specified duration.
for  count, motion in enumerate(motions):
    print("Motion: ", count+1, "\t Chassis Forward Velocity (m/s): {:.2f} \t Chassis Angular Velocity (rad/s): {:.2f} \t Duration (sec): {:.2f}".format(motion[0], motion[1], motion[2]))
    wheel_speeds = ik.getPdTargets(motion[:2])                  # take the forward speed(m/s) and turning speed(rad/s) and use inverse kinematics to deterimine wheel speeds
    sc.driveOpenLoop(wheel_speeds)                              # take the calculated wheel speeds and use them to run the motors
    sleep(motion[2]) # wait the motion duration
    
def x_dot_log():
    Vel_to_Log = Log.tmpFile(motion[0], "Velocity")
    return
if __name__ == "__main__":
    while True:
        x_dot_log()
        time.sleep(1)

def theta_dot_log():
    AngV_to_Log = Log.tmpFile(motion[1], "anglular_velocity")
    return
if __name__ == "__main__":
    while True:
        theta_dot_log()
        time.sleep(1)
