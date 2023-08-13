from send import conncet
import time 
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller


kirim = conncet ()
keyboard = Controller()


kirim.send_whatsapp_message(msg="peni")
keyboard.press(Key.enter)
