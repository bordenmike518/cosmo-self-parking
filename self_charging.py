import sys
import time
import cozmo
import numpy as np
import cv2
from cozmo.util import degrees  # use radians if desired

def run(sdk_conn):
	robot = sdk_conn.wait_for_robot()
	find_charger(robot)
	
def find_charger(robot):
	battery_icon = cv2.CascadeClassifier('cascades/battery_icon_cascade.xml')
	robot.set_lift_height(0).wait_for_completed()
	robot.set_head_angle(degrees(0)).wait_for_completed()
	lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
	while 1:
		img = robot.world.raw_image()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		batteryIcon = battery_icon.detectMultiScale(gray,2,6)

		for (x,y,w,h) in batteryIcon:
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
			print ('x = %.2f y = %.2f' % (x, y))

		cv2.imshow('img',img)
		k = cv2.waitKey(30) & 0xff
		if k == 27:
			lookaround.stop()
			return
	lookaround.stop()

def backup_onto_charger(robot):
	robot.drive_wheels(-30, -30)
	time_waited = 0.0
	while time_waited < 3.0 and not robot.is_on_charger:
		sleep_time_s = 0.1
		time.sleep(sleep_time_s)
		time_waited += sleep_time_s
	robot.stop_all_motors()

if __name__ == '__main__':
	cozmo.setup_basic_logging()
	try:
		cozmo.connect(run)
	except cozmo.ConnectionError as e:
		sys.exit("A connection error occurred: %s" % e)
