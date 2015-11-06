#!/usr/bin/env python3
import requests
import json
import time
import datetime
from time import gmtime, strftime
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
url = "http://friskby.herokuapp.com/sensor/api/reading/"
headers = {"Content-Type" : "application/json"}
api_key = "GET YOUR OWN KEY!!!"
while True:
	
	# read data from Arduino
	s = ser.readline()
	# decode the data into a list l
	l = s.decode("utf-8", "ignore").strip(" ").split(',')
	# print(l)
	
	# replace with your own sensorid's
	data = [{"sensorid" : "NJBStoevGronnlien" ,"timestamp" : datetime.datetime.utcnow().isoformat() , "value" : l[0], "key" : api_key},
			{"sensorid" : "NJBTempGronnlien"  ,"timestamp" : datetime.datetime.utcnow().isoformat() , "value" : l[1], "key" : api_key},
			{"sensorid" : "NJBFuktGroennlien" ,"timestamp" : datetime.datetime.utcnow().isoformat() , "value" : l[2], "key" : api_key},
			{"sensorid" : "NJBGassGroenllien" ,"timestamp" : datetime.datetime.utcnow().isoformat() , "value" : l[3], "key" : api_key}]
			
	for measurement in data:
		#data are posted to the API
		response = requests.post( url , data = json.dumps( measurement ) , headers = headers )
		if response.status_code == 201:
			print("OK - {}".format(response.text))
		else:
			print("ERROR - posting failed")
			print("Status: {}".format(response.status_code))
			print("Msg: {}".format(response.text))
	
