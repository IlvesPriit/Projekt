from tkinter import *
from tkinter import ttk
from stopp_nupp import stardinupp
from stopp_nupp import stopp
from ristike import unusta


#funktsioon üheks linnukesega tegevuse reaks
#see värk peaks käivituma iga kord kui vajutada nuppu 'lisa'
def do_do(raam, colour, tegevuse_sisestamine, aja_sisestamine, kiri):
    var = IntVar()
    c = Checkbutton(raam, activebackground=colour,background=colour, variable=var)
    c.grid(column=0, padx=5, pady=5)

    rida= c.grid_info()["row"]
    #võtame entry boxidest sisestatu
    tegevuse_sisestamine_tulemus = Label(raam, text=tegevuse_sisestamine.get(), background=colour, font=kiri)
    tegevuse_sisestamine_tulemus.grid(column=1, row = rida, padx=5, pady=5)

    aja_sisestamine_tulemus = Label(raam, text="Ennustus = "+ aja_sisestamine.get(), background=colour, font=kiri)
    aja_sisestamine_tulemus.grid(column=2, row = rida,  padx=5, pady=5)

    #see timeri asi
    global olek
    olek = False
    global timer
    timer = [0, 0, 0]
    global pattern
    pattern = '{0:02d}:{1:02d}:{2:02d}'
    #global clock
    clock = Label(raam, text="00:00:00", background=colour, font=kiri)
    clock.grid(column=3, row = rida,  padx=5, pady=6)

    # soovime, et nupp veniks nii laiuses kui ka kõrguses
    nupp = Button(raam,cursor="hand2", text=" Start ",font=kiri, bg="lime green", command=lambda : stopp(raam, rida, kiri))
    #sulgudesse vaja ka command = alustab aja lugemist, mis on funktsioonis aeg
    nupp.grid(column=4, row = rida,  padx=5, pady=6)

    # soovime, et nupp muutuks peale vajutust
    progress = ttk.Progressbar(raam, orient='horizontal', length= 75, mode = 'indeterminate')
    progress.grid(column=5, row=rida, padx=5, pady=5)


    # #nupp, et soovimatud to_do-d kustutada
    ristike = Button(raam, text=" X ",bg="MediumVioletRed", command=lambda: unusta(clock,c, tegevuse_sisestamine_tulemus,aja_sisestamine_tulemus, nupp, progress, ristike))
    ristike.grid(column=6, row=rida, padx=5, pady=5)


