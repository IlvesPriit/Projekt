
import tkinter as tk

# see oleks siis kui asi 0 tiksub aga ei oska rakendada seda veel 
def countdown2():
    if (olek):
        global timer

        # sekund juurde
        timer[2] += 1

        if (timer[2] >= 60):
            timer[2] = 0
            timer[1] += 1

        if (timer[1] >= 60):
            timer[0] = 0
            timer[1] += 1
        # We create our time string here
        timeString = pattern.format(timer[0], timer[1], timer[2])
        # Update the timeText Label box with the current time
        timeText.configure(text=timeString)
        # Call the countdown() function after 1 centisecond
    root.after(1000, countdown)

def countdown():
    if(olek):
        global timer
        if (timer[2] > 0 or timer[1]>0 or timer[0]>0):
            if (timer[2] >0 ):
                timer[2] -= 1

            elif (timer[2] == 0 and timer[1]>0):
                timer[1] = timer[1]-1
                timer[2] = 59
            
            elif (timer[2] == 0 and timer[1]==0 and timer[0]>0):
                timer[0]=timer[0]-1
                timer[1]=59
                timer[2]=59

        timeString = pattern.format(timer[0], timer[1], timer[2])
        timeText.configure(text=timeString)
    root.after(1000, countdown)
olek2 = True
#'''
#start
def start():
    global olek
    olek = True
    pauseButton.pack_forget()
# pause
def pause():
    global olek
    olek = False

# reset
def reset():
    global timer
    timer = lõppjärjend
    timeText.configure(text=aeg)

#kõik kinni
def exist():
    root.destroy()

# aja split
aeg = "00:00:06"
järjend = aeg.split(":")
lõppjärjend= []
for i in järjend:
    i = int(i)
    lõppjärjend +=[i]


# olek:
# False: taimer ei tööta
# True: taimer töötab
olek = False
root = tk.Tk()
root.wm_title('Timer')
#siia peaks siis minema lõhutud aja list
# kust esimesed nullid on eemaldtatud

timer = lõppjärjend
#format
pattern = '{0:02d}:{1:02d}:{2:02d}'

#teksti asemele kogu sisend(AEG)
timeText = tk.Label(root, text=aeg, font=(50))
timeText.pack()

startButton = tk.Button(root, text='Start', command=start)
startButton.pack()

pauseButton = tk.Button(root, text='Pause', command=pause)

pauseButton.pack()
resetButton = tk.Button(root, text='Reset', command=reset)

resetButton.pack()

quitButton = tk.Button(root, text='Quit', command=exist)

quitButton.pack()

countdown()

root.mainloop()
