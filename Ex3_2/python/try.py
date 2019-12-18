#! /usr/bin/env python
import rospy





class MoveBB8:
    '''class that allows square movements to bb_8'''

    def __init__(self, side, repetitions):        
        
      
        self.side = side
        self.repetitions = repetitions
        self.time = self.side / 0.2
        self.success = False
        self.count = 0


        while not rospy.is_shutdown() and self.success == False :
            if self.repetitions > self.count:
                self.run()
                rospy.sleep(self.time)
                self.run()
                rospy.sleep(4.0)
                self.run()
                rospy.sleep(2.6)
                self.count += 1
                print("count = ", self.count)
            else:
                self.success = True

	print('End',self.success)



    def run(self):
	print('running')
        






if __name__ == '__main__':
    rospy.init_node('move_bb8_node')
    MoveBB8(1,3)
    rospy.spin()
