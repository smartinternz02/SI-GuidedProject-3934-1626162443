#! /usr/bin/env python
import rospy
rospy.init_node("node2")
rate=rospy.Rate(2)
while not rospy.is_shutdown():
    print "Is"
    rate.sleep()