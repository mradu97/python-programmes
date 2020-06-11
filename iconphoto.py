import tkinter as tk
import sys
from tkinter import *
from tkinter.ttk import *

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self._geom='200*200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() -pad, master.winfo_screenheight() -pad))
        master.bind('<Escape>',self.toggle_geom)

    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom.self._geom)
        self.master.geometry(self.geom)
        self._geom=geom

root=tk.Tk()

photo = PhotoImage(file ='D:/PythonProg/6-2-tree-free-png-image.png')
root.iconphoto(False,photo)

app=FullScreenApp(root)
root.mainloop()
