

from tkinter import *
#from tkinter import ttk
#from time import *
from time import time
#def aeg():
    #print(time())

def start(raam, rida, kiri):
    nupp = Button(raam, cursor="hand2", text=" Start ",font=kiri, bg="lime green", command=lambda : stopp(raam, rida, kiri))
    #sulgudesse vaja ka command = alustab aja lugemist, mis on funktsioonis aeg
    nupp.grid(column=4, row = rida,  padx=5, pady=6)
    print(time())

def stopp(raam, rida, kiri):
    print('toimib1')
    # soovime, et nupp veniks nii laiuses kui ka kõrguses
    #b = time()
    nupp = Button(raam, cursor="hand2", text="Stopp",font=kiri, bg="tomato", command=lambda: start(raam, rida, kiri))
    #sulgudesse vaja ka command = alustab aja lugemist, mis on funktsioonis aeg
    nupp.grid(column=4, row=rida, padx=5, pady=6)
    print(time())

