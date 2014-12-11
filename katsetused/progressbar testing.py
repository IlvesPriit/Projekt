
import tkinter as Tkinter
import tkinter.ttk as ttk
 
 
def bar():
 
  root = Tkinter.Tk()
 
  ft = ttk.Frame()

 
  ft.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)

 
  pb_hd = ttk.Progressbar(ft, orient='horizontal', mode='indeterminate')
  pb_hd.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)
 
  pb_hd.start(1200)

  root.mainloop()
def stop():
    pb_hd.stop(1200)
bar()
stop()
