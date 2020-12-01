import keyboard
from time import sleep

bomb = "!bruh \n"
while True:
    if(keyboard.is_pressed("BACKSPACE")):
        for i in range(10):
            for char in (bomb):
                if(char.islower() == True):
                    keyboard.press_and_release(char)
                    sleep(0.001)
                elif(char == ("!")):
                    keyboard.press_and_release("SHIFT + " + char)
                    sleep(0.001)
                elif(char == ("\n")):
                    keyboard.press_and_release("space")
                    keyboard.press_and_release(int(i))
                    keyboard.press_and_release("enter")
                    sleep(0.001)
    elif(keyboard.is_pressed("ESC")):
        break
