__author__ = 'Karin'

from tkinter import *
from tkinter import ttk
from time import *
from time import time

def stopp(raam):
    print('toimib1')
    # soovime, et nupp veniks nii laiuses kui ka kõrguses
    a = time()
    nupp = ttk.Button(raam, text="Stopp", command=a)
    #sulgudesse vaja ka command = alustab aja lugemist, mis on funktsioonis aeg
    nupp.grid(column=4, row=2, padx=5, pady=5)

