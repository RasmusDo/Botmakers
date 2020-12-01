import keyboard
from time import sleep

result = open('fil.txt', 'r').read()
"""   
while True:
    if(keyboard.is_pressed("BACKSPACE")):
        for i in result:
            with open("fil.txt", "w") as f:
                f.write(result)
            count = 0

            if count < len(result):
                if(i.islower() == True):
                    keyboard.press_and_release(i)
                    count += 1
                    sleep(0.1)
                elif(i == ("\n")):
                    keyboard.press_and_release("SPACE")
                    count += 1
                    sleep(0.1)
            else:
                break
    elif(keyboard.is_pressed("ESC")):
        break
"""

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