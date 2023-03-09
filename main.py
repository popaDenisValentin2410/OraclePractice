import os
from tkinter import *
#import random
import tkinter as tk

import tkinter.font as tkFont

root=Tk()
root.title("undefined")
#setting window size
width=389
height=702
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
img = PhotoImage(file='Fără titlu.png')
label = Label(
    root,
    image=img
)
label.place(x=0, y=0)






def ComandaProfesor():
    with open('cecautam.txt', 'w') as f:
        f.write('1')
    root.destroy()
    os.system(('Profesor.py'))


def ComandaClasa():
    with open('cecautam.txt', 'w') as f:
        f.write('2')
    root.destroy()
    os.system(('Profesor.py'))


def ComandaMaterie():
    with open('cecautam.txt', 'w') as f:
        f.write('3')
    root.destroy()
    os.system(('Profesor.py'))

butonMaterie=tk.Button(root)
butonMaterie["bg"] = "#000000"
ft = tkFont.Font(family='Times',size=13)
butonMaterie["font"] = ft
butonMaterie["fg"] = "#ffffff"
butonMaterie["justify"] = "center"
butonMaterie["text"] = "Materia"
butonMaterie["relief"] = "flat"
butonMaterie.place(x=20,y=230,width=341,height=57)
butonMaterie["command"] = ComandaMaterie

butonClasa=tk.Button(root)
butonClasa["bg"] = "#000000"
ft = tkFont.Font(family='Times',size=13)
butonClasa["font"] = ft
butonClasa["fg"] = "#fffcfc"
butonClasa["justify"] = "center"
butonClasa["text"] = "Clasa"
butonClasa.place(x=20,y=350,width=341,height=57)
butonClasa["command"] = ComandaClasa

butonProfesor=tk.Button(root)
butonProfesor["bg"] = "#000000"
ft = tkFont.Font(family='Times',size=13)
butonProfesor["font"] = ft
butonProfesor["fg"] = "#ffffff"
butonProfesor["justify"] = "center"
butonProfesor["text"] = "Profesor"
butonProfesor.place(x=20,y=470,width=341,height=57)
butonProfesor["command"] = ComandaProfesor





root.mainloop()
