from tkinter import *
from lisa_to_do import do_do
from tkinter import ttk
#avaneb siis kui vajutada menüüs "homme"
#tekitame raami
def future(colour, ajad, tegevused):
    tulevikus = Tk()
    tulevikus.title("To Do Tomorrow")
    tulevikus.configure(background=colour)
    #rea pealkiri
    kiri = "Calibri"
    rea_pealkiri = Label(tulevikus, text="Tegevus:", font=kiri, background=colour)
    rea_pealkiri.grid(column=0, row=0, padx=5, pady=5)

    #tegevuse sisestamise kastikesed
    tegevuse_sisestamine = Entry(tulevikus, cursor="pencil", font=kiri,justify=CENTER)
    tegevuse_sisestamine.grid(column=1, row=0, padx=10, pady=10)

    #aja lisestamise kastike
    rea_pealkiri = Label(tulevikus, text="Aeg:", font=kiri, background=colour)
    rea_pealkiri.grid(column=2, row=0, padx=5, pady=5)
    aja_sisestamine = Entry(tulevikus, cursor="pencil",font=kiri, justify=CENTER)
    aja_sisestamine.grid(column=3, row=0, padx=10, pady=10)

    nupp = Button(tulevikus, cursor="hand2",text="  Lisa  ",
                  font=kiri, bg="SkyBlue2",
                  command=lambda: do_do(tulevikus, colour, tegevuse_sisestamine, aja_sisestamine, kiri, ajad, tegevused))
    nupp.grid(column=4, row= 0, padx=5, pady=6)

    tulevikus.mainloop()
