from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox




def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')

    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f' Costo de la Comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f' Costo de la Bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f' Costo de la Postres: \t\t\t{var_costo_postres.get()}\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f' Sub-total: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f' Impuestos: \t\t\t{var_impuestos.get()}\n')
    texto_recibo.insert(END, f' Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Lo esperamos pronto')

# iniciar tkinter
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry('760x420+0+0')

# evitar maximizar
aplicacion.resizable(0, 0)

# titulo de la ventana
aplicacion.title("Asistente gpt")

# color de fondo de la ventana
aplicacion.config(bg='black')

# panel izquierda
panel_izquierda = Frame(aplicacion,
                        bd=1,
                        bg='black',
                        relief=FLAT)
panel_izquierda.pack(side=TOP)

#entry apy_key
entry_key = Entry(panel_izquierda,
                    font=('Dosis', 11),
                    width=50,
                    bd=1)
entry_key.pack()

# panel recibo
panel_recibo = Frame(panel_izquierda,
                    bd=1,
                    relief=FLAT,
                    bg='black')
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_izquierda,
                    bd=1,
                    relief=FLAT,
                    bg='black')
panel_botones.pack()

# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()


# botones
botones         = ['Iniciar']
botones_creados = []

columnas = 0
boton = Button(panel_botones,
                text="iniciar",
                font=('Dosis', 10,),
                fg='black',
                bg='red',
                width=19)


boton.grid(row=0,
            column=columnas)

boton.config(command=recibo)

# area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=50,
                    height=10)
texto_recibo.grid(row=0,
                  column=0)






# evitar que la pantalla se cierre
aplicacion.mainloop()
