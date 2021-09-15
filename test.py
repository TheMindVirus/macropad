#pip install keyboard
import keyboard

def onKeyPress(key):
    print(key)
    
keyboard.hook(onKeyPress)
    
