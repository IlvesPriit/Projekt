

from tkinter import *
#from tkinter import ttk
#from time import *
#import time

def start(raam, rida, kiri, pattern, clock):
    global olek
    olek = True
    nupp = Button(raam,cursor="hand2",text=" Start ",font=kiri,bg="lime green",command=lambda: stopp(raam,rida,kiri,pattern,clock))
    #sulgudesse vaja ka command = alustab aja lugemist, mis on funktsioonis aeg
    nupp.grid(column=4, row=rida,  padx=5, pady=6)


def stopp(raam,rida,kiri,pattern,clock):
    global olek
    olek = False
    print('toimib1')
    # soovime, et nupp veniks nii laiuses kui ka kõrguses
    nupp = Button(raam, cursor="hand2", text="Stopp",font=kiri, bg="tomato", command=lambda: stopinupp(pattern,clock,raam,rida,kiri))
    #sulgudesse vaja ka command = alustab aja lugemist, mis on funktsioonis aeg
    nupp.grid(column=4, row=rida, padx=5, pady=6)

#stopi funktsioonid
def stopinupp(pattern, clock, raam, rida, kiri):
    update_clock(pattern, clock)
    start(raam, rida, kiri, pattern, clock)


#siin hakkab stopper tiksuma
def update_clock(pattern, clock):
    if (olek):
        global timer
        timer[2] += 1
        if (timer[2] >= 100):
            timer[2] = 0
            timer[1] += 1
        if (timer[1] >= 60):
            timer[0] += 1
            timer[1] = 0
        timeString = pattern.format(timer[0], timer[1], timer[2])
        clock.configure(text=timeString)
    clock.after(10, update_clock(pattern, clock))

