import L1_log as log
import L2_kinematics as kin
import L1_encoder as en
import numpy as np
import time
import L1_ina as VR



def getVoltagetoLog():
    Voltage_Reader = VR.readVolts()
    Vol_to_Log = log.tmpFile(Voltage_Reader, "SV")
    return


def thetadot_log():
    AngVel = kin.getPdCurrent()
    AngVel_to_Log = log.tmpFile(AngVel[1], "thetadot")
    return

def xdot_log():
    Vel = kin.getMotion()
    Vel_to_Log = log.tmpFile(Vel[0], "xdot")
    return

def pdl_log():
    AngL = en.readShaftPositions()
    pdl_to_Log = log.tmpFile(AngL[0], "pdl")
    return

def pdr_log():
    AngR = en.readShaftPositions()
    pdr_to_Log = log.tmpFile(AngR[1], "pdr")
    return

if __name__ == "__main__":
    while True:
        thetadot_log()
        xdot_log()
        pdl_log()
        pdr_log()
        getVoltagetoLog()
        time.sleep(1)

