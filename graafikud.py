from tkinter import *

info_aken = Tk()
info_aken.title("Statistika")
info_aken.configure(background="white")
tegevus="tegevus"
sektor_diagramm = Canvas(info_aken, bg="white", width=400, height=400)
sektor_diagramm.grid(column=3, row=3, padx=5, pady=6)
coord = 360, 360, 10, 10
osa = sektor_diagramm.create_arc(coord, start=0, extent=180, fill="purple", activefill="blue", outline="purple", tags=tegevus)
sektor_diagramm.create_arc(coord, start=180, extent=90, fill="pink", activefill="blue", outline="pink")

# soovime, et akna suuruse muutmisel muudetakse veeru 1 ja rea 1 mõõtmeid
info_aken.columnconfigure(10, weight=10)
info_aken.rowconfigure(1, weight=10)
info_aken.mainloop()