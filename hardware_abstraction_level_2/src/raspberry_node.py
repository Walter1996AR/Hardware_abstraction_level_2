#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16
from hardware_abstraction_2.msg import custom_msg
########################
# delete all the #### to run on rasberry


####import RPi.GPIO as GPIO

# set pinmode to Broadcom SOC.
####GPIO.setmode(GPIO.BCM)
# turn of warnings.
####GPIO.setwarnings(False)
 
# set these gpio pins as output pins.
####GPIO.setup(4, GPIO.OUT) #servo pin 
####GPIO.setup(8, GPIO.OUT)# led pin

# configure PWM with a frequence of 50Hz.
####p = GPIO.PWM(4, 50) # servo pin
#####led = GPIO.PWM(8, 100)      # led pin 

# Start PWM on GPIO pin with a duty-cycle of 6%
#####p.start(6) # start the servopin with 1,5 ms (servo will start in the middle position)
#####led.start(0)  # start led on 0 percent duty cycle (off) 

# function to change the range of the received numers to another range
def map_custom(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

#subscriber function which is subscibed to topic data_out_raspberry,which is published by the master node 
def subscriber():
    sub = rospy.Subscriber('data_out_raspberry', custom_msg, callback_function)
    
    rospy.spin()

#callback function which is run everytime there is a message received on the topic. 
def callback_function(message):
    
    rospy.loginfo("I received: %s"%message.servo)
    ServoValue = message.servo
    LedValue = map_custom(message.led, 0, 460, 0, 100)
    
    newAnalogValue = map_custom(ServoValue, 0, 460, 2.5 , 11)
    rospy.loginfo("Duty Cycle %s"%newAnalogValue)
    rospy.loginfo(" Led value %s" %LedValue)
    ####p.ChangeDutyCycle(newAnalogValue)
    ####led.ChangeDutyCycle(LedValue)  
    
# main loop. 
if __name__ == "__main__":
    rospy.init_node("raspberry_node")
    subscriber()
