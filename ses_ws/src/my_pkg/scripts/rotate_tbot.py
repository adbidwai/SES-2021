#!/usr/bin/env python
#Shebang declaration

import rospy #Python API client library
from nav_msgs.msg import Odometry #Importing the Odometry message type from nav_msgs ROS package to subscribe to the /odom topic
from geometry_msgs.msg import Twist #Importing the Twist message type from geometry_msgs ROS package to publish on /cmd_vel topic
from tf.transformations import euler_from_quaternion #Importing the euler_from_quaternion() function from tf's transformations module to convert quaternions to euler angles
from math import degrees, radians #Importing functions to convert degrees to radians and vice versa

#Create a blank message twist
twist_msg = Twist()
twist_msg.linear.x = 0
twist_msg.linear.y = 0
twist_msg.linear.z = 0
twist_msg.angular.x = 0
twist_msg.angular.y = 0
twist_msg.angular.z = 0

yaw = 0.0

val = int(input("Enter the angle in degrees: "))
val = radians(val)

#Defining callback for /odom topic's subscriber (odom_sub)
def odom_cb(msg):
	global yaw
	rot = msg.pose.pose.orientation #Extract the orientation from msg which is of type : nav_msgs/Odometry
	(roll, pitch, yaw) = euler_from_quaternion ([rot.x, rot.y, rot.z, rot.w]) #Convert the orientation in quaternion form to euler angles
	print "Rotation angle (in degrees) is ", degrees(yaw)


rospy.init_node("commander") #Initialise ROS Node

odom_sub = rospy.Subscriber("/odom", Odometry, odom_cb) #Create a ROS subscriber object for the /odom topic
cmd_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10) #Create a ROS publisher object for the /cmd_vel topic

rate = rospy.Rate(5) #Create a rate object to determine the rate at which messages are to be published on the /cmd_vel topic

while not rospy.is_shutdown(): #Keep running until the node is not killed

	if abs(val - yaw) > 0.05:
		twist_msg.angular.z = 0.2
	else:
		twist_msg.angular.z = 0.0
	cmd_pub.publish(twist_msg)
	rate.sleep() #To add a delay in order to adjust the rate of publishing
	
