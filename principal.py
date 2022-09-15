from tkinter import *
import poker as pk
import kolmogorov as kol
import promedio as p
from decimal import Decimal
import random

principal = Tk()

marco1 = Frame(principal)
marco1.place(x=50, y=200)
marco1.config(width=100,height=200)

canvas = Canvas(marco1,width=380)
scrollbar = Scrollbar(marco1, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)


canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

Label(principal, text="Pruebas de Aleatoriedad",font=("Arial", 40, "bold"), pady=30).pack()



def datos(cantvariables):
    fila = 0
    columna = 0
    vector = []
    vectork = []
    vectorp = []
    
    for i in range(cantvariables):
        rand = round(Decimal(random.random()),5)
        string = str(rand)
        if string.find("0.") == 0:
            new_string = string.replace('0.', '')
        elif string.find("1.") == 0:
            new_string = (string.replace('1.', ''))
        
        vector.append(new_string)
        vectork.append(string)
        vectorp.append(string)
        
        if columna == 5:
            columna = 0
            fila +=1
            
        label = Label(scrollable_frame,text=rand, borderwidth=1, relief="solid", font=1,width=8, height=1).grid(row = fila, column = columna)
        
        if (cantvariables%2)==0:
            columna += 1
            calculo = cantvariables/2
            if columna >= calculo:
                fila += 1
                columna = 0
        elif (cantvariables%2)==1:
            columna += 1
            calculo = cantvariables/2
            if columna >= calculo and columna <=10:
                fila += 1
                columna = 0

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    marco2 = Frame(principal)
    marco2.place(x=500, y=200)
    marco2.config(width=100,height=200)



    btnpromedio = Button(marco2,text="Prueba promedio", width=20, height=2, command=(lambda: p.promedio(vectorp,cantvariables))).grid(row=0,column=0,pady=10, padx=10)

    btnpoker = Button(marco2,text="Prueba poker", width=20, height=2, command=(lambda: pk.poker(vector,cantvariables)))
    if cantvariables >= 30:
        btnpoker.grid(row=2,column=0,pady=10, padx=10)
        btnpoker["state"] = "normal"
    else:
        btnpoker.grid(row=2,column=0,pady=10, padx=10)
        btnpoker["state"] = "disabled"

    btnprueba = Button(marco2,text="Prueba Kolmogorov", width=20, height=2,command=(lambda: kol.kolmogorov(vectork,cantvariables))).grid(row=8,column=0,pady=10, padx=10)

    
marco3 = Frame(principal)
marco3.config(width=300,height=40)
marco3.pack()



Label(marco3,text="Digite la cantidad de numeros aleatorios:",font=("Arial", 15)).grid(row=0,column=0, padx=10)
cantidad = IntVar()
cant = Entry(marco3, textvariable=cantidad).grid(row=0,column=1, padx=10)

Button(marco3, text="Ingresar", command=(lambda:datos(cantidad.get()))).grid(row=0,column=3)


principal.geometry('700x500')
principal.mainloop()