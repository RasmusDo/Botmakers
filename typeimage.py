import pytesseract
import keyboard
from time import sleep
from PIL import Image
from PIL import ImageGrab

word_list = []



pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

while True:
    if(keyboard.is_pressed("SPACE")):
        img = ImageGrab.grab(bbox=(566,477,1356,777))
        img.save("test.png")
        result = pytesseract.image_to_string(img)

    elif(keyboard.is_pressed("BACKSPACE")):
        for i in result:
            with open("fil.txt", "w") as f:
                f.write(result)
            count = 0

            if count < len(result)-98:
                if(i.islower() == True):
                    keyboard.press_and_release(i)
                    count += 1
                    sleep(0.1)
                elif(i == ("|")):
                    keyboard.press_and_release("i")
                    count += 1
                    sleep(0.1)
                elif(i == ("[")):
                    pass
                elif(i == ("\n"))
                    keyboard.press_and_release("SPACE")
                    count += 1
                    sleep(0.1)
                else:
                    keyboard.press_and_release("SHIFT + " + i)
                    count += 1
                    sleep(0.1)

            else:
                break

    elif(keyboard.is_pressed("ESC")):
        break

