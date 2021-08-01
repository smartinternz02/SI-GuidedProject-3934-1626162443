#! /usr/bin/env python
import rospy
rospy.init_node("node3")
rate=rospy.Rate(2)
while not rospy.is_shutdown():
    print "Assignment3"
    rate.sleep()