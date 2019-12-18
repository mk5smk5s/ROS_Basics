#! /usr/bin/env python

import rospy
from Ex3_2.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest
#Import the service message used by the service /gazebo/delete_model
import sys

rospy.init_node('service_custom_client_bb8')
 #Initialize a ROS node with the name service service_client
rospy.wait_for_service('move_bb8_in_square_custom')
#Wait for the service client gazebo/delete_model to be running
move_bb8_service = rospy.ServiceProxy('move_bb8_in_square_custom', BB8CustomServiceMessage)
#Create the connection to the service
kk = BB8CustomServiceMessageRequest()
kk.side = 1.0
kk.repetitions = 2.0
#Create an object of type DeleteModelRequest

#Fill the variable model_name of this object kk with the desired value
result = move_bb8_service(kk)
if result :
    kk.side = 0.5 
    result = move_bb8_service(kk)
#Send through the connection the name of the object to be deleted by the service
print result #Print the result given by the service called
