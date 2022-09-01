import tkinter
from tkinter import *
import random
from PIL import Image, ImageTk
from tkinter import messagebox

ventana = tkinter.Tk()
ventana.geometry("350x200")

def juego(jugador):
    imagen_juego = "fondo.jpg"
    imagen_juego1 = "fondo.jpg"
    opciones = ["piedra", "papel", "tijera", "spock", "lagarto"]
    pc = random.choice(opciones)
    if jugador == pc:
        Resultado["text"] = "Empate"
    elif jugador == "piedra" and pc == "tijera":
        Resultado["text"] = "Ganaste"
    elif jugador == "papel" and pc == "piedra":
        Resultado["text"] = "Ganaste"
    elif jugador == "tijera" and pc == "papel":
        Resultado["text"] = "Ganaste"
    elif jugador == "lagarto" and pc == "spock":
        Resultado["text"] = "Ganaste"
    elif jugador == "spock" and pc == "tijera":
        Resultado["text"] = "Ganaste"
    elif jugador == "piedra" and pc == "lagarto":
        Resultado["text"] = "Ganaste"
    elif jugador == "papel" and pc == "spock":
        Resultado["text"] = "Ganaste"
    elif jugador == "tijera" and pc == "lagarto":
        Resultado["text"] = "Ganaste"
    elif jugador == "lagarto" and pc == "papel":
        Resultado["text"] = "Ganaste"
    elif jugador == "spock" and pc == "piedra":
        Resultado["text"] = "Ganaste"
    else:
        Resultado["text"] = "Perdiste"
    opcion_pc["text"] = f"La computadora escogió: {pc}"

    if jugador == "piedra":
        imagen_juego = "piedra.jpg"
    elif jugador == "papel":
        imagen_juego = "papel.jpg"
    elif jugador == "tijera":
        imagen_juego = "tijeras.jpg"
    elif jugador == "lagarto":
        imagen_juego = "lagarto.jpg"
    elif jugador =="spock":
        imagen_juego = "spock.jpg"

    img = Image.open(imagen_juego)
    new_img = img.resize((50,50))
    render = ImageTk.PhotoImage(new_img)
    img1 = Label(ventana, image = render)
    img1.image = render
    img1.grid(row = 14, column = 4)

    if pc == "piedra":
        imagen_juego1 = "piedra.jpg"
    elif pc == "papel":
        imagen_juego1 = "papel.jpg"
    elif pc == "tijera":
        imagen_juego1 = "tijeras.jpg"
    elif pc == "lagarto":
        imagen_juego1 = "lagarto.jpg"
    elif pc =="spock":
        imagen_juego1 = "spock.jpg"

    img2 = Image.open(imagen_juego1)
    new_img2 = img2.resize((50,50))
    render2 = ImageTk.PhotoImage(new_img2)
    img2 = Label(ventana, image = render2)
    img2.image = render2
    img2.grid(row = 14, column = 20)

def fin():
    salir = messagebox.askquestion("salir", "¿Desea salir del juego?")
    if salir == 'yes':
        ventana.quit()
        ventana.destroy()

j1 = tkinter.Label(ventana, text = "JUGADOR", bg = "gray")
j1.grid(row = 8, column = 0)
pc1 = tkinter.Label(ventana, text = "COMPUTADORA", bg = "gray")
pc1.grid(row = 8, column = 20)
piedra = tkinter.Button(ventana, text = "Piedra", command = lambda: juego("piedra"))
piedra.grid(row = 10, column = 0)
papel = tkinter.Button(ventana, text = "papel", command = lambda: juego("papel"))
papel.grid(row = 12, column = 0)
tijeras = tkinter.Button(ventana, text = "tijeras", command = lambda: juego("tijera"))
tijeras.grid(row = 14, column = 0)
lagarto = tkinter.Button(ventana, text = "lagarto", command = lambda: juego("lagarto"))
lagarto.grid(row = 16, column = 0)
spock = tkinter.Button(ventana, text = "spock", command = lambda: juego("spock"))
spock.grid(row = 18, column = 0)
salir = tkinter.Button(ventana, text = "Salir", command = fin)
salir.grid(row = 50, column = 20)
vs = tkinter.Label(ventana, text = "VS", bg = "gray")
vs.grid(row = 14, column = 18)
Resultado = tkinter.Label(ventana)
Resultado.grid(row = 50, column = 18)
opcion_pc = tkinter.Label(ventana)
opcion_pc.grid(row = 12, column = 20)
ventana.mainloop()