##importar módulos necesarios
#from cgitb import grey
#from tkinter import *
#
##crear interfáz de selección 
#win = Tk()
#
##obtener información de la pantalla
#width= win.winfo_screenwidth()
#height= win.winfo_screenheight()
#
##tamaño ventana
#win.geometry("%dx%d" % (width, height))
#
##color de fondo
#win.configure(bg = "grey")
#
#msg = Message( text = "We ")    
#
#rock = Button(win, text = "rock", bg = "brown",).grid(row = 10, column = 0)  
#
#paper = Button(win, text = "paper",bg = "white").grid(row = 10, column = 1)  
#
#scissors = Button(win, text = "scissors", bg = "red").grid(row = 10, column = 2)  
#
#win.mainloop()  



import functions

import pygame
# iniciar la reproducción de la música
pygame.mixer.init()
my_sound = pygame.mixer.Sound('piano2.ogg')
my_sound.play()
pygame.time.wait(int(my_sound.get_length() * 000))

# mostrar creador
print("   _____                     __   _______  ")
print("  / ____|                    \ \ / /  __ \ ")
print(" | (___  _   _  __ _  __ _ _ _\ V /| |__) |")
print("  \___ \| | | |/ _` |/ _` | '__> < |  ___/ ")
print("  ____) | |_| | (_| | (_| | | / . \| |     ")
print(" |_____/ \__,_|\__, |\__,_|_|/_/ \_\_|     ")
print("                __/ |                      ")
print("               |___/                       ")
print("")




print("Bienvenido al juego integrado de piedra papel o tijeras!\n")

dificultad = input("elige tu dificultad: fácil (1) o dificil (2)\n")

print("Para jugar necesitas introducir una de tres opciones: piedra (pi), papel (pa) o tijeras (ti)\n")

if str(dificultad) == "1":
    functions.modo_facil()
elif str(dificultad) == "2":
    functions.modo_pro()
else: print("error 03 :( .Por favor, elija 1 o 2 para la dificultad")