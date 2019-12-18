#! /usr/bin/env python 
#The interpreter used is the first of your environment's $PATH 

import rospy
#python library for ROS

rospy.init_node("ObiWan")
#initiate a node called ObiWan

rate=rospy.Rate(2)
#We create a rate object of 2Hz

while not rospy.is_shutdown(): #endless loop until Ctrl + C
	print "Help me Obi-Wan"
	rate.sleep()			   #the node sleeps to maintain the rate