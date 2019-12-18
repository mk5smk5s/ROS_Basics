#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist




class MoveBB8:
    '''class that allows square movements to bb_8'''

    def __init__(self, side, repetitions):
        self.pub = rospy.Publisher("/cmd_vel", Twist , queue_size=10)
        #self.reset_service = rospy.Service("/reset_counter", SetBool, self.callback_reset_counter)
        self.twist_msg = Twist()
        self.twist_msg.linear.x = 0
        self.twist_msg.angular.z = 0
        self.side = side
        self.repetitions = repetitions
        self.time = self.side / 0.2
        self.success = False
        self.count = 1


        while not rospy.is_shutdown() and self.success == False :
            if self.repetitions > self.count:
                for i in range (5):
                    self.run(-0.2,0)
                    rospy.sleep(self.time)
                    self.run(0,0)
                    rospy.sleep(4.0)
                    self.run(0,0.29)
                    rospy.sleep(self.time)
                    print(self.count, "COUNTTTTTTTTTTTTTTTTTTTT")
                self.count += 1
            else:
                self.success = True



    def run(self, vel_x, vel_z):
        self.twist_msg.linear.x = vel_x
        self.twist_msg.angular.z = vel_z
        self.pub.publish(self.twist_msg)






if __name__ == '__main__':
    rospy.init_node('move_bb8_node')
    MoveBB8()
    rospy.spin()
