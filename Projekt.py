from tkinter import *
from lisa_to_do import do_do
#from ristike import unusta
#from time import *
from tkinter import colorchooser
from Homme import tomorrow
from Tulevikus import future
from Statistika import info

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


f = open("backg.gif")
#background_image=ImageTK.Photoimage("backg.gif")
#background_label = Tk.Label(parent, image=background_image)
#background_label.photo=background
#background_label.place(x=0, y=0, relwidth=1, relheight=1)
#bg = PhotoImage(file="backg.gif")
#img = raam.create_image(450, 80, image=bg)


#rea pealkiri
kiri = "Calibri"
rea_pealkiri = Label(raam, text="Tegevus:", font=kiri, background=colour)
rea_pealkiri.grid(column=0, row=0, padx=5, pady=5)

#tegevuse sisestamise kastikesed
tegevuse_sisestamine = Entry(raam, cursor="pencil", font=kiri,justify=CENTER)
tegevuse_sisestamine.grid(column=1, row=0, padx=10, pady=10)

#aja lisestamise kastike
rea_pealkiri = Label(raam, text="Aeg:", font=kiri, background=colour)
rea_pealkiri.grid(column=2, row=0, padx=5, pady=5)
aja_sisestamine = Entry(raam, cursor="pencil",font=kiri, justify=CENTER)
aja_sisestamine.grid(column=3, row=0, padx=10, pady=10)

nupp = Button(raam, cursor="hand2",text="  Lisa  ",font=kiri, bg="SkyBlue2", command=lambda: do_do(raam, colour, tegevuse_sisestamine, aja_sisestamine, kiri))
nupp.grid(column=4, row= 0, padx=5, pady=6)


# soovime, et akna suuruse muutmisel muudetakse veeru 1 ja rea 1 mõõtmeid
raam.columnconfigure(10, weight=10)
raam.rowconfigure(1, weight=10)

# kuvame akna ekraanile
raam.mainloop()