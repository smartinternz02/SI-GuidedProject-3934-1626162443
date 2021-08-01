#! /usr/bin/env python

import rospy
rospy.init_node("node1")
rate=rospy.Rate(2)
while not rospy.is_shutdown():
    print "This"
    rate.sleep()


