#!/usr/bin/env python
#Shebang declaration

import rospy #Python API client library
import math  #for performing mathematical conversions
from nav_msgs.msg import Odometry #Importing the Odometry message type from nav_msgs ROS package to subscribe to the /odom topic
from geometry_msgs.msg import Twist #Importing the Twist message type from geometry_msgs ROS package to publish on /cmd_vel topic

#Create a blank message twist
twist_msg = Twist()
twist_msg.linear.x = 0
twist_msg.linear.y = 0
twist_msg.linear.z = 0
twist_msg.angular.x = 0
twist_msg.angular.y = 0
twist_msg.angular.z = 0

x = 0

#Defining callback for /odom topic's subscriber (odom_sub)
def odom_cb(msg):
	global x
	x = msg.pose.pose.position.x #Extract the x coordinate from msg which is of type : nav_msgs/Odometry
	print "X coordinate of the turtlebot is ", x

rospy.init_node('commander') #Initialise ROS Node

odom_sub = rospy.Subscriber('/odom', Odometry, odom_cb) #Create a ROS subscriber object for the /odom topic
cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10) #Create a ROS publisher object for the /cmd_vel topic

rate = rospy.Rate(5) #Create a rate object to determine the rate at which messages are to be published on the /cmd_vel topic

while not rospy.is_shutdown(): #Keep running until the node is not killed
	if x<4:
		twist_msg.linear.x = 0.07
		cmd_pub.publish(twist_msg)
	if x>4:
		twist_msg.linear.x = 0
		cmd_pub.publish(twist_msg)
	rate.sleep() #To add a delay in order to adjust the rate of publishing
	






