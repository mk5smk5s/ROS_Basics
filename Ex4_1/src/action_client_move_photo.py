#! /usr/bin/env python

import rospy
import time
import actionlib
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty


"""
class SimpleGoalState:
	ACTIVE = 1
	DONE = 2
	WARN = 3
	ERROR = 4

"""
#we create some constants as in the SimpleGoalState class

ACTIVE = 1
DONE = 2
WARN = 3
ERROR = 4

nImage = 1


#definition of the feedback callback. Called when feedback is received from the action server
#it prints a message indicating a new message has been received

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
land = rospy.Publisher('/drone/land', Empty, queue_size=1)

def feedback_callback(feedback):
	global nImage
	print('[Feedback] image n. %d received' %nImage)
	nImage += 1

rospy.init_node('move_photo_drone_action_client') #initializes the action client node 

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

state_result = client.get_state()
rospy.loginfo("state_result:" + str(state_result) )

vel = Twist() #create a var of type Twist

vel.linear.x = 1
vel.angular.z = 0.5

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


