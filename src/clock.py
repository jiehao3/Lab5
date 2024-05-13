import time
from threading import Thread
from hal import hal_lcd as lcd 

def update_time():
    while True:
        current_time = time.localtime()
        time_string = time.strftime("%H:%M:%S", current_time)
        lcd.clear()
        lcd.set_cursor(0, 0)
        lcd.write_string(time_string)
        time.sleep(1)  


def blink_colons():
    while True:
        lcd.set_cursor(0, 2)  
        lcd.write_string(" ")  
        time.sleep(0.5)
        lcd.write_string(":")  
        time.sleep(0.5)

lcd.init()
time_thread = Thread(target=update_time)
colon_thread = Thread(target=blink_colons)
time_thread.start()
colon_thread.start()
