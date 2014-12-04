from tkinter import *
from time import *

#kogu see statistika nd stuff
def info(colour, ajad, tegevused):
    info_aken = Tk()
    info_aken.title("Statistika")
    info_aken.configure(background=colour)

    #skrollbar


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
    tunnid_kokku = minutite_summa // 60
    minutid_kokku = minutite_summa % 60

    varvid = ["chartreuse3", "pink", "blue4", "DeepPink4", "purple1",
              "IndianRed1", "magenta", "SeaGreen2", "violet",
              "brown2", "gray45", "blue", "green3", "firebrick1",
              "VioletRed1", "sienna1", "MediumPurple3", "cyan3",
              "OliveDrab1", "VioletRed4", "orchid1", "yellow2"]

    #tegevused + ajad tuleb välja kirjutada igale reale
    asukoht = 1
    for i in range(len(tegevused)):
        tegevus = Label(info_aken, text=tegevused[i], font=kiri, background=colour)
        tegevus.grid(column=0, row=asukoht, padx=5, pady=5)
        aeg = Label(info_aken, text= ajad[i], font=kiri, background=colour)
        aeg.grid(column=1, row=asukoht, padx=5, pady=5)
        varvi_marge = Label(info_aken, text="   ", bg = varvid[i])
        varvi_marge.grid(column=2, row=asukoht, padx=5, pady=5)
        asukoht += 1

     #teeme ühe graafiku
    sektor_diagramm = Canvas(info_aken, bg="white", width=200, height=200)
    sektor_diagramm.grid(column=1, row=asukoht + 1, padx=5, pady=6)
    coord = 190, 190, 10, 10

    alguspunkt = 0
    for i in range(len(ajad_minutites)):
        lopppunkt = round(360/minutite_summa*ajad_minutites[i])
        sektor_diagramm.create_arc(coord, start=alguspunkt, extent=lopppunkt, fill=varvid[i], activefill="gray50", outline="white", tag=tegevused[i])
        alguspunkt = alguspunkt + lopppunkt

    #tagasiside
    tagasiside = Label(info_aken, text="Aega kulus kokku: " + str(tunnid_kokku) + "h " + str(minutid_kokku) + "min", font=kiri, background=colour)
    tagasiside.grid(column=0, row=asukoht+1, padx=5, pady=5)
    info_aken.mainloop()