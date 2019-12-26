"""
import I2C_LCD_driver

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Hello World!", 2, 3)
"""
import I2C_LCD_driver


mylcd = I2C_LCD_driver.lcd()
nama = input ("nama : ")
kelas = input("keles : ")
no_wali = int(input ("no_wali : "))

mylcd.lcd_display_string(nama, 1, 3)
mylcd.lcd_display_string(kelas, 2, 3)
mylcd.lcd_display_string(str(no_wali), 3, 3)


