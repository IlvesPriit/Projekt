from tkinter import *
from tkinter import ttk
from time import time
from stopp_nupp import stopp
from stopp_nupp import aeg
from lisa_to_do import do_do
from time import *


def do_do(raam):
    var = IntVar()
    c = Checkbutton(raam, variable=var)
    c.grid(column=0, padx=5, pady=5)
    rida= c.grid_info()["row"]
    # tegevus = Label(raam, text="tegevus:")
    # tegevus.grid(column=1, row = rida, padx=5, pady=5)
    # aeg = Label(raam, text="aeg:")
    # aeg.grid(column=3, row = rida,  padx=5, pady=5)
    #võtame entry boxidest sisestatu
    tegevuse_sisestamine_tulemus = Label(raam, text=tegevuse_sisestamine.get())
    tegevuse_sisestamine_tulemus.grid(column=2, row = rida, padx=5, pady=5)
    aja_sisestamine_tulemus = Label(raam, text=aja_sisestamine.get())
    aja_sisestamine_tulemus.grid(column=3, row = rida,  padx=5, pady=5)
    
    # soovime, et nupp veniks nii laiuses kui ka kõrguses
    a = time()
    nupp = Button(raam, text="Start",bg="green", command=lambda : stopp(raam, rida))
    #sulgudesse vaja ka command = alustab aja lugemist, mis on funktsioonis aeg
    nupp.grid(column=4, row = rida,  padx=5, pady=6)
    # soovime, et nupp muutuks peale vajutust
    progress = ttk.Progressbar(raam, orient='horizontal', length= 75, mode = 'indeterminate')
    progress.grid(column=6, row=rida, padx=5, pady=5)

#võta see muutuja i ning lisa see õigetele ridadele, sest iga dodo peab olema ju uuel
raam = Tk()
raam.title("To Do")

f = open("backg.gif")
#background_image=ImageTK.Photoimage("backg.gif")
#background_label = Tk.Label(parent, image=background_image)
#background_label.photo=background
#background_label.place(x=0, y=0, relwidth=1, relheight=1)
#bg = PhotoImage(file="backg.gif")
#img = raam.create_image(450, 80, image=bg)

#rea pealkiri
rea_pealkiri = Label(raam, text="Tegevus")
rea_pealkiri.grid(column=0, row=0, padx=5, pady=5)
#sisestamise kastikesed
tegevuse_sisestamine = Entry(raam)
tegevuse_sisestamine.grid(column=2, row=0, padx=10, pady=10)
aja_sisestamine = Entry(raam)
aja_sisestamine.grid(column=3, row=0, padx=10, pady=10)

nupp = Button(raam, text=" Lisa ",bg="blue", command=lambda: do_do(raam))
#sulgudesse vaja ka command = alustab aja lugemist, mis on funktsioonis aeg
nupp.grid(column=4, row= 0, padx=5, pady=6)
#see junn tuleks panna tsüklisse
#do_do()


# soovime, et akna suuruse muutmisel muudetakse veeru 1 ja rea 1 mõõtmeid
# (st. veerg 0 ja rida 0 jäävad sama laiaks/kõrgeks)
raam.columnconfigure(10, weight=10)
raam.rowconfigure(1, weight=10)

#menüü
def Uus_fail():
    print("mingi asi!")
def Uus_fail2():
    print("menüü commandi näidis")

menu = Menu(raam)
raam.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Homme", menu=filemenu)
#see lisab sinna menüü alla mingeid vidinaid
#filemenu.add_command(label="Tulevikus", command=NewFile)
menu.add_cascade(label="Tulevikus", menu=filemenu)
menu.add_cascade(label="Arhiiv", menu=filemenu)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=raam.quit)
# kuvame akna ekraanile
raam.mainloop()
