#risti nupu funktsioonid

def unusta(timer,c,tegevuse_sisestamine_tulemus,aja_sisestamine_tulemus,nupp,progress,ristike):
    c.grid_forget()
    tegevuse_sisestamine_tulemus.grid_forget()
    aja_sisestamine_tulemus.grid_forget()
    nupp.grid_forget()
    progress.grid_forget()
    ristike.grid_forget()
    timer.grid_forget()
    nupp.grid_forget()
    nupp.grid_forget()
    #start_nupp.grid_forget()
    #stopp_nupp.grid_forget()

def unusta_homne(timer, c, tegevuse_sisestamine_tulemus, ristike):
    c.grid_forget()
    tegevuse_sisestamine_tulemus.grid_forget()
    timer.grid_forget()
    ristike.grid_forget()
