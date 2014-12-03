ajad= ["00:20:30", "00:30:50", "01:40:00"]
ajad_minutites = []
for aeg in ajad:
    jarjend = aeg.split(":")
    loppjarjend= []
    for i in jarjend:
        loppjarjend +=[int(i)]
    print(loppjarjend)

    #aja_string = muster.format(timer[0], timer[1], timer[2])
    summa = loppjarjend[0]*60 + loppjarjend[1] + loppjarjend[2]%60
    ajad_minutites.append(summa)
print(ajad_minutites)