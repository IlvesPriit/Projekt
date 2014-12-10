# coding=utf-8
from tkinter import *
from tkinter import colorchooser
from Homme import tomorrow
from Tulevikus import future
from Statistika import info
from lisa_to_do import do_do

#tekitame raami
raam = Tk()
raam.title("To Do")
raam.configure(background="white")

#teeme menüü
menu = Menu(raam)
raam.config(menu=menu)
menu.add_cascade(label="Homme", command=lambda: tomorrow(colour))
#see lisab sinna menüü alla mingeid vidinaid
menu.add_cascade(label="Tulevikus", command=lambda: future(colour, ajad, tegevused, ennustatud_ajad))
menu.add_cascade(label="Statistika", command=lambda: info(colour, ajad, tegevused, ennustatud_ajad))

#kujunduse värvide kompott
def värv():
    color = colorchooser.askcolor()
    color_name = color[1]
    raam.configure(background=color_name)
    global colour
    colour = color_name
    print(colour)


colour = "white"
menu.add_cascade(label="Raami värv", command=värv)

#rea pealkiri
kiri = "Purisa"
rea_pealkiri = Label(raam, text="Tegevus:", font=kiri, background="white")
rea_pealkiri.grid(column=0, row=0, padx=5, pady=5)


#tegevuse sisestamise kastikesed
tegevuse_sisestamine = Entry(raam, cursor="pencil", font=kiri,justify=CENTER)
tegevuse_sisestamine.grid(column=1, row=0, padx=10, pady=10)


#aja lisestamise kastike
rea_pealkiri = Label(raam, text="Aeg(00:00:00):", font=kiri, background="white")
rea_pealkiri.grid(column=2, row=0, padx=5, pady=5)
aja_sisestamine = Entry(raam, cursor="pencil",font=kiri, justify=CENTER)
aja_sisestamine.grid(column=3, row=0, padx=10, pady=10)


nupp =Button(raam, cursor="hand2", text="  Lisa  ",
              font=kiri, bg="SkyBlue2",
              command=lambda: do_do(raam, colour,
                                    tegevuse_sisestamine,
                                    aja_sisestamine,
                                    kiri, ajad, tegevused, ennustatud_ajad))
nupp.grid(column=4, row= 0, padx=5, pady=6)

# #salvestamine faili
# class salvestan_tegevused:
#     def __init__(self):
#         self._aeg = aja_sisestamine.get()
#
#     def getCSV(self):
#         return str(self._aeg)
#
#     def __str__(self):
#         return "[Aeg:" + self._aeg + "]"
#
#     def salvestati(failinimi):
#         f = open(failinimi, "w")
#         f.write(ajad.getCSV() + "\n")
#
#     def laadi(failinimi):
#         f = open(failinimi)
#         for rida in f:
#             ajad.append(rida)

#aegade jaoks järjend
ajad = []
tegevused = []
ennustatud_ajad = []
# failinimi = "todo.txt"
# #viimasel real on nupp "salvesta"
# salvestan = Button(raam, cursor="hand2",
#                    text=" Salvesta ",font=kiri,
#                    bg="RoyalBlue2", command = salvestan_tegevused)
# salvestan.grid(column=5, row=0, padx=5, pady=6)


# kuvame akna ekraanile
raam.mainloop()
