from tkinter import *
from tkinter import ttk
from stopp_nupp import stopp
#from stopp_nupp import start
#from stopp_nupp import aeg
#from lisa_to_do import do_do
#from ristike import unusta
from time import *


def do_do(raam):
    var = IntVar()
    c = Checkbutton(raam, variable=var)
    c.grid(column=0, padx=5, pady=5)
    c.configure(background=colour)

    rida= c.grid_info()["row"]
    #võtame entry boxidest sisestatu
    tegevuse_sisestamine_tulemus = Label(raam, text=tegevuse_sisestamine.get())
    tegevuse_sisestamine_tulemus.grid(column=2, row = rida, padx=5, pady=5)
    tegevuse_sisestamine_tulemus.configure(background=colour)

    aja_sisestamine_tulemus = Label(raam, text=aja_sisestamine.get())
    aja_sisestamine_tulemus.grid(column=3, row = rida,  padx=5, pady=5)
    aja_sisestamine_tulemus.configure(background=colour)

    
    # soovime, et nupp veniks nii laiuses kui ka kõrguses
    a = time()
    nupp = Button(raam,cursor="hand2", text=" Start ",bg="lime green", command=lambda : stopp(raam, rida))
    #sulgudesse vaja ka command = alustab aja lugemist, mis on funktsioonis aeg
    nupp.grid(column=4, row = rida,  padx=5, pady=6)

    # soovime, et nupp muutuks peale vajutust
    progress = ttk.Progressbar(raam, orient='horizontal', length= 75, mode = 'indeterminate')
    progress.grid(column=6, row=rida, padx=5, pady=5)


    #nupp, et soovimatud to_do-d kustutada
    #ristike = Button(raam, text=" X ",bg="white", command=lambda: unusta(c, tegevuse_sisestamine_tulemus,aja_sisestamine_tulemus, nupp, progress, ristike))
    #ristike.grid(column=7, row=rida, padx=5, pady=5)
    #ristike.pack()


#võta see muutuja i ning lisa see õigetele ridadele, sest iga dodo peab olema ju uuel
raam = Tk()
raam.title("To Do")
colour = 'SkyBlue1'
raam.configure(background=colour)

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
rea_pealkiri.configure(background=colour)
#sisestamise kastikesed
tegevuse_sisestamine = Entry(raam, cursor="pencil")
tegevuse_sisestamine.grid(column=2, row=0, padx=10, pady=10)

aja_sisestamine = Entry(raam, cursor="pencil")
aja_sisestamine.grid(column=3, row=0, padx=10, pady=10)

nupp = Button(raam, cursor="hand2",text=" Lisa ",bg="SkyBlue2", command=lambda: do_do(raam))
#sulgudesse vaja ka command = alustab aja lugemist, mis on funktsioonis aeg
nupp.grid(column=4, row= 0, padx=5, pady=6)

#teen selle et värvi saaks valida
#menüü buttoni moodi asi
akna_colour = ttk.Menubutton(raam, cursor="hand2", text="Värv")
akna_colour.grid(column=6, row= 0, padx=5, pady=5)
akna_colour.menu= Menu(akna_colour, tearoff=0)
akna_colour['menu'] = akna_colour.menu

akna_colour.mayoVar  = IntVar()
akna_colour.ketchVar = IntVar()
akna_colour.menu.add_checkbutton(label='   ', background ="medium orchid", variable=akna_colour.mayoVar)
akna_colour.menu.add_checkbutton(label='   ', background="blue",variable=akna_colour.ketchVar)
akna_colour.menu.add_checkbutton(label='   ', background="pink",variable=akna_colour.ketchVar)
akna_colour.menu.add_checkbutton(label='   ', background="white",variable=akna_colour.ketchVar)
akna_colour.menu.add_checkbutton(label='   ', background="green yellow",variable=akna_colour.ketchVar)
akna_colour.menu.add_checkbutton(label='   ', background="deep sky blue",variable=akna_colour.ketchVar)
akna_colour.menu.add_checkbutton(label='   ', background="IndianRed1",variable=akna_colour.ketchVar)



#akna_colour.add_command(label="Tulevikus", command=donothing)
#akna_colour.add_command(label="Tulevikus", command=donothing)



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
menu.add_cascade(label="Homme",menu=filemenu)
#see lisab sinna menüü alla mingeid vidinaid
#filemenu.add_command(label="Tulevikus", command=NewFile)
menu.add_cascade(label="Tulevikus", menu=filemenu)
menu.add_cascade(label="Arhiiv", menu=filemenu)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=raam.quit)
# kuvame akna ekraanile
raam.mainloop()
