import pyautogui
import time
import win32api
import random
import keyboard
import ctypes

banner = """
███████╗██╗░░██╗░█████╗░  
██╔════╝╚██╗██╔╝██╔══██╗  
█████╗░░░╚███╔╝░██║░░██║  
██╔══╝░░░██╔██╗░██║░░██║  
███████╗██╔╝╚██╗╚█████╔╝  
╚══════╝╚═╝░░╚═╝░╚════╝░  

░█████╗░███╗░░██╗████████╗██╗  ██████╗░███████╗░█████╗░░█████╗░██╗██╗░░░░░
██╔══██╗████╗░██║╚══██╔══╝██║  ██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██║░░░░░
███████║██╔██╗██║░░░██║░░░██║  ██████╔╝█████╗░░██║░░╚═╝██║░░██║██║██║░░░░░
██╔══██║██║╚████║░░░██║░░░██║  ██╔══██╗██╔══╝░░██║░░██╗██║░░██║██║██║░░░░░
██║░░██║██║░╚███║░░░██║░░░██║  ██║░░██║███████╗╚█████╔╝╚█████╔╝██║███████╗
╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝  ╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝╚══════╝
"""

horizontal_range = 2

min_vertical = 7.8
max_vertical = 7.9

min_firerate = 0.03
max_firerate = 0.04

toggle_button = 'f2'

enabled = False
 
def is_mouse_down():    
    lmb_state = win32api.GetKeyState(0x01)
    return lmb_state < 0
 

print(banner)
print("EXO Anti Recoil running without error")
print(f"The start/stop key is {toggle_button}")
if enabled:
    print("EXO Anti Recoil is ENABLED")
else:
    print("EXO Anti Recoil is DISABLED")
 
last_state = False
while True:
    key_down = keyboard.is_pressed(toggle_button)
    
    if key_down != last_state:
        last_state = key_down
        if last_state:
            enabled = not enabled
            if enabled:
                print("EXO ANTI RECOIL ENABLED")
            else:
                print("EXO ANTI RECOIL DISABLED")
    
    if is_mouse_down() and enabled:
        
        offset_const = 1000
        horizontal_offset = random.randrange(-horizontal_range * offset_const, horizontal_range * offset_const, 1) / offset_const
        vertical_offset = random.randrange(min_vertical * offset_const, max_vertical * offset_const, 1) / offset_const
 
        
        ctypes.windll.user32.mouse_event(0x1, int(horizontal_offset),int(vertical_offset),0,0)
 
        
        time_offset = random.randrange(min_firerate * offset_const, max_firerate * offset_const, 1) / offset_const
        time.sleep(time_offset)
    
    time.sleep(0.001)
