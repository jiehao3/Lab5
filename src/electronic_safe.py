from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
#Empty list to store sequence of keypad presses
password = [1234]
attempt = []
lcd = LCD.lcd()
lcd.lcd_clear()

#Call back function invoked when any key on keypad is pressed
def key_pressed(key):
    count = 0
    attemptcount = 0
    attempt.append(key)
    if count < 4:
        count +=1
        if password == attempt:
            lcd.lcd_clear()
            lcd.lcd_display_string("Safe Unlocked",1)
            lcd.lcd_display_string(" ",2)
        else:
            lcd.lcd_display_string("Wrong Password",1)
            lcd.lcd_display_string(" ",2)
            attemptcount+=1
            if attemptcount == 3:
                lcd.lcd_clear()
                lcd.lcd_display_string("Safe disabled",1)
                lcd.lcd_display_string(" ",2)
        
def main():
    # Initialize LCD
    lcd = LCD.lcd()
    lcd.lcd_clear()

    lcd.lcd_display_string("Safe Lock", 1)
    lcd.lcd_display_string("Enter PIN: ",2)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()
   


# Main entry point
if __name__ == "__main__":
    main()
