import time 
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller

keyboard = Controller()

class conncet :

    def send_whatsapp_message(self,msg=str):
        try:
            pywhatkit.sendwhatmsg_instantly(
                phone_no="+6288286017661", 
                message=msg,
            # tab_close=True
            )
            time.sleep(0)
            pyautogui.click()
            time.sleep(0)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            print("Message sent!")
        except Exception as e:
            print(str(e))
        
       