#! /usr/bin/env python 

import rospy  #Importing the Python API client library
from std_msgs.msg import String #Importing the String message definition / class

rospy.init_node('publisher_node')
pub = rospy.Publisher('/chatter', String, queue_size=5)

str_obj = String() #Creating an instance of String with name str_obj
str_obj.data = "Hello World !!!" #adding data to the str_obj 

rate = rospy.Rate(2)  #defining the rate of publishing in Hz

while not rospy.is_shutdown(): #until this code isn't ended
	pub.publish(str_obj)   #publish the str_obj
	print "The message is published" #debug statement
	rate.sleep()           #sleep or add delay to the rate to adjust it from overflow
	


