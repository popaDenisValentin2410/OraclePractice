import os
from tkinter import *
#import random
import tkinter as tk

import tkinter.font as tkFont

import Backend


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
img = PhotoImage(file='imagineFereastra.png')
label = Label(
    root,
    image=img
)
label.place(x=0, y=0)


numeElev = StringVar()
clasa = StringVar()
cnpElev = IntVar()
ID = IntVar()



linie=tk.Entry(root)
linie["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
linie["font"] = ft
linie["fg"] = "#333333"
linie["justify"] = "center"
linie["text"] = "Entry"
linie["textvariable"] = clasa


linie2=tk.Entry(root)
linie2["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
linie2["font"] = ft
linie2["fg"] = "#333333"
linie2["justify"] = "center"
linie2["text"] = "Entry"
linie2["textvariable"] = ID



lista=tk.Listbox(root)
lista["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
lista["font"] = ft
lista["fg"] = "#333333"
lista["justify"] = "center"
lista.place(x=60,y=230,width=263,height=281)

print(clasa)

with open('cecautam.txt') as f:
    fereastra=f.readline()


if fereastra == '2':
    linie.place(x=80, y=70, width=203, height=43)
else:
    linie2.place(x=80, y=70, width=203, height=43)
print(fereastra)

linie2=tk.Entry(root)
linie2["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
linie2["font"] = ft
linie2["fg"] = "#333333"
linie2["justify"] = "center"
linie2["text"] = "Entry"
linie2["textvariable"] = ID

var1=IntVar()
var2=IntVar()

linie31=tk.Entry(root)
linie31["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
linie31["font"] = ft
linie31["fg"] = "#333333"
linie31["justify"] = "center"
linie31["text"] = "Entry"
linie31["textvariable"] = var1

linie24=tk.Entry(root)
linie24["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
linie24["font"] = ft
linie24["fg"] = "#333333"
linie24["justify"] = "center"
linie24["text"] = "Entry"
linie24["textvariable"] = var2


numeMaterie = StringVar()
linie3=tk.Entry(root)
linie3["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
linie3["font"] = ft
linie3["fg"] = "#333333"
linie3["justify"] = "center"
linie3["text"] = "Entry"
linie3["textvariable"] = numeMaterie
if fereastra =='3':
    linie3.place(x=150, y=600)
def ComandaAdaugareMaterie():
    Backend.AdaugareMaterie(numeMaterie.get())





def comandaToti():
    row = Backend.calculsalariutoti()
    lista.insert(END, row)

def ComandaCautare():
    lista.place(x=60, y=230, width=263, height=281)
    count=0
    Backend.modificare2(var1.get(), var2.get())
    if fereastra == '2':
        for row in Backend.AfisareElev( clasa.get() ): #pentru butonul clasa
            lista.insert(END, row)
            count = 1+ count
        lista.insert(END,count)
    if fereastra == '1':
        row=Backend.calculsalariu(ID.get()) #pentru butonul profesor
        lista.insert(END, row , "de euro")

    if fereastra == '3':
        row = Backend.ProfesoriPerMaterie(ID.get()) #pentru butonul materie
        lista.insert(END, row, "Profesori")

def ComandaBack():
    root.destroy()
    os.system(('main.py'))


butonAdauga=tk.Button(root)
butonAdauga["bg"] = "#ffffff"
ft = tkFont.Font(family='Times',size=10)
butonAdauga["font"] = ft
butonAdauga["fg"] = "#000000"
butonAdauga["justify"] = "center"
butonAdauga["text"] = "Adauga"
if fereastra == '3':
    butonAdauga.place(x=50,y=600,width=46,height=44)
butonAdauga["command"] = ComandaAdaugareMaterie


butonCautare=tk.Button(root)
butonCautare["bg"] = "#000000"
ft = tkFont.Font(family='Times',size=10)
butonCautare["font"] = ft
butonCautare["fg"] = "#ffffff"
butonCautare["justify"] = "center"
butonCautare["text"] = "Cauta"
butonCautare.place(x=300,y=70,width=46,height=44)
butonCautare["command"] = ComandaCautare

butonToti = tk.Button(root)
butonToti["bg"] = "#000000"
ft = tkFont.Font(family='Times', size=10)
butonToti["font"] = ft
butonToti["fg"] = "#ffffff"
butonToti["justify"] = "center"
butonToti["text"] = "Toti"
butonToti["command"] = comandaToti

if fereastra == '1':
    butonToti.place(x=150, y=115, width=70, height=25)

butonBack = tk.Button(root)
butonBack["bg"] = "#000000"
ft = tkFont.Font(family='Times', size=10)
butonBack["font"] = ft
butonBack["fg"] = "#ffffff"
butonBack["justify"] = "center"
butonBack["text"] = "Back"
butonBack.place(x=2, y=2, width=40, height=30)
butonBack["command"] = ComandaBack






root.mainloop()
