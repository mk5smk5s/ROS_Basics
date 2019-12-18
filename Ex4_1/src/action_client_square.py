#! /usr/bin/env python

import rospy
import time
import actionlib
from actionlib.msg import TestAction, TestGoal, TestResult, TestFeedback
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty



#we create some constants as in the SimpleGoalState class

ACTIVE = 1
DONE = 2
WARN = 3
ERROR = 4




#definition of the feedback callback. Called when feedback is received from the action server
#it prints a message indicating a new message has been received

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
land = rospy.Publisher('/drone/land', Empty, queue_size=1)

vel = Twist() #create a var of type Twist

def feedback_callback(feedback):

	print('[Feedback] Side n. %d flying' %feedback)
	if (feedback == 1):
		vel.linear.x = 1
		vel.angular.z = 0.5

rospy.init_node('action_client_square') #initializes the action client node

#create the connection to the action server
client = actionlib.SimpleActionClient('/action_server_square', TestAction)

#waits until the action server is up and running
rospy.loginfo('Waiting fo action server')
client.wait_for_server()
rospy.loginfo('Action Server Found')

#creates a goal to send to the action server
goal = TestGoal()
goal = 10 #indicates the side lenght that drone has to complete

#sends the goal to the action server, specifying which feedback function to call when feedback is received
client.send_goal(goal, feedback_cb=feedback_callback)
rate = rospy.Rate(1)

state_result = client.get_state()
rospy.loginfo("state_result:" + str(state_result) )




empty = Empty()

while state_result < DONE:
	rospy.loginfo('Doing stuff while waiting the server to give a result')
	takeoff.publish(empty)
	pub.publish(vel)
	rate.sleep()
	state_result = client.get_state()
	rospy.loginfo("state_result:" + str(state_result) )

land.publish(empty)


rospy.loginfo("[Result] State: " +str(client.get_state()))

if state_result == ERROR:
	rospy.logerr("Something went wrong in the Server Side")
if state_result == WARN:
	rospy.logwarn("There is a warning in the Server Side")
