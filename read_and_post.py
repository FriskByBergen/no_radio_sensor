#!/usr/bin/env python3
import requests
import json
import time
import datetime
from time import gmtime, strftime
import serial

def isnumbers(l):
	itsanumber = True 
	try:
		for n in l:
			if not n.replace('.','1',1).isdigit():
				itsanumber = False
	except:
		return False
	return itsanumber

ser = serial.Serial('/dev/ttyACM0', 9600)
url = "http://friskby.herokuapp.com/sensor/api/reading/"
headers = {"Content-Type" : "application/json"}
api_key = "9c72f670-d60e-436e-b6b9-5cde41cd01a5"
while True:
		# read data from Arduino
	s = ser.readline()
		# decode the data into a list l
	l = s.decode("utf-8", "ignore").strip().replace(' ','').split(',')
	print(l)
		# test that we got 4 values
	if len(l) == 4 and isnumbers(l):
		#print("Line passed test \n")
		data = [{"sensorid" : "NJBStoevGronnlien" ,"timestamp" : datetime.datetime.utcnow().isoformat() , "value" : l[0], "key" : api_key},
			{"sensorid" : "NJBTempGronnlien"  ,"timestamp" : datetime.datetime.utcnow().isoformat() , "value" : l[1], "key" : api_key},
			{"sensorid" : "NJBFuktGroennlien" ,"timestamp" : datetime.datetime.utcnow().isoformat() , "value" : l[2], "key" : api_key},
			{"sensorid" : "NJBGassGroenllien" ,"timestamp" : datetime.datetime.utcnow().isoformat() , "value" : l[3], "key" : api_key}]
		
		for measurement in data:
			#data are posted to the API
			try:
				response = requests.post( url , data = json.dumps( measurement ) , headers = headers )
				if response.status_code == 201:
					print("OK - {}".format(response.text))
				else:
					print("ERROR - posting failed")
					print("Status: {}".format(response.status_code))
					print("Msg: {}".format(response.text))
			except:
				pass
	else:
		print("Line did not pass test \n")
		print(l)
