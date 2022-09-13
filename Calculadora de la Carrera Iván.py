from sympy import *
from sympy.parsing.sympy_parser import parse_expr  
from tkinter import *


def derivada():
    try:
        x = symbols('x')
        fun_escrita = funcion.get()
        f = parse_expr(fun_escrita)
        derivada = diff(f, x)
        etiqueta.configure(text=derivada)
    except:
        etiqueta.configure(text="Introduce la función correctamente")


def integral():
    try:
        x = symbols('x')
        fun_escrita2 = funcion.get()
        g = parse_expr(fun_escrita2)
        integral = integrate(g, x)
        etiqueta.configure(text=integral)
    except:
        etiqueta.configure(text="Introduce la función correctamente")


ventana = Tk()
ventana.geometry('400x280')
ventana.title("La mejor calculadora del Mundo: f(x)")

anuncio = Label(ventana, text="Introduce una función de x:", font=("Times New Roman", 15), fg="blue")
anuncio.pack()

funcion = Entry(ventana, font=("Times New Roman", 15))
funcion.pack()

etiqueta = Label(ventana, text="Resultado", font=("Times New Roman", 15), fg="red")
etiqueta.pack()

boton1 = Button(ventana, text="Derivar Función", font=("Times New Roman", 15), command=derivada)
boton1.pack()

boton2 = Button(ventana, text="Integrar Función", font=("Times New Roman", 15), command=integral)
boton2.pack()


def _quit():
    ventana.quit()
    ventana.destroy()


button3 = Button(master=ventana, text="Salir", font=("Arial", 15), command=_quit)
button3.pack()

ventana.mainloop()
