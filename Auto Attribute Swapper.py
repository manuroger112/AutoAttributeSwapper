import win32api
import win32con
import tkinter as tk
import threading
import time



window = tk.Tk()
StopThread = False

#keybind vars
Item1 = 1
Item2 = 2
startHitKey = 0x06

#Creating sliders above so that I can use it in script fn
DelaySetter = tk.Scale(window, from_=30, to=200, orient=tk.HORIZONTAL)
DelaySetterMouse = tk.Scale(window, from_=50, to=200, orient=tk.HORIZONTAL)
DelaySetterPresses = tk.Scale(window, from_=75, to=200, orient=tk.HORIZONTAL)

def script():
    global Item1, Item2, StopThread, window, startHitKey, DelaySetter, DelaySetterMouse, DelaySetterPresses

    DelaySetter.set(100)
    DelaySetterMouse.set(100)
    DelaySetterPresses.set(100)
    
    while StopThread == False:
        time.sleep(0.01)
        
        if win32api.GetAsyncKeyState(startHitKey) & 1:

            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.keybd_event(ord(str(Item2)), 0, 0, 0)
            time.sleep(DelaySetterMouse.get() / 1000)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            time.sleep(DelaySetterPresses.get() / 1000)
            win32api.keybd_event(ord(str(Item2)), 0, win32con.KEYEVENTF_KEYUP, 0)

            time.sleep(DelaySetter.get() / 1000)
    
            win32api.keybd_event(ord(str(Item1)), 0, 0, 0)
            time.sleep(DelaySetterMouse.get()/1000)
            win32api.keybd_event(ord(str(Item1)), 0, win32con.KEYEVENTF_KEYUP, 0)
            
        elif win32api.GetAsyncKeyState(0x2D):
            print("bye!")
            window.destroy()
            break;



def CreateBindListener():
    
    bindButtonHit.config(text = "Listening...")
    global startHitKey
    stop = False
    while stop==False:
        time.sleep(0.001)
        for VKcode in range(3, 166):
            
            if win32api.GetAsyncKeyState(VKcode) & 0x8000:
                startHitKey = VKcode
                if 48 <= startHitKey <= 90:
                    showHitBind.config(text=chr(startHitKey))
                else:
                    showHitBind.config(text=hex(startHitKey))
                stop = True
                break
    
    bindButtonHit.config(text = "Bind StartKey")
    

def FirstItemSelection():
    global Item1
    Item1 += 1
    Item1 = (Item1 - 1) % 9 + 1
    if(Item2 == Item1):
        Item1 += 1
        Item1 = (Item1 - 1) % 9 + 1
    ShowSelection1.config(text=Item1)
    

def SecondItemSelection():
    global Item2
    Item2 += 1
    Item2 = (Item2 - 1) % 9 + 1
    if(Item2 == Item1):
        Item2 += 1
        Item2 = (Item2 - 1) % 9 + 1
    ShowSelection2.config(text=Item2)

def onExit():
    global StopThread
    StopThread = True
    window.destroy()



thread = threading.Thread(target=script)
thread.start()

window.geometry("700x700")
window.title("TickHitter")
window.config(background="#73600b")

#Title
MainTitle = tk.Label(window, text="manuroger112's auto Tick Hitter/Attribute Swapper", font=('Comic Sans', 20, 'bold'), bd = 10)
MainTitle.place(x=350, y=50, anchor= tk.CENTER)

#Selecting Location For First Item
Selection1 = tk.Label(window, text="Item providing damage", font=('Arial', 15, 'bold'), bd = 10)
Selection1.place(x=350, y=200, anchor=tk.CENTER) #place it on screen window
Description1 = tk.Label(window, text="Hold your item before starting usage (it's better)", font=('Arial', 8, 'bold'), bg="#73600b")
Description1.place(x=350, y=170, anchor=tk.CENTER)

buttonS1 = tk.Button(window, text="Hotbar Number: ");
buttonS1.config(command = FirstItemSelection, font= ('Arial', 9, 'bold'))
buttonS1.place(x=350, y=270, anchor=tk.CENTER, width = 100, height = 50)
ShowSelection1 = tk.Label(window, text=Item1, font=('Arial', 20, 'bold'))
ShowSelection1.place(x=430, y = 270, anchor=tk.CENTER)

#Selecting Location For Second Item
Selection2 = tk.Label(window, text="Item providing enchants/Durability deflector", font=('Arial', 15, 'bold'), bd = 10)
Selection2.place(x=350, y=350, anchor=tk.CENTER)
Description2 = tk.Label(window, text="(Second item can be set to a hotbar with nothing in it (resulting in first item receiving 0 damage upon its durability))", font=('Arial', 8, 'bold'), bg="#73600b")
Description2.place(x=350, y=670, anchor=tk.CENTER)

buttonS2 = tk.Button(window, text="Hotbar Number: ");
buttonS2.config(command = SecondItemSelection, font= ('Arial', 9, 'bold'))
buttonS2.place(x=350, y=420, anchor=tk.CENTER, width = 100, height = 50)
ShowSelection2 = tk.Label(window, text=Item2, font=('Arial', 20, 'bold'))
ShowSelection2.place(x=430, y = 420, anchor=tk.CENTER)

#Exit Button
buttonExit = tk.Button(window, text="EXIT");
buttonExit.config(command = onExit, font= ('Arial', 13, 'bold'))
buttonExit.place(x=30, y=125, width = 100, height = 50)

#Bind Start Button
bindButtonHit = tk.Button(window, text="Bind StartKey");
bindButtonHit.config(command = CreateBindListener, font= ('Arial', 13, 'bold'))
bindButtonHit.place(x=550, y=100, width = 150, height = 50)
showHitBind = tk.Label(window, text=hex(startHitKey), font=('Arial', 15, 'bold'))
showHitBind.place(x=630, y = 165, anchor=tk.CENTER)

#Configuration Of The 3 Delays

DelaySetter.place(x=500, y=550, width = 175)
DelaySetterTitle = tk.Label(window, text="Return To First Item Delay (ms)", font=('Arial', 11, 'bold'), bg="#73600b")
DelaySetterTitle.place(x=590, y = 520, anchor=tk.CENTER)

DelaySetterMouse.place(x=280, y=550, width = 175)
DelaySetterMouseTitle = tk.Label(window, text="Key&Click Down/Up Delay (ms)", font=('Arial', 11, 'bold'), bg="#73600b")
DelaySetterMouseTitle.place(x=360, y = 520, anchor=tk.CENTER)

DelaySetterPresses.place(x=50, y=550, width = 175)
DelaySetterPressesTitle = tk.Label(window, text="Delays Between Presses (ms)", font=('Arial', 11, 'bold'), bg="#73600b")
DelaySetterPressesTitle.place(x=130, y = 520, anchor=tk.CENTER)

window.mainloop() #place window on pc screeen and listen for events




