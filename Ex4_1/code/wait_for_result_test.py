#! /usr/bin/env python

import rospy
import time
import actionlib
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback

nImage = 1

#definition of the feedback callback. Called when feedback is received from the action server
#it prints a message indicating a new message has been received

def feedback_callback(feedback):
	global nImage
	print('[Feedback] image n. %d received' %nImage)
	nImage += 1

rospy.init_node('example_with_wait_for_result_drone_action_client') #initializes the action client node 

#create the connection to the action server
client = actionlib.SimpleActionClient('/ardrone_action_server', ArdroneAction)

#waits until the action server is up and running
rospy.loginfo('Waiting fo action server')
client.wait_for_server()
rospy.loginfo('Action Server Found')

#creates a goal to send to the action server
goal = ArdroneGoal() 
goal.nseconds = 10 #indicates the time for taking pictures 

#sends the goal to the action server, specifying which feedback function to call when feedback is received
client.send_goal(goal, feedback_cb=feedback_callback)
rate = rospy.Rate(1)


rospy.loginfo('Lets Start the wait for the action to finish loop')
while not 	client.wait_for_result():
	rospy.loginfo('Doing stuff while waiting the server to give a result')
	rate.sleep()



print('[Result] State: %d' %(client.get_state())) 

