#from gpiozero import DistanceSensor,Button
#import RPi.GPIO as GPIO
import time
#import datetime
import requests
import json

#button = Button(4)
#sensor = DistanceSensor(24, 18)


#while True:
#	jarak = sensor.distance*100	
#data = '\r\n{\r\n  "m2m:cin": {\r\n    "cnf": "message",\r\n    "con": "\r\n      {\r\n      \t \\"Temperature\\": \\"'+str(40)+'\\"\r\n }\r\n    "\r\n  }\r\n}'
data = '\r\n{\r\n  "m2m:cin": {\r\n    "cnf": "message",\r\n    "con": "\r\n      {\r\n      \t \\"user_id\\": \\"'+str(123)+'\\",\r\n \\"height\\": \\"'+str(180)+'\\",\r\n \\"weight_ideal\\": \\"'+str(75)+'\\"\r\n   }\r\n    "\r\n  }\r\n}'
url = 'https://platform.antares.id:8443/~/antares-cse/antares-id/sohit/test'
headers =  {'cache-control':'no-cache','content-type':'application/json;ty=4','x-m2m-origin':'2f2b5c0e49d365b0:f68b99c78b62a9b3'}
requests.post(url,headers=headers,data=data)
#time.sleep(2)
