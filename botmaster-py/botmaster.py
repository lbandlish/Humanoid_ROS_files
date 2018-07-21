#!/usr/bin/env python

import threading
import rospy
import roslaunch
# from speech_pkg.srv import mode_srv
from turtlesim.srv import Spawn

global flag2
flag2 = 0

global give_command
give_command = "foo"

global flag
flag = 0

# global process
node = roslaunch.core.Node('turtlesim','turtlesim_node')

launch = roslaunch.scriptapi.ROSLaunch()
launch.start()

process = launch.launch(node)
process.stop()

global success
success = 2						# 2 is a random value (any value other than 0 and 1 would suffice)

rospy.init_node('botmaster')	# can put a test here to check if botmaster is reinitialized due to some breakdown and proceed accordingly

class myThread (threading.Thread):	
	def __init__(self, threadID, name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		
	def run(self):
		print "Starting " + self.name2
		initialize_botmaster()
		print "Exiting " + self.name

def api_roslaunch(str1,str2):
	global process
	global success
	global flag2

	node = roslaunch.core.Node(str1,str2)

	launch = roslaunch.scriptapi.ROSLaunch()
	launch.start()

	process = launch.launch(node)

	flag2 = 1

	if process.is_alive():
		success = 1

	else:
		success = 0

def callback_fn(req):
	global success
	global command
	global flag

	# command = req.comm
	command = req.name       #Use this line instead of the above if this code is used to run turtlesim node instead of line following, object tracking etc.
	flag = 1

	while 1:
		if success is 1:
			success = 2
			return "1"
			break

		if success is 0:
			success = 2
			return "0"
			break
	

def initialize_botmaster():
	# s = rospy.Service('give_command',mode_srv,callback_fn)
	s = rospy.Service('give_command',Spawn,callback_fn)
	
	rospy.loginfo("Botmaster is ready for commands.")

	rospy.spin()

def run_node():
	global give_command
	global success
	global flag
	global process
	global flag2

	while not rospy.is_shutdown():
		if flag is 1:
			if not give_command is command:
				give_command = command

				if give_command is "o":
					if flag2 is 1:
						process.stop()	

					print "o\n"			# to be deleted						
					api_roslaunch("turtlesim","turtlesim_node")			# change this line to run another node.

				elif give_command is "l":
					if flag2 is 1:
						process.stop()
					
					print "l\n"			# to be deleted
					api_roslaunch("turtlesim","turtle_teleop_key")		# change this line to run another node.
					
				elif give_command is "t": # to be changed.
					if flag2 is 1:
						process.stop()

					print "t\n"			# to be deleted
					api_roslaunch("turtlesim","turtlesim_node")			# change this line to run another node.

				# else success = 1 , in case request can send garbage values, which don't have any meaning but require 1 as response(not imp line)

			else:
				if process.is_alive():
					success = 1

				else:													# subsequent block of code tries to start a node when a request is received which wasn't ableo to start the code in the first instance.
					if give_command is "o":								
						api_roslaunch("'turtlesim','turtlesim_node'")	# change this line to run another node.

					elif give_command is "l":
						api_roslaunch("'turtlesim','turtlesim_node'")	# change this line to run another node.

					elif give_command is "t": # to be changed.
						api_roslaunch("'turtlesim','turtlesim_node'")	# change this line to run another node.

			flag = 0
		
Thread = myThread(1,"Thread")
Thread.start()

run_node()

# can put a condition which tells if shutdown occured, then send logerr message.	