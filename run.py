#!/usr/bin/python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
var = 1
Relay = 4
Sensor = 17
GPIO.setup(Sensor, GPIO.IN)
GPIO.setup(Relay, GPIO.OUT)
GPIO.output(Relay, GPIO.HIGH)
while var == 1:
	if GPIO.input(Sensor):
 		print "PUMP ON"
		GPIO.output(Relay, GPIO.LOW)
	else:
		print "PUMP OFF"
		GPIO.output(Relay, GPIO.HIGH)
#	except KeyboardInterrupt:
#	  print " Quit"
#	  GPIO.cleanup()
