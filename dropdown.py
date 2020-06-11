from tkinter import *
from tkinter import ttk

win = Tk()
def show():
    mll = Label(win, text=var.get()).pack()

def comboclick(event):
    mll = Label(win, text = cmb.get()).pack()

opt = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]

var = StringVar()
var.set(opt[0])

drop = OptionMenu(win, var, *opt)
drop.pack()

cmb = ttk.Combobox(win, value=opt)
cmb.current(0)
cmb.bind("<<ComboboxSelected>>", comboclick)
cmb.pack()

mbt = Button(win, text = "Show Selection", command = show).pack()

win.mainloop()
