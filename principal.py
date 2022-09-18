from cProfile import label
from tkinter import *
import poker as pk
from tkinter.ttk import Treeview
import kolmogorov as kol
import promedio as p
from decimal import Decimal
import random

principal = Tk()


Label(principal, text="Pruebas de Aleatoriedad",font=("Arial", 40, "bold"), pady=30).pack()

marco1 = Frame(principal)
marco1.place(x=50, y=200)
marco1.config(width=100,height=200)

marco2 = Frame(principal)
marco2.place(x=500, y=200)
marco2.config(width=100,height=200)

marco3 = Frame(principal)
marco3.config(width=300,height=40)
marco3.pack()

btnpoker = Button(marco2,text="Prueba poker", width=20, height=2, state="disable")
btnpromedio = Button(marco2,text="Prueba promedio", width=20, height=2, state="disable")
btnks = Button(marco2,text="Prueba Kolmogorov", width=20, height=2, state="disable")
btnpoker.grid(row=0,column=0, pady=10)
btnpromedio.grid(row=1,column=0, pady=10)
btnks.grid(row=2,column=0, pady=10)


def btn_pk(vec,cant):
    btnpoker.config(command=(lambda: pk.poker(vec,cant)))
    if cant >= 30:
        btnpoker["state"] = "normal"
    else:
        btnpoker["state"] = "disabled"

def btn_promedio(vec,cant):
    btnpromedio.config(command=(lambda: p.promedio(vec,cant)), state="normal")

def btn_ks(vec,cant):
    btnks.config(command=(lambda: kol.kolmogorov(vec,cant)),state="normal")

def datos(cantvariables):
    vectorpk = []
    vectork = []
    vectorp = []
    
    for i in range(cantvariables):
        rand = round(Decimal(random.random()),5)
        string = str(rand)
        if string.find("0.") == 0:
            new_string = string.replace('0.', '')
        elif string.find("1.") == 0:
            new_string = (string.replace('1.', ''))
        
        vectorpk.append(new_string)
        vectork.append(string)
        vectorp.append(string)  
            
        listbox = Listbox(marco1)
        listbox.grid(row=0, column=0)
        
        
        #for i in range(cantvariables):
        listbox.insert(0, *vectork)
        listbox.config(borderwidth=1, relief="solid", font=1)

    btn_pk(vectorpk,cantvariables)
    btn_promedio(vectork,cantvariables)
    btn_ks(vectorp,cantvariables)


Label(marco3,text="Digite la cantidad de numeros aleatorios:",font=("Arial", 15)).grid(row=0,column=0, padx=10)
cantidad = IntVar()
cantt = IntVar()
cantidad.set("")


cant = Entry(marco3, textvariable=cantidad).grid(row=0,column=1, padx=10)
cantt=cantidad

Button(marco3, text="Ingresar", command=(lambda:[datos(cantidad.get())])).grid(row=0,column=3)


    


principal.geometry('700x500')
principal.mainloop()
