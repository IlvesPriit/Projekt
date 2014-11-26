from tkinter import *

#risti nupu funktsioonid

def unusta(c, tegevuse_sisestamine_tulemus,aja_sisestamine_tulemus, nupp, progress, ristike):
    c.pack()
    #tegevuse_sisestamine_tulemus.grid_remove()
    tegevuse_sisestamine_tulemus.pack_forget()
    #aja_sisestamine_tulemus.grid_remove()
    aja_sisestamine_tulemus.pack_forget()
    #nupp.grid_remove()
    nupp.pack_forget()
    #progress.grid_remove()
    progress.pack_forget()
    #ristike.grid_remove()
    ristike.pack_forget()
    #ristike.pack_forget()
