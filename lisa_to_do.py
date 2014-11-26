from tkinter import *
from tkinter import ttk
from time import *

from stopp_nupp import stopp

#funktsioon üheks linnukesega tegevuse reaks
#see värk peaks käivituma iga kord kui vajutada nuppu 'lisa'
def do_do(raam, colour, font):
    var = IntVar()
    c = Checkbutton(raam, variable=var)
    c.grid(column=0, padx=5, pady=5)
    rida= c.grid_info()["row"]
    tegevus = ttk.Label(raam, text="tegevus", font=font)
    tegevus.grid(column=2, row = rida, padx=5, pady=5)
    tegevus.configure(background=colour)
    aeg = ttk.Label(raam, text="aeg", font=font)
    aeg.grid(column=3, row = rida,  padx=5, pady=5)
    aeg.configure(background=colour)
    # soovime, et nupp veniks nii laiuses kui ka kõrguses
    a = time()
    nupp = ttk.Button(raam, text="Start", command=lambda : stopp(raam, rida))
    #sulgudesse vaja ka command = alustab aja lugemist, mis on funktsioonis aeg
    nupp.grid(column=4, row = rida,  padx=5, pady=6)
    # soovime, et nupp muutuks peale vajutust
    progress = ttk.Progressbar(raam, orient='horizontal', length= 100, mode = 'indeterminate')
    progress.grid(column=5, row=rida, padx=5, pady=5)
    progress.configure(background=colour)

