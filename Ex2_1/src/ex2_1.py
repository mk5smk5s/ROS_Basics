#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
#create a publsher object that publish on the /turtle1/cmd_vel topic
rate = rospy.Rate(2)
vel = Twist() #create a var of type Twist
vel.linear.x = 1
vel.angular.z = 0.5  

while not rospy.is_shutdown():#until someone stops 
#the program execution 
	pub.publish(vel)	
	rate.sleep()
