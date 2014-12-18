# coding=utf-8
from tkinter import *
from tkinter import colorchooser
from Homme import tomorrow
from Tulevikus import future
from Statistika import info
from lisa_to_do import do_do
from lisa_to_do import n
from taastamine import taasta
#tekitame raami
raam = Tk()
raam.title("To Do")
raam.configure(background="white")

#teeme menüü
menu = Menu(raam)
menu = Menu(menu,tearoff=0)
raam.config(menu=menu)

def sulge():
    salvestaAndmebaas()
    raam.destroy()

#aegade jaoks järjend
ajad = []
tegevused = []
ennustatud_ajad = []
def salvestaAndmebaas():
    fail = open('andmebaas.csv','w')
    fail.write("n;tegevuse_sisestamine_tulemus;aja_sisestamine;lõppjärjend\n")
    if ajad ==[] :
        fail.close()
    else:
        for i in range (len(ajad)):
            fail.write(str(i+1)+";"+tegevused[i]+";"+ennustatud_ajad[i]+";"+ajad[i]+"\n")
        fail.close()

def LaeAndmebaas():
    fail = open('andmebaas.csv','r')
    for i in fail:
        if i == "n;tegevuse_sisestamine_tulemus;aja_sisestamine;lõppjärjend\n":
            continue
        järjend= i.split(";")
        n = järjend[0]
        ajad=järjend[3]
        tegevused=järjend[1]
        ennustatud_ajad=järjend[2]
        taasta(raam, colour, n, kiri, ajad, tegevused, ennustatud_ajad)
#menu.add_cascade(label="Homme", command=lambda: tomorrow(colour))
#see lisab sinna menüü alla mingeid vidinaid
#menu.add_cascade(label="Tulevikus", command=lambda: future(colour, ajad, tegevused, ennustatud_ajad))
menu.add_command(label="Sulge", command=sulge)
menu.add_command(label="Salvesta", command=salvestaAndmebaas)
menu.add_command(label="Lae", command=LaeAndmebaas)
#menu.add_cascade(label="Salvesta", command=lambda: future(colour, ajad, tegevused, ennustatud_ajad))
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
