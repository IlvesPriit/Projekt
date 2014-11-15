__author__ = 'Karin'

from tkinter import *
from tkinter import ttk
from time import *
from time import time
def aeg():
    print(time())
def stopp(raam, rida):
    print('toimib1')
    # soovime, et nupp veniks nii laiuses kui ka kõrguses
    #b = time()
    nupp = ttk.Button(raam, text="Stopp", command=aeg)
    #sulgudesse vaja ka command = alustab aja lugemist, mis on funktsioonis aeg
    nupp.grid(column=4, row=rida, padx=5, pady=5)
    #print(b)

