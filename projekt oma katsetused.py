from tkinter import *


root = Tk()
root.title("Pack is BEST!!!")

l = Label(root, text="todo")
l.pack()


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