#! /usr/bin/env python
import rospy
from std_msgs.msg import String
pub = rospy.Publisher('/chatter', String, queue_size=1)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(2) 
while not rospy.is_shutdown():
    hello_str = "hello world %s" % rospy.get_time()
   
    pub.publish(hello_str)
    rate.sleep()