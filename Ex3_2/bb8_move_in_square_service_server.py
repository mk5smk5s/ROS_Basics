#! /usr/bin/env python

import rospy
from python import move_bb8 as bb8
from std_srvs.srv import Empty, EmptyResponse
#Import the service message classes generated from Empty.srv

def my_callback(request):
    bb8.MoveBB8()
    return EmptyResponse()
#The Service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split()))

rospy.init_node('movebb8_server')
my_service = rospy.Service('/move_bb8_in_square', Empty, my_callback)
#Create the service called my_service with the defined callback
rospy.spin()
#maintain the service open
