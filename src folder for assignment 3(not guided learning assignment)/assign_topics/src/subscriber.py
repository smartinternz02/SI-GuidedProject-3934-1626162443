#! /usr/bin/env python
import rospy
from std_msgs.msg import String
def callback(msg):
    print msg.data

rospy.init_node("subsciber")
sub=rospy.Subscriber('chatter', String, callback)
rospy.spin()