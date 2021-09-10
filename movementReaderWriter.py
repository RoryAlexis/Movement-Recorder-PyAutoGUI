import pyautogui
from  pynput import keyboard, mouse
import time
import os

def countdown():
    for i in range(10):
        time.sleep(1)
        if i < 9:
            s = 's'
        else:
            s = ''
        print('You have {} second{} left to get ready'.format(10-i, s))
    print('It is now recording!')

def getFileName():
    counter = 1
    found = False
    while not found:
        tryFile = 'autoGUIscript{}.py'.format(counter)
        if os._exists('C:\\Users\\49151\\appose\\{}'.format(tryFile)):
            counter += 1
        else:
            break
    return tryFile

def on_press(key):
    keyPressed = ''
    try:
        keyPressed = key.char
    except AttributeError:
        keyPressed = key
    fileString.append('pyautogui.keyDown({})'.format(keyPressed))
    
def on_release(key):
    fileString.append('pyautogui.keyUp({})'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def movementReader():
    global fileString
    fileString = []
    fileString.append('import pyautogui')
    fileString.append('sizeX, sizeY = pyautogui.size()')
    fileString.append('mouseX, mouseY = pyautogui.position()')    
    for _ in range(400):
        positionX, positionY = pyautogui.position()
        fileString.append('pyautogui.moveTo({}, {})'.format(positionX,positionY))
        '''with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
            listener.start()
            startTime = time.time()
            endTime = time.time()
            while (endTime-startTime) < .05:
                print((endTime-startTime))
                endTime = time.time()
            listener.stop()'''
        time.sleep(.05)
    return fileString
def movementWriter(listofInstructions, name):
    with open(name, 'w', encoding='utf-8') as f:
        for line in listofInstructions:
            f.write(line)
            f.write('\n')


countdown()
fileName = getFileName()
instructions = movementReader()
movementWriter(instructions, fileName)
print('done')

