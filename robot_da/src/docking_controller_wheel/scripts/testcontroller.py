#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist

class SimpleController(object):
    def __init__(self):
        rospy.loginfo("Starting 3-wheel robot controller")
        
        # Publisher to send commands to the wheels
        self.front_cmd_pub = rospy.Publisher("wheel_front_controller/command", Float64, queue_size=10)
        self.left_cmd_pub = rospy.Publisher("wheel_left_controller/command", Float64, queue_size=10)
        self.right_cmd_pub = rospy.Publisher("wheel_right_controller/command", Float64, queue_size=10)
        
        # Set the rate at which we send commands (e.g., 10 Hz)
        self.rate = rospy.Rate(10)
        
    def control_motor(self, speed=0.5):
        # Publish velocity command for each wheel
        rospy.loginfo("Publishing motor commands: %.2f", speed)
        self.right_cmd_pub.publish(speed)
        self.left_cmd_pub.publish(speed)
        # self.front_cmd_pub.publish(speed)

    def run(self):
        # Main loop to control the robot
        while not rospy.is_shutdown():
            self.control_motor(3)  # Modify the speed here if needed
            self.rate.sleep()  # Sleep to maintain loop rate

if __name__ == "__main__":
    try:
        rospy.init_node("simple_controller")
        controller = SimpleController()
        controller.run()  # Run the motor control loop
    except rospy.ROSInterruptException:
        pass
