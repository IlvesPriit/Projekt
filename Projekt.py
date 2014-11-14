
from tkinter import *
from tkinter import ttk
from time import *
from stopp_nupp import stopp
from lisa_to_do import lisa


def do_do():
    var = IntVar()
    c = Checkbutton(raam, variable=var)
    c.grid(column=0, row=2, padx=5, pady=5)

    tegevus = ttk.Label(raam, text="tegevus")
    tegevus.grid(column=2, row=2, padx=5, pady=5)

    aeg = ttk.Label(raam, text="aeg")
    aeg.grid(column=3, row=2, padx=5, pady=5)

    # soovime, et nupp veniks nii laiuses kui ka kõrguses
    a = time()
    nupp = ttk.Button(raam, text="Start", command=lambda : stopp(raam))
    #sulgudesse vaja ka command = alustab aja lugemist, mis on funktsioonis aeg
    nupp.grid(column=4, row=2, padx=5, pady=5)

    # soovime, et akna suuruse muutmisel muudetakse veeru 1 ja rea 1 mõõtmeid
    # (st. veerg 0 ja rida 0 jäävad sama laiaks/kõrgeks)
    raam.columnconfigure(10, weight=10)
    raam.rowconfigure(1, weight=10)

    # kuvame akna ekraanile
    raam.mainloop()

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
nupp = ttk.Button(raam, text="Lisa", command=lisa)
#sulgudesse vaja ka command = alustab aja lugemist, mis on funktsioonis aeg
nupp.grid(column=4, row= 0, padx=5, pady=5)
#see junn tuleks panna tsüklisse
a=time()
do_do()
print(round(a/3600, 3),"asiiii")
