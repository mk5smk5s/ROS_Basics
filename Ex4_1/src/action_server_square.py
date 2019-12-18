#! /usr/bin/env python

import rospy
import actionlib

from actionlib.msg import TestFeedback, TestResult, TestAction

class SquareClass():

	#create messages that are used to publish feedback/result
	_feedback = TestFeedback() #we are creating the message objects
	_result = TestResult()

	def __init__(self):
		#creates the action server
		self._as  = actionlib.SimpleActionServer("square_as", TestAction, self.goal_callback, False)
		self._as.start()

	def goal_callback(self, goal):
		#it is called when the action server is called and each time a new goal si sent to the Action Server
		#it counts the Fibonacci sequence and returns the sequence to the node that called the action server
		r = rospy.Rate(1)
		success = True

		#append the seeds (first values) for the Fibonacci sequence
		self._feedback.sequence = []
		self._feedback.sequence.append(0)
		self._feedback.sequence.append(1)

		#publish info to the console for the user
		rospy.loginfo('"fibonacci_as": Executing, crreating fibonacci sequence of order %i, %i , %i' % (goal.order, self._feedback.sequence[0],  self._feedback.sequence[1]))

		#starts calculating the Fibonacci sequence
		fibonacciOrder = goal.order
		for i in xrange(1, fibonacciOrder):

			#check that preempt (cancelation) has not been requested by the action client
			if self._as.is_preempt_requested():
				rospy.loginfo("The goal has been preempted")
				self._as.set_preempted() #sets the client in preempted state (goal cancelled)
				success = False
				break

			#builds the next feedback msg to be sent
			self._feedback.sequence.append(self._feedback.sequence[i] + self._feedback.sequence[i-1])
			#publish the feedback
			self._as.publish_feedback(self._feedback)
			#the sequence is computed at 1 Hz frequency
			r.sleep()

		#if success we publish the final result otherwise we don't publish anything
		if success:
			self._result.sequence = self._feedback.sequence
			rospy.loginfo("Succeeded calculating the Fibonacci sequence of order %i" % fibonacciOrder)
			self._as.set_succeeded(self._result)

if __name__ == '__main__':
	print('provaaa')
	rospy.init_node('drone_square')
	SquareClass()
	rospy.spin()
