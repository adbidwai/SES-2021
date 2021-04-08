#! /usr/bin/env python
#The above line is not a comment. It is something known as a shebang which is required when you want the language/program to run files as executables. Whenever you run the ROS nodes using 'rosrun #package_name #node_name' the nodes are run as executables and not ordinary code files

import rospy #Importing the Python API client library
from std_msgs.msg import String #Importing the String message definition / class

# Below is the definition of the callback function
def cb(msg):
	print msg.data

rospy.init_node("subscriber_node") #Initializing the ROS node with "subscriber_node" as its name
sub = rospy.Subscriber('/chatter', String, cb)  #Creating an object of the Subscriber class from the rospy library with (#topic_name, #message_type, #name_of_the_callback_function) as parameters
rospy.spin() #the spin() function acts like an infinite empty while loop so your codes does not end and your callbacks can keep on being called					
