import time
import RPi.GPIO as GPIO
from keypad import keypad 
GPIO.setwarnings(False)
import I2C_LCD_driver
mylcd= I2C_LCD_driver.lcd()
i = 0 
def tampilan():
   kp = keypad(columnCount = 3)
 
    # waiting for a keypress
   digit = None
   while digit == None:
       digit = kp.getKey()
   i = 0 
   i+=1
   mylcd.lcd_display_string(str(digit), 2, (i))
   time.sleep(0.5)
while True:
   # Initialize
    kp = keypad(columnCount = 3)
 
    # waiting for a keypress
    digit = None
    while digit == None:
        digit = kp.getKey()
    tampilan
