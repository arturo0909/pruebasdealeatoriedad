from math import sqrt
from tkinter import *
from scipy.stats import t

def promedio(vecp, cant):
    ventpro = Tk()
    vector = vecp
    vectorp = []
    Label(ventpro, text="Prueba de Promedio",font=("Arial", 40, "bold"), pady=20).pack()
    datosrandom = Frame(ventpro)
    datosrandom.place(x=30, y=110)
    datosrandom.config(bg="blue", width=500, height=300)
    resultado = Frame(ventpro)
    resultado.place(x=450, y=110)
    resultado.config(width=100, height=100,bg="red")
    resultado2 = Frame(ventpro)
    resultado2.place(x=450, y=220)
    resultado2.config(width=100, height=40,bg="green")
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
    for i in range(cant):
    
        vectorp.append(float(vector[i]))
        if columna == 5:
            columna = 0
            fila +=1
        Label(scrollable_frame,text=vector[i], borderwidth=1, relief="solid", font=1, width=7, height=1).grid(row=fila, column=columna)
        sol = cant * 2
        if (sol%2)==0:
            columna += 1
            calculo = sol/2
            if columna >= calculo:
                fila += 1
                columna = 0
        j = i+1

    x = round(sum(vectorp)/cant,5)
    zo = round(((x-0.5)*sqrt(cant))/sqrt(1/12),5)
    z2 = round(zo/2,5)
    zo = abs(round(((x-0.5)*sqrt(cant))/sqrt(1/12),5))
    z2=abs(round(t.ppf(0.05, cant),5))
    prueba = ""

    Label(resultado, text="x", borderwidth=1, relief="solid", font=("Arial",11,"bold"), width=8, height=1, bg="green").grid(row=0,column=0)
    Label(resultado, text="N", borderwidth=1, relief="solid", font=("Arial",11,"bold"), width=8, height=1, bg="green").grid(row=1,column=0)
    Label(resultado, text="Zo", borderwidth=1, relief="solid", font=("Arial",11,"bold"), width=8, height=1, bg="green").grid(row=2,column=0)
    Label(resultado, text="Zα/2", borderwidth=1, relief="solid", font=("Arial",11,"bold"), width=8, height=1, bg="green").grid(row=3,column=0)
    Label(resultado, text=x, borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=0,column=1)
    Label(resultado, text=cant, borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=1,column=1)
    Label(resultado, text=zo, borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=2,column=1)
    Label(resultado, text=z2, borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=3,column=1)
    if zo < z2:
        prueba = "La muestra pasa la prueba"
    else:
        prueba = "La muestra no pasa la prueba"

    Label(resultado2, text=prueba, font=("Arial", 10, "bold")).pack()
    ventpro.geometry('700x400')
    ventpro.mainloop()
    ventpro.mainloop()
