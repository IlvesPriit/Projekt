from tkinter import *
from tkinter import ttk
from stopp_nupp import stopp
from ristike import unusta
from ristike import unusta_homne

#homsed tegevused, nende jaoks veidi teistsugune formaat. Seal ju pole vaja start ja stopp
def do_tomorrow(raam, colour, tegevuse_sisestamine, aja_sisestamine, kiri):
    var = IntVar()
    c = Checkbutton(raam, activebackground=colour,background=colour, variable=var)
    c.grid(column=0, padx=5, pady=5)

    rida= c.grid_info()["row"]
    #võtame entry boxidest sisestatu
    tegevuse_sisestamine_tulemus = Label(raam, text=tegevuse_sisestamine.get(), background=colour, font=kiri)
    tegevuse_sisestamine_tulemus.grid(column=1, row = rida, padx=5, pady=5)

    clock = Label(raam, text=aja_sisestamine.get(), background=colour, font=kiri)
    clock.grid(column=3, row = rida,  padx=5, pady=6)

    # #nupp, et soovimatud to_do-d kustutada
    ristike = Button(raam, text=" X ",bg="MediumVioletRed",
                     command=lambda: unusta_homne(clock, c, tegevuse_sisestamine_tulemus, ristike))
    ristike.grid(column=4, row=rida, padx=5, pady=5)

