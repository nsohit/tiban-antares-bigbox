from gpiozero import DistanceSensor,Button
from time import sleep
from signal import pause
import RPi.GPIO as GPIO
import requests
import json
import I2C_LCD_driver
import subprocess
mylcd = I2C_LCD_driver.lcd()
#cnt = 0
button=Button(18)
sensor= DistanceSensor(27,17)
#nama = input("nama : ")
#kelas = input ("kelas : ")
#no_wali = int(input("no_wali : ")
#jarak = sensor.distance*100
nama = input("nama : ")
#kelas = input ("kelas : ")
#no_wali = int(input("no_wali : "))
i=0
"""
   for i  in range (9):
      jarak = 190 - (sensor.distance*100) #tinggi badan
      berat_ideal = (jarak - 100) - 0.1*(jarak-100)
"""

while True:
   gape = 190
   jarak = gape - (sensor.distance*200) #tinggi badan
   berat_ideal = (jarak - 100) - 0.1*(jarak-100)
   
   if button.is_pressed:
      for i  in range (9):
         jarak = gape - (sensor.distance*100) #tinggi badan
         berat_ideal = (jarak - 100) - 0.1*(jarak-100)
      mylcd.lcd_display_string("nama :%s " % nama, 1, 0)
      mylcd.lcd_display_string("tinggi:%d" % jarak, 4, 1)
      mylcd.lcd_display_string("berat ideal:%d" %berat_ideal, 2, 0)
      data = '\r\n{\r\n  "m2m:cin": {\r\n    "cnf": "message",\r\n    "con": "\r\n      {\r\n      \t \\"nama\\": \\"'+str(nama)+'\\",\r\n \\"berat_ideal\\": \\"'+str(berat_ideal)+'\\",\r\n \\"Tinggi_anak\\": \\"'+str(jarak)+'\\"\r\n  }\r\n    "\r\n  }\r\n}'
      url = 'https://platform.antares.id:8443/~/antares-cse/antares-id/sohit/test'
      headers =  {'cache-control':'no-cache','content-type':'application/json;ty=4','x-m2m-origin':'2f2b5c0e49d365b0:f68b99c78b62a9b3'}
      requests.post(url,headers=headers,data=data)
      subprocess.call(["curl", "-X", "POST", "https://api.thebigbox.id/sms-notification/1.0.0/messages", "-H", "accept: application/x-www-form-urlencoded", "-H", "x-api-key: siRoNm3Te3mHkqt5CeAkXBgL1X5I0Uhc", "-H", "Content-Type: application/x-www-form-urlencoded", "-d", "msisdn=081388056019&content= tinggi_anda%d berat_ideal%d "%(jarak,berat_ideal)])

      print("sukses kirim data")
      sleep(1)


