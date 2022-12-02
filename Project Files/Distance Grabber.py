import time
import L1_log
import L1_lidar
import L2_vector
import numpy as np

while True:
    
    # Distances/angle
    distanceValues = L2_vector.getNearest()
    distanceMeters = distanceValues[0]
    distanceAngle = distanceValues[1]
    
    print ("Meters:", distanceMeters)
    L1_log.tmpFile(distanceMeters, "meterFile")
    
    print("Angle:", distanceAngle)
    L1_log.tmpFile(distanceAngle, "angleFile")
    
    
    #X and Y value
    xValue = distanceMeters * np.cos(distanceAngle) 
    yValue = distanceMeters * np.sin(distanceAngle)
    
    print("X Value", xValue)
    L1_log.tmpFile(xValue, "xFile")
    
    print("Y Value", yValue)
    L1_log.tmpFile(yValue, "yFile")
    
    print("")
    time.sleep(1)