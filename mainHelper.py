import sys
import os
import Tkinter 
import tkMessageBox
from Tkinter import *

wd = Tkinter.Tk()
wd.tk.call('wm','iconphoto',wd._w,Tkinter.PhotoImage(file="cs.png"))
wd.title("Python CD Helper")
wd.configure(bg='purple')

def executaScript():
    os.system('/eri/Documentos/scriptHelper.py')

Bt = Tkinter.Button(wd,text="Abrir bandeja", command=executaScript, bg='aliceblue', height=10, width=100)
Bt.pack()

Bt.place(relx=0.5, rely=0.5, anchor=CENTER)

wd.mainloop()    
