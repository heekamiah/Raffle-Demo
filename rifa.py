# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import font
import random
from tkinter import filedialog

pnc = Tk()
pnc.title("Prueba Rifa  | Gustavo")
pnc.geometry("600x315+330+150")
pnc.resizable(False, False)
slinder1 = PhotoImage(file="fondo.png")
slinder = Label(image=slinder1, cursor="right_ptr")
slinder.place(x=-0, y=-0, relwidth = 1, relheight = 1)


def fileoperations():
    opn = open(ext["text"])
    opn_lines = opn.readlines()
    liste = []
    for line in opn_lines:
        liste.append(line)
    person = random.choice(liste)
    opn.close()
    winner["text"] = person


def selectfile():
    dsy = filedialog.askopenfilename()
    ext["text"] = dsy
    select = Button(text="Obtener un ganador", height=4, bg="white", fg="red", font="Forte", cursor="hand2",
                    command=fileoperations)
    select.place(x=230, y=105)


ext = Label(text="No se encuentra Archivo")
ext.place(x=150, y=30)

dosya = Button(text="Selecciona Archivo", cursor="hand2", command=selectfile, bg="black", fg="white")
dosya.place(x=10, y=30)

on = Label(text="Nuevo Ganador", font="Algerian", fg="red")
on.place(x=150, y=220)

winner = Label(text="Sin Elegir")
winner.place(x=285, y=220)


mainloop()