import L1_ina as VR
import L1_log as Log
import time

def getVoltagetoLog():
    Voltage_Reader = VR.readVolts()
    Vol_to_Log = Log.tmpFile(Voltage_Reader, "SV")
    return
if __name__ == "__main__":
    while True:
        getVoltagetoLog()
        time.sleep(1)