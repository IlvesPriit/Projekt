from tkinter import *
from time import *

#kogu see statistika nd stuff
def info(colour, ajad, tegevused, ennustatud_ajad):
    info_aken = Tk()
    info_aken.title("Statistika")
    info_aken.configure(background=colour)

    #skrollbar


    #rea pealkiri
    kiri = "Calibri"
    rea_pealkiri = Label(info_aken, text= ctime(), font=kiri, background=colour)
    rea_pealkiri.grid(column=0, row=0, padx=5, pady=5)

    ajad_minutites = []
    for aeg in ajad:
        jarjend = aeg.split(":")
        loppjarjend= []
        for i in jarjend:
            loppjarjend +=[int(i)]
        print(loppjarjend)
        summa = loppjarjend[0]*60 + loppjarjend[1] + round(loppjarjend[2]/60)
        ajad_minutites.append(summa)
    minutite_summa=sum(ajad_minutites)
    tunnid_kokku = minutite_summa // 60
    minutid_kokku = minutite_summa % 60

    teisendatud_ennustus = []
    for ennustus in ennustatud_ajad:
        jarjend = ennustus.split(":")
        loppjarjend = []
        for osa in jarjend:
            print(osa)
            loppjarjend.append(int(osa))
        summa = loppjarjend[0]*60 + loppjarjend[1] + round(loppjarjend[2]/60)
        teisendatud_ennustus.append(summa)
    ennustatud_min_sum =sum(teisendatud_ennustus)
    ennustatud_h = ennustatud_min_sum // 60
    ennustatud_min_kokku = ennustatud_min_sum % 60


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
    planeeritud = Label(info_aken, text="Planeeritud aeg: " + str(tunnid_kokku) + "h " + str(minutid_kokku) + "min", font=kiri, background=colour)
    planeeritud.grid(column=0, row=asukoht+1, padx=5, pady=5)

    tegelik = Label(info_aken, text="Tegelik aeg: " + str(ennustatud_h) + "h " + str(ennustatud_min_kokku) + "min", font=kiri, background=colour)
    tegelik.grid(column=0, row=asukoht+2, padx=5, pady=5)

    info_aken.mainloop()