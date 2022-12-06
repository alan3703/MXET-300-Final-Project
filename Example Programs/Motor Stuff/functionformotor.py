def rotatearm():
    if __name__ == "__main__":
    my_Rate = 0.
    while(1):
        #Motor will move to pick up
        sendarm(-0.7)
        time.sleep(0.2)                       # run fwd for 4 seconds
        sendarm(0)                      # stops for claw to do its job
        time.sleep(5)

        #Motor will move to normal position

        sendarm(0.7)
        time.sleep(0.2)                       # run reverse for 4 seconds
        sendarm(0)
        time.sleep(4)
        
        #stops the motor
        sendarm(0)
        time.sleep(4)
        
        return 0 