from tkinter import *
from decimal import Decimal

def poker(vec, cant):
    vector = vec
    cantvariables = cant
    vent2 = Tk()
    vent2.geometry('1100x500')
    resultado = Frame(vent2)
    resultado.place(x=660, y=120)
    resultado.config(width=100,height=100,bg="blue")

    resultado2 = Frame(vent2)
    resultado2.place(x=660, y=330)
    resultado2.config(width=100,height=100,bg="red")

    resultado3 = Frame(vent2)
    resultado3.place(x=660, y=380)
    resultado3.config(width=100,height=100,bg="green")

    Label(vent2, text="Prueba de Poker",font=("Arial", 40, "bold"), pady=20).pack()

    datosframe = Frame(vent2)
    datosframe.config(bg="blue")
    datosframe.place(x=30,y=100)

    canvas = Canvas(datosframe,width=580)
    scrollbar = Scrollbar(datosframe, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    columnap = 0
    filap = 0
    solp = 0
    def posi(randi):
        posibilidad = ""
        d = dict()
        res = [int(x) for x in str(randi)] 

        for item in res:
            try:
                d[item]+=1
            except KeyError:
                d[item]=1

        i = 0
        counti = 0
        countp = 0
        countt = 0
        countpk = 0
        countq = 0

        for g in d.values():
            if g == 2:
                countp +=1
            elif g == 3:
                countt +=1
            elif g == 1:
                counti +=1
            elif g == 4:
                countpk +=1
            elif g == 5:
                countq +=1
            i += 1
            
        if countp == 2:
            posibilidad = "2P"
        elif countt == 1 and countp == 1:
            posibilidad = "F"
        elif countp == 1 or counti == 3:
            posibilidad = "1P"
        elif countt == 1:
            posibilidad = "T"
        elif countpk == 1:
            posibilidad = "PK"
        elif counti == 5 or counti == 4:
            posibilidad = "TD"
        elif countq == 1:
            posibilidad = "Q"
        return posibilidad
    
    contartd = 0
    contar1p = 0
    contar2p = 0
    contart = 0
    contarf = 0
    contarpk = 0
    contarq = 0
    for i in range(cantvariables):
        if columnap == 10:
            columnap = 0
            filap +=1
        
        deci = int(vector[i])/100000
        adu = round(Decimal(deci),5)
        Label(scrollable_frame,text=adu, borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row = filap, column = columnap)
        columnap+=1
        Label(scrollable_frame, text=posi(vector[i]), borderwidth=1, relief="solid", font=1, width=4, height=1, bg="skyblue").grid(row = filap, column = columnap)

        solp = cantvariables * 2
        if (solp%2)==0:
            columnap += 1
            calculo = solp/2
            if columnap >= calculo:
                filap += 1
                columnap = 0
        
        
        if posi(vector[i]) == "TD":
            contartd += 1
        elif posi(vector[i]) == "1P":
            contar1p += 1
        elif posi(vector[i]) == "2P":
            contar2p += 1
        elif posi(vector[i]) == "T":
            contart += 1
        elif posi(vector[i]) == "F":
            contarf += 1
        elif posi(vector[i]) == "PK":
            contarpk += 1
        elif posi(vector[i]) == "Q":
            contarq += 1

            
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
       
    vecposi = ['TD',"1P","2P","T","F","PK","Q"]
    vecconte = [contartd,contar1p,contar2p,contart,contarf,contarpk,contarq]
    vecprob = [0.3024,0.504,0.108,0.072,0.009,0.0045,0.0001]
    

    
    #Label(resultado,text="FO").grid(row=0,column=1)
    fe = []
    xo = []
    sumxo = 0
    x=1
    for x in range(7):
        """#Label(resultado,text="Posibilidad").grid(row=0,column=0)
        Label(resultado,text=vecposi[x], borderwidth=1, relief="solid", font=1, width=8, height=1, bg="green").grid(row=x,column=0)
        #Label(resultado,text="FO").grid(row=0,column=1)
        Label(resultado,text=vecconte[x], borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=x,column=1)
        #Label(resultado,text="Probabilidad").grid(row=0,column=2)
        Label(resultado,text=vecprob[x], borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=x,column=2) """
        fe.append(round(vecprob[x]*cantvariables,5))
        #Label(resultado,text="FE").grid(row=0,column=3)
        #Label(resultado,text=fe[x], borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=x,column=3)

        xo.append(((vecconte[x]-fe[x])**2)/fe[x])
        
    Label(resultado,text="Posibilidad", borderwidth=1, relief="solid", font=("Arial",11,"bold"), width=20, height=1, bg="green").grid(row=0,column=0)
    Label(resultado,text="Todos diferentes (TD)", borderwidth=1, relief="solid", font=("Arial",11,"bold"), width=20, height=1, bg="green").grid(row=1,column=0)
    Label(resultado,text="Un par (1P)", borderwidth=1, relief="solid", font=("Arial",11,"bold"), width=20, height=1, bg="green").grid(row=2,column=0)
    Label(resultado,text="Dos pares (2P)", borderwidth=1, relief="solid", font=("Arial",11,"bold"), width=20, height=1, bg="green").grid(row=3,column=0)
    Label(resultado,text="Tercia (T)", borderwidth=1, relief="solid", font=("Arial",11,"bold"), width=20, height=1, bg="green").grid(row=4,column=0)
    Label(resultado,text="Full (F)", borderwidth=1, relief="solid", font=("Arial",11,"bold"), width=20, height=1, bg="green").grid(row=5,column=0)
    Label(resultado,text="Poker (PK)", borderwidth=1, relief="solid", font=("Arial",11,"bold"), width=20, height=1, bg="green").grid(row=6,column=0)
    Label(resultado,text="Quintilla (Q)", borderwidth=1, relief="solid", font=("Arial",11,"bold"), width=20, height=1, bg="green").grid(row=7,column=0)

    sumatotalcont = sum(vecconte)
    Label(resultado,text="FO", borderwidth=1, relief="solid", font=("Arial",11,"bold"), width=8, height=1, bg="green").grid(row=0,column=1)
    Label(resultado,text=contartd, borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=1,column=1)
    Label(resultado,text=contar1p, borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=2,column=1)
    Label(resultado,text=contar2p, borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=3,column=1)
    Label(resultado,text=contart, borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=4,column=1)
    Label(resultado,text=contarf, borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=5,column=1)
    Label(resultado,text=contarpk, borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=6,column=1)
    Label(resultado,text=contarq, borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=7,column=1)
    Label(resultado,text=sumatotalcont, borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=8,column=1)
    sumatotalpro = round(sum(vecprob),0)
    Label(resultado,text="Probabilidad", borderwidth=1, relief="solid", font=("Arial",11,"bold"), width=10, height=1, bg="green").grid(row=0,column=2)
    Label(resultado,text="0.3024", borderwidth=1, relief="solid", font=1, width=10, height=1).grid(row=1,column=2)
    Label(resultado,text="0.504", borderwidth=1, relief="solid", font=1, width=10, height=1).grid(row=2,column=2)
    Label(resultado,text="0.108", borderwidth=1, relief="solid", font=1, width=10, height=1).grid(row=3,column=2)
    Label(resultado,text="0.072", borderwidth=1, relief="solid", font=1, width=10, height=1).grid(row=4,column=2)
    Label(resultado,text="0.009", borderwidth=1, relief="solid", font=1, width=10, height=1).grid(row=5,column=2)
    Label(resultado,text="0.0045", borderwidth=1, relief="solid", font=1, width=10, height=1).grid(row=6,column=2)
    Label(resultado,text="0.0001", borderwidth=1, relief="solid", font=1, width=10, height=1).grid(row=7,column=2)
    Label(resultado,text=int(sumatotalpro), borderwidth=1, relief="solid", font=1, width=10, height=1).grid(row=8,column=2)    
    
    
    sumafe = round(sum(fe),0)
    sumxo = round(sum(xo),5)

    Label(resultado,text="FE", borderwidth=1, relief="solid", font=("Arial",11,"bold"), width=8, height=1, bg="green").grid(row=0,column=3)
    Label(resultado,text=fe[0], borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=1,column=3)
    Label(resultado,text=fe[1], borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=2,column=3)
    Label(resultado,text=fe[2], borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=3,column=3)
    Label(resultado,text=fe[3], borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=4,column=3)
    Label(resultado,text=fe[4], borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=5,column=3)
    Label(resultado,text=fe[5], borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=6,column=3)
    Label(resultado,text=fe[6], borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=7,column=3)
    Label(resultado,text=int(sumafe), borderwidth=1, relief="solid", font=1, width=8, height=1).grid(row=8,column=3)

    Label(resultado,text="TOTAL", borderwidth=1, relief="solid", font=("Arial",11,"bold"), width=20, height=1, bg="green").grid(row=8,column=0)
    Label(resultado,text=sumatotalcont, borderwidth=1, relief="solid", font=("Arial", 10, "bold"), width=9, height=1).grid(row=8,column=1)
    Label(resultado,text=int(sumatotalpro), borderwidth=1, relief="solid", font=("Arial", 10, "bold"), width=11, height=1).grid(row=8,column=2)
    Label(resultado,text=int(sumafe), borderwidth=1, relief="solid", font=("Arial", 10, "bold"), width=9, height=1).grid(row=8,column=3)

    Label(resultado2, text="Xo", borderwidth=1, relief="solid", font=("Arial",11,"bold"), width=8, height=1, bg="green").grid(row=0,column=0)
    Label(resultado2, text=sumxo, borderwidth=1, relief="solid", font=1, width=10, height=1).grid(row=0,column=1)
    Label(resultado2, text="Tabla", borderwidth=1, relief="solid", font=("Arial",11,"bold"), width=8, height=1, bg="green").grid(row=1,column=0)
    Label(resultado2, text="12.5916", borderwidth=1, relief="solid", font=1, width=10, height=1).grid(row=1,column=1)

    prueba = ""

    if sumxo < 12.5916:
        prueba = "La muestra pasa la prueba"
    else:
        prueba = "La muestra no pasa la prueba"
    
    Label(resultado3,text=prueba,font=("Arial", 10, "bold")).pack()
    vent2.mainloop()