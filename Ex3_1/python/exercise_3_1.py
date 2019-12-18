#!/usr/bin/env python
import rospy
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest
import sys
import rospkg

rospy.init_node('service_client')
rospy.wait_for_service('/execute_trajectory')
exec_trj_serv =rospy.ServiceProxy('/execute_trajectory',ExecTraj)
rospack = rospkg.RosPack()
traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"
kk = ExecTrajRequest()
kk.file = traj
result = exec_trj_serv(kk)
print(result)
traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/release_food.txt"
kk = ExecTrajRequest()
kk.file = traj
result = exec_trj_serv(kk)
print(result)
