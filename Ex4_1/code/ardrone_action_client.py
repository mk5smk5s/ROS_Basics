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

rospy.init_node('drone_action_client') #initializes the action client node 

#create the connection to the action server
client = actionlib.SimpleActionClient('/ardrone_action_server', ArdroneAction)

client.wait_for_server() #waits until the action server is up and running

goal = ArdroneGoal() #creates a goal to send to the action server

goal.nseconds = 10 #indicates the time for taking pictures 

#sends the goal to the action server, specifying which feedback function to call when feedback is received
client.send_goal(goal, feedback_cb=feedback_callback)

#goal preemption
#time.sleep(3.0)
#client.cancel_goal() #cancel the goal 3 seconds after starting

#wait until the result is obtained and check status periodically
#in the meantime you can do other stuff
status = client.get_state()

client.wait_for_result()
print('[Result] State: %d' %(client.get_state())) 

