import pyautogui as pui
import keyboard
import mouse
import time

sims_status = None

def click(x,y) :
      mouse.move(x,y, duration=0.20)
      time.sleep(.5)
      mouse.click()

def checkTablet():
      if pui.pixel(1535,914)[2] != 170:
        print('not in the first spot')
        click(1575,759)
        click(1287,767)
        time.sleep(.5)
def createJob():
     click(1555,883)
     click(1749,862)
     click(1542,757)
def checkIfDone():
        while True:
            print(pui.pixel(32,1011))
            time.sleep(1)
            if pui.pixel(32,1011)[0] != 248:
                mode = None
                test = 0
                return True
      
mode = 0

while True:
    time.sleep(2)
#Check to see if start button is being pressed
    if keyboard.is_pressed('f9') == True :
            mode = 1
    if mode == 0 :
            print('test')
            time.sleep(5)
    elif mode == 1 :
        keyboard.press_and_release('i')
        time.sleep(.5)
        x = 0
        while x < 6:
            #Check tablet is in the correct position
            checkTablet()
            createJob()
            print(x)
            x += 1
            time.sleep(1)
            if x == 6 :
                  keyboard.press_and_release('3')
                  keyboard.press_and_release('i')
                  pui.moveTo(32,1011)
                  time.sleep(24)
                  checkIfDone()
                  if checkIfDone() is True:
                        print('Done')
                        keyboard.press_and_release('0')
        #Check if the termamite buttons are being pressed
            if keyboard.is_pressed('f12') == True:
                        mode = 0
                        test = 0
                        break
#Used to end program once in the pause/mode 1
    if keyboard.is_pressed('shift + f12') == True:
          break
