from tkinter import *
from time import *
import time
#kogu see statistika nd stuff
def info(colour):
    info_aken = Tk()
    info_aken.title("Statistika")
    info_aken.configure(background=colour)

    localtime = time.localtime(time.time())
    juba_struktureeritud = ctime()
    #rea pealkiri
    kiri = "Calibri"
    rea_pealkiri = Label(info_aken, text= juba_struktureeritud, font=kiri, background=colour)
    rea_pealkiri.grid(column=0, row=0, padx=5, pady=5)
    #
    # #tegevuse sisestamise kastikesed
    # tegevuse_sisestamine = Entry(tulevikus, cursor="pencil", font=kiri,justify=CENTER)
    # tegevuse_sisestamine.grid(column=1, row=0, padx=10, pady=10)
    #
    # #aja lisestamise kastike
    # rea_pealkiri = Label(tulevikus, text="Aeg:", font=kiri, background=colour)
    # rea_pealkiri.grid(column=2, row=0, padx=5, pady=5)
    # aja_sisestamine = Entry(tulevikus, cursor="pencil",font=kiri, justify=CENTER)
    # aja_sisestamine.grid(column=3, row=0, padx=10, pady=10)
    #
    # nupp = Button(tulevikus, cursor="hand2",text="  Lisa  ",font=kiri, bg="SkyBlue2", command=lambda: do_do(tulevikus, colour, tegevuse_sisestamine, aja_sisestamine, kiri))
    # nupp.grid(column=4, row= 0, padx=5, pady=6)

    # soovime, et akna suuruse muutmisel muudetakse veeru 1 ja rea 1 mõõtmeid
    info_aken.columnconfigure(10, weight=10)
    info_aken.rowconfigure(1, weight=10)
    info_aken.mainloop()