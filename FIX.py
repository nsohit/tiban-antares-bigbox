from gpiozero import DistanceSensor,Button
import time
from signal import pause
from keypad import keypad
import RPi.GPIO as GPIO
import requests
import json
import I2C_LCD_driver
import subprocess
mylcd = I2C_LCD_driver.lcd()
import subprocess
import sys

EMULATE_HX711=False
referenceUnit = -441

button=Button(18)
sensor= DistanceSensor(17,27)

mylcd.lcd_display_string("masukan userid", 1,0)
mylcd.lcd_display_string("******", 2,3)

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()

    print("Bye!")
    sys.exit()

hx = HX711(5, 6)

hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(referenceUnit)

hx.reset()

hx.tare()

       # val =max (0,int(hx.get_weight(5)))
      #  print(val)

while True:
   val =max (0,int(hx.get_weight(5)))
   kp = keypad(columnCount = 3)
   gape = 190
   jarak = gape - (sensor.distance*200) #tinggi badan
   berat_ideal = (jarak - 100) - 0.1*(jarak-100)
   seq = []
   for i in range(6):
       digit = None
       while digit == None:
           digit = kp.getKey()
       seq.append(digit)
       time.sleep(0.4)
   print(seq)
   str1 = ''.join(str(e) for e in seq)
   data = '\r\n{\r\n  "m2m:cin": {\r\n    "cnf": "message",\r\n    "con": "\r\n      {\r\n      \t \\"user_id\\": \\"'+str(str1)+'\\",\r\n \\"height\\": \\"'+str(jarak)+'\\",\r\n \\"ideal_weight\\": \\"'+str(berat_ideal)+'\\",\r\n  \\"weight\\": \\"'+str(val)+'\\"\r\n   }\r\n    "\r\n  }\r\n}'
   #data = '\r\n{\r\n  "m2m:cin": {\r\n    "cnf": "message",\r\n    "con": "\r\$
   url = 'https://platform.antares.id:8443/~/antares-cse/antares-id/sohit/test'
   headers = {'cache-control':'no-cache','content-type':'application/json;ty=4','x-m2m-origin':'2f2b5c0e49d365b0:f68b99c78b62a9b3'}
   requests.post(url,headers=headers,data=data)
   subprocess.call(["curl", "-X", "POST", "https://api.thebigbox.id/sms-notification/1.0.0/messages", "-H", "accept: application/x-www-form-urlencoded", "-H", "x-api-key: 6Bx6rLhdyxCmaQxfWtjkMQYFIjIzXZEt", "-H", "Content-Type: application/x-www-form-urlencoded", "-d", "msisdn=082120826723content= user_id%s tinggi_anda%d berat_ideal%d "%(str1,jarak,berat_ideal)])
   print("sukses")


