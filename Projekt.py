from tkinter import *
from tkinter import colorchooser
from Homme import tomorrow
from Tulevikus import future
from Statistika import info
from lisa_to_do import do_do

#tekitame raami
raam = Tk()
raam.title("To Do")

menu = Menu(raam)
raam.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Homme", command=lambda: tomorrow(colour))
#see lisab sinna menüü alla mingeid vidinaid
menu.add_cascade(label="Tulevikus", command=lambda: future(colour))
menu.add_cascade(label="Statistika", command=lambda: info(colour))

#kujunduse värvide kompott
def värv():
    color = colorchooser.askcolor()
    color_name = color[1]
    raam.configure(background=color_name)
    global colour
    colour = color_name
    print(colour)

colour = "white"
kujundus = Menu(menu)
menu.add_cascade(label="Kujundus", menu=kujundus)
kujundus.add_command(label='Värv', command=värv)

#kujunduse fontide kompott
#def fondi_valik():

kujundus.add_command(label='Font', command=värv)
filemenu.add_command(label="Exit", command=raam.quit)


#rea pealkiri
kiri = "Calibri"
rea_pealkiri = Label(raam, text="Tegevus:", font=kiri, background=colour)
rea_pealkiri.grid(column=0, row=0, padx=5, pady=5)

#tegevuse sisestamise kastikesed
tegevuse_sisestamine = Entry(raam, cursor="pencil", font=kiri,justify=CENTER)
tegevuse_sisestamine.grid(column=1, row=0, padx=10, pady=10)

#aja lisestamise kastike
rea_pealkiri = Label(raam, text="Aeg(00:00:00):", font=kiri, background=colour)
rea_pealkiri.grid(column=2, row=0, padx=5, pady=5)
aja_sisestamine = Entry(raam, cursor="pencil",font=kiri, justify=CENTER)
aja_sisestamine.grid(column=3, row=0, padx=10, pady=10)


nupp = Button(raam, cursor="hand2",text="  Lisa  ",font=kiri, bg="SkyBlue2", command=lambda: do_do(raam, colour, tegevuse_sisestamine, aja_sisestamine, kiri))
nupp.grid(column=4, row= 0, padx=5, pady=6)


#viimasel real on nupp "salvesta"
salvestan = Button(raam, cursor="hand2", text=" Salvesta ",font=kiri, bg="RoyalBlue2" )
salvestan.grid(column=5, row=0, padx=5, pady=6)

# soovime, et akna suuruse muutmisel muudetakse veeru 1 ja rea 1 mõõtmeid
raam.columnconfigure(10, weight=10)
raam.rowconfigure(1, weight=10)

# kuvame akna ekraanile
raam.mainloop()