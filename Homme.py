from tkinter import *
from tomorrow_to_do import do_tomorrow


#avaneb siis kui vajutada menüüs "homme"
#tekitame raami
def tomorrow(colour):
    homme = Tk()
    homme.title("To Do Tomorrow")
    homme.configure(background=colour)
    #rea pealkiri
    kiri = "Calibri"
    rea_pealkiri = Label(homme, text="Tegevus:", font=kiri, background=colour)
    rea_pealkiri.grid(column=0, row=0, padx=5, pady=5)
    
    #tegevuse sisestamise kastikesed
    tegevuse_sisestamine = Entry(homme, cursor="pencil", font=kiri,justify=CENTER)
    tegevuse_sisestamine.grid(column=1, row=0, padx=10, pady=10)
    
    #aja lisestamise kastike
    rea_pealkiri = Label(homme, text="Aeg:", font=kiri, background=colour)
    rea_pealkiri.grid(column=2, row=0, padx=5, pady=5)
    aja_sisestamine = Entry(homme, cursor="pencil",font=kiri, justify=CENTER)
    aja_sisestamine.grid(column=3, row=0, padx=10, pady=10)
    
    nupp = Button(homme, cursor="hand2",text="  Lisa  ",font=kiri, bg="SkyBlue2", command=lambda: do_tomorrow(homme, colour, tegevuse_sisestamine, aja_sisestamine, kiri))
    nupp.grid(column=4, row= 0, padx=5, pady=6)
    
    # soovime, et akna suuruse muutmisel muudetakse veeru 1 ja rea 1 mõõtmeid
    homme.mainloop()