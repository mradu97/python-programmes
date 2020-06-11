import tkinter as tk
import tkinter.messagebox as msg
top=tk.Tk()
def hello():
    msg.showinfo("hello python","hello world")

b=tk.Button(top,text="hello",command=hello)
b.pack()
top.mainloop()
