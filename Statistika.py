from tkinter import *
from time import *

#kogu see statistika nd stuff
def info(colour, ajad):
    info_aken = Tk()
    info_aken.title("Statistika")
    info_aken.configure(background=colour)

    #rea pealkiri
    kiri = "Calibri"
    rea_pealkiri = Label(info_aken, text= ctime(), font=kiri, background=colour)
    rea_pealkiri.grid(column=0, row=0, padx=5, pady=5)

    ## Need on need 2 muutujat, mis oleks vaja nt csv failist statistikasse toimetada (kõik tegvused ja nendele kulunud aeg!)
    # tegevuse_sisestamine
    # aja_sisestamine
    #ajad= ["00:20:30", "00:30:50", "01:40:00"]
    ajad_minutites = []
    for aeg in ajad:
        jarjend = aeg.split(":")
        loppjarjend= []
        for i in jarjend:
            loppjarjend +=[int(i)]
        print(loppjarjend)

        #aja_string = muster.format(timer[0], timer[1], timer[2])
        summa = loppjarjend[0]*60 + loppjarjend[1] + round(loppjarjend[2]/60)
        ajad_minutites.append(summa)
    minutite_summa=sum(ajad_minutites)
    print(ajad_minutites)
    print(minutite_summa)

    #teeme ühe graafiku
    sektor_diagramm = Canvas(info_aken, bg="white", width=400, height=400)
    sektor_diagramm.grid(column=3, row=3, padx=5, pady=6)
    coord = 390, 390, 10, 10
    varvid = ["chartreuse3", "pink", "blue4", "DeepPink4", "purple1",
              "IndianRed1", "magenta", "SeaGreen2", "violet",
              "brown2", "gray45", "blue", "green3", "firebrick1",
              "VioletRed1", "sienna1", "MediumPurple3", "cyan3",
              "OliveDrab1", "VioletRed4", "orchid1", "yellow2"]
    alguspunkt = 0
    for i in range(len(ajad_minutites)):
        lopppunkt = round(360/minutite_summa*ajad_minutites[i])
        sektor_diagramm.create_arc(coord, start=alguspunkt, extent=lopppunkt, fill=varvid[i], activefill="blue", outline="white")
        alguspunkt = alguspunkt + lopppunkt
    # soovime, et akna suuruse muutmisel muudetakse veeru 1 ja rea 1 mõõtmeid
    info_aken.columnconfigure(10, weight=10)
    info_aken.rowconfigure(1, weight=10)
    info_aken.mainloop()