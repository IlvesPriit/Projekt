from tkinter import *

def start(raam,rida,kiri):
    global olek
    olek = True
    nupp = Button(raam,cursor="hand2",text=" Start ",font=kiri,bg="lime green",command=lambda: stopp(raam,rida,kiri))
    #sulgudesse vaja ka command = alustab aja lugemist, mis on funktsioonis aeg
    nupp.grid(column=4, row=rida,  padx=5, pady=6)

def stopp(raam,rida,kiri):
    global olek
    olek = False
    print('toimib1')
    # soovime, et nupp veniks nii laiuses kui ka kõrguses
    nupp = Button(raam, cursor="hand2", text="Stopp",font=kiri, bg="tomato", command=lambda: start(raam,rida,kiri))
    #sulgudesse vaja ka command = alustab aja lugemist, mis on funktsioonis aeg
    nupp.grid(column=4, row=rida, padx=5, pady=6)

#stopi funktsioonid
#def stopinupp(raam, rida, kiri):
    #update_clock(raam, pattern, clock, olek)
    #start(raam, rida, kiri, pattern, clock, olek)

# #stardi funktsioonid
def stardinupp(pattern, clock, raam, rida, kiri, olek):
    #stopp(raam, rida, kiri, pattern, clock, olek)
    update_clock(raam, pattern, clock, olek)

#siin hakkab stopper tiksuma
def update_clock(raam, pattern, clock, olek):
    if olek == True:
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
    #clock.after(10, lambda: update_clock((pattern, clock, olek)))
    raam.after(10, lambda: update_clock(raam, pattern, clock, olek))
