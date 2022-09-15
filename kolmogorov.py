from tkinter import *
import random
from tkinter import font
from tkinter.ttk import Treeview

def kolmogorov(vec, cantvariables):
    vecpri = vec
    vector = []
    vectorposi = []
    vectorresultado = []


    ventkolmo = Tk()
    tabla = Treeview(ventkolmo,columns=("posicion", "burbuja", "resta"))
    tabla.place(x=440, y=110)

    Label(ventkolmo, text="Prueba de Kolmogorov",font=("Arial", 40, "bold"), pady=20).pack()

    datosrandom = Frame(ventkolmo)
    datosrandom.place(x=30, y=110)
    datosrandom.config(bg="blue", width=300, height=300)

    resultado2 = Frame(ventkolmo)
    resultado2.place(x=440, y=350)
    resultado2.config(width=100,height=100,bg="red")

    resultado3 = Frame(ventkolmo)
    resultado3.place(x=440, y=410)
    resultado3.config(width=100,height=100,bg="green")

    tabla.column("#0",width=80)
    tabla.column("posicion",width=90, anchor=CENTER)
    tabla.column("burbuja",width=80, anchor=CENTER)
    tabla.column("resta",width=80, anchor=CENTER)

    tabla.heading("#0", text="n", anchor=CENTER)
    tabla.heading("posicion", text="Vector posicion", anchor=CENTER)
    tabla.heading("burbuja", text="Burbuja", anchor=CENTER)
    tabla.heading("resta", text="VP-Burb", anchor=CENTER)

    canvas = Canvas(datosrandom, width=380)
    scrollbar = Scrollbar(datosrandom, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    i=1
    sol = 0
    fila = 0
    columna = 0

    for i in range(cantvariables):
    
        vector.append(float(vecpri[i]))

        if columna == 5:
            columna = 0
            fila +=1

        Label(scrollable_frame,text=vecpri[i], borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=fila, column=columna)

        sol = cantvariables * 2
        if (sol%2)==0:
            columna += 1
            calculo = sol/2
            if columna >= calculo:
                fila += 1
                columna = 0
        j = i+1

        recta = round(j/cantvariables,5)
        vectorposi.append(recta)
        #print(vector[i])
        #tabla.insert("",END,text=j, values=(recta))
        #print(vectorposi[i])

    vectorordenado =  sorted(vector)

    contas = []

    for i in range(cantvariables):
        j = i+1
        resta = round(abs(vectorposi[i]-vectorordenado[i]),5)
        vectorresultado.append(resta)
        contas.append((vectorposi[i],vectorordenado[i],vectorresultado[i]))
        tabla.insert("",END,text=j, values=(contas[i]))

    mayor = max(vectorresultado)

    Label(resultado2, text="Max", borderwidth=1, relief="solid", font=("Arial",11,"bold"), width=8, height=1, bg="green").grid(row=0,column=0)
    Label(resultado2, text=mayor, borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=0,column=1)
    Label(resultado2, text="Tabla", borderwidth=1, relief="solid", font=("Arial",11,"bold"), width=8, height=1, bg="green").grid(row=1,column=0)

    ventkolmo.geometry('800x500')
    ventkolmo.mainloop()

#la prueba pasa cuando el maximo es menor al de la tabla