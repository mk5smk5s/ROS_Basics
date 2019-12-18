#! /usr/bin/env python

import rospy
from python import move_bb8 as bb8
from Ex3_2.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
#Import the service message classes generated from BB8CustomServiceMessage.srv

def my_callback(request):
    bb_8 = bb8.MoveBB8(request.side, request.repetitions )
    print ("Request Data ==> side "+ str(request.side)+", repetitions =" + str(request.repetitions))

    my_response = BB8CustomServiceMessageResponse()
    if bb_8.success == True:
        my_response.success = True
    print('return')
    return my_response.success





rospy.init_node('movebb8_server_custom')
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage, my_callback)
#Create the service called my_service with the defined callback
rospy.spin()
#maintain the service open
