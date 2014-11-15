from tkinter import *
from tkinter import ttk
from time import *
from stopp_nupp import stopp
from stopp_nupp import aeg
from lisa_to_do import do_do

#võta see muutuja i ning lisa see õigetele ridadele, sest iga dodo peab olema ju uuel
raam = Tk()
raam.title("To Do")
#rea pealkiri
rea_pealkiri = ttk.Label(raam, text="Tegevus")
rea_pealkiri.grid(column=0, row=0, padx=5, pady=5)
#sisestamise kastikesed
tegevuse_sisestamine = ttk.Entry(raam)
tegevuse_sisestamine.grid(column=2, row=0, padx=10, pady=10)
aja_sisestamine = ttk.Entry(raam)
aja_sisestamine.grid(column=3, row=0, padx=10, pady=10)

nupp = ttk.Button(raam, text="Lisa", command=lambda: do_do(raam))
#sulgudesse vaja ka command = alustab aja lugemist, mis on funktsioonis aeg
nupp.grid(column=4, row= 0, padx=5, pady=5)
#see junn tuleks panna tsüklisse
#do_do()


# soovime, et akna suuruse muutmisel muudetakse veeru 1 ja rea 1 mõõtmeid
# (st. veerg 0 ja rida 0 jäävad sama laiaks/kõrgeks)
raam.columnconfigure(10, weight=10)
raam.rowconfigure(1, weight=10)

# kuvame akna ekraanile
raam.mainloop()
