from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Pack is BEST!!!")

l = Label(root, text="todo")
l.pack()


color = colorchooser.askcolor()
color_name = color[1]    #to pick up the color name in HTML notation, i.e. the 2nd element of the tuple returned by the colorchooser
root.configure(background=color_name)

def forget():
    d.pack_forget()
def unusta():
    b.pack_forget()

def remember():
      l.pack()


b = Button(root, text=" X ", command=unusta)
b.pack()
# b = Button(root, text="Wait, I still need you", command=remember)
# b.pack()
d = Button(root, text="Wait, I still need you", command=forget)
d.pack()

root.mainloop()