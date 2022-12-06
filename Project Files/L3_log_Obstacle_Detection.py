import L1_log as log
import L1_lidar as lid
import L2_vector as vect
import numpy as np
import time

# def Object_Distance_log():
#     Dist = vec.getNearest()
#     Dist_to_Log = log.tmpFile(Dist[0], "Obj_Dist")
#     return

# def Object_Angle_log():
#     Angle = vec.getNearest()
#     Ang_to_Log = log.tmpFile(Angle[1], "Obj_Angle")
#     return

# def x_log():
#     cartx = vec.polar2cart(m, deg)
#     x_to_Log = log.tmpFile(cartx[0], "x_values")
#     return

# def y_log():
#     carty = vec.polar2cart(m, deg)
#     y_to_Log = log.tmpFile(carty[1], "y_values")
#     return





if __name__ == "__main__":
    while True:
        

        Angle, Distance = vect.getNearest()
        
        
        cartx = vect.polar2cart(Distance, Angle)
        carty = vect.polar2cart(Distance ,Angle)

        Ang_to_Log = log.tmpFile(Angle, "Obj_Angle")
        Dist_to_Log = log.tmpFile(Distance, "Obj_Dist")


        x = cartx[0]
        y = carty[1]
        
        x_to_Log = log.tmpFile(x, "x_values")
        y_to_Log = log.tmpFile(y, "y_values")
        
        time.sleep(1)
