#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('topic_publisher')
pub = rospy.Publisher('/counter', Int32, queue_size=1)
#create a publsher object that publish on the /counter topic
rate = rospy.Rate(2)
count = Int32() #create a var of type Int32
count.data = 0  

while not rospy.is_shutdown():#until someone stops 
#the program execution 
	pub.publish(count)
	count.data += 1
	rate.sleep()
