#!/usr/bin/env python

import sys
import rospy
from turtlesim.srv import Spawn

def call():
	rospy.wait_for_service('give_command')

	rospy.loginfo("Sending request\n")

	try:
		command = rospy.ServiceProxy('give_command',Spawn)

		x = 0
		y = 0
		theta = 0
		name = sys.argv[1]

		resp = command(x,y,theta,name)
		return resp
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e



if __name__ == "__main__":
	print "calling botmaster"
	print "response received: %s" % call()
