from tkinter import *

#inicial tkinter
aplicacion = Tk()

#tamaño de la ventana
aplicacion.geometry('1020x630+0+0')
#evitar maximizar
aplicacion.resizable(0,0)
#titulo de la ventana
aplicacion.title("Mi restaurante - sistema de facturación")
#colo de fonde de la ventada
aplicacion.config(bg="burlywood")
#panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)
#etiqueta titulo
etiqueta_titulo = Label(panel_superior, text="Sistema de facturación", fg="azure4",
                        font=("Dosis", "28"), bg="burlywood", width="27")
etiqueta_titulo.grid(row=0, column=0)
#panel izquiedo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)
#panel de costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)
#panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text="Comida", font=("Dosis", "19", "bold"),
                           bd=1, relief=FLAT, bg="azure4" )
panel_comidas.pack(side=LEFT)
#panel Bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas", font=("Dosis", "19", "bold"),
                           bd=1, relief=FLAT, bg="azure4" )
panel_bebidas.pack(side=LEFT)
#panel Postres
panel_postres = LabelFrame(panel_izquierdo, text="Postres", font=("Dosis", "19", "bold"),
                           bd=1, relief=FLAT, bg="azure4" )
panel_postres.pack(side=LEFT)
#panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)
#panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1,relief=FLAT,bg="burlywood")
panel_calculadora.pack()
#panel recibo
panel_recibo = Frame(panel_derecha, bd=1,relief=FLAT,bg="burlywood")
panel_recibo.pack()
#panel botones
panel_botones = Frame(panel_derecha, bd=1,relief=FLAT,bg="burlywood")
panel_botones.pack()


#Lista de productos
lista_comidas = ["Pollo", "Cordero", "Salmon", "Merluza", "Completos", "Pizza", "Empanadas", "Choclo"]
lista_bebidas = ["Jugo", "Cocacola", "fanta", "Sprite", "Cristal", "Pepsi", "Escudo", "Pisco"]
lista_postres = ["Torta", "Pie", "Helado", "Galletas", "Tortillas", "Panqueques", "Sandia", "Bananasplit"]

#generar items de comida
variables_comida = []
contador = 0
for comida in lista_comidas:
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(),font=("Dosis", "19", "bold"),
                        onvalue=1,offvalue=0, variable=variables_comida[contador] )
    comida.grid(row=contador, column=0, sticky=W)
    contador += 1

#generar items de bebida
variables_bebida = []
contador = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(),font=("Dosis", "19", "bold"),
                        onvalue=1,offvalue=0, variable=variables_bebida[contador] )
    bebida.grid(row=contador, column=0, sticky=W)
    contador += 1

#generar items de postre
variables_postre = []
contador = 0
for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(),font=("Dosis", "19", "bold"),
                        onvalue=1,offvalue=0, variable=variables_postre[contador] )
    postre.grid(row=contador, column=0, sticky=W)
    contador += 1
#evitar que la pantalla se cierre
aplicacion.mainloop()