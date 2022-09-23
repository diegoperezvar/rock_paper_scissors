import random
from time import sleep

def modo_facil():
    number = 0
    derrotas = 0
    while number < 10:
        valor1 = input("introduce tu elección: ")

        eleccion_jugador = "tijeras"

        if valor1 == "pi" :
            eleccion_jugador = "piedra"

        elif valor1 == "pa":
            eleccion_jugador = "papel"

        elif valor1 == "ti":
            eleccion_jugador = "tijeras"

        else:
            print("Error 01, el valor introducido no ha sido reconocido  ;("), exit()

        print("elegiste: " + str(eleccion_jugador))

        elecciones = ["piedra","papel","tijeras"]

        eleccion_ordenador = random.choices(elecciones)

        sleep(2)

        print("el ordenador eligió " + str(eleccion_ordenador))

        sleep(1)

        if eleccion_jugador ==  eleccion_ordenador:
            print("empate!")

        elif eleccion_jugador == "piedra": 
            if str(eleccion_ordenador) == "['papel']":
                print("perdiste!")
                derrotas = derrotas + 1
            elif  str(eleccion_ordenador) == "['tijeras']"  :
                 print("ganaste!")
                 number = number + 1
        elif eleccion_jugador == "papel":  
            if str(eleccion_ordenador) == "['piedra']":
                print("ganaste!")
                number = number + 1
            elif  str(eleccion_ordenador) == "['tijeras']"  : 
                print("perdiste!")
                derrotas = derrotas + 1
        elif eleccion_jugador == "tijeras": 
            if  str(eleccion_ordenador) == "['piedra']":
                print("perdiste!")
                derrotas = derrotas + 1
            elif  str(eleccion_ordenador) == "['papel']"  : 
                print("ganaste!")
                number = number + 1
            else: print("empate")
        else: print("error 02 ;c")
        
        print("número de victorias: " + str(number) + "/10")
        print("número de derrotas: " + str(derrotas))

def modo_pro():
    number = 0
    while number < 10:
        derrotas = 0
        valor1 = input("introduce tu elección: ")

        eleccion_jugador = "tijeras"

        if valor1 == "pi" :
            eleccion_jugador = "piedra"

        elif valor1 == "pa":
            eleccion_jugador = "papel"

        elif valor1 == "ti":
            eleccion_jugador = "tijeras"

        else:
            print("Error 01, el valor introducido no ha sido reconocido  ;("), exit()

        print("elegiste: " + str(eleccion_jugador))

        eleccion_ordenador = "tijeras"

        if eleccion_jugador == "piedra": 
            eleccion_ordenador = "papel"  

        elif eleccion_jugador == "papel":  

            eleccion_ordenador = "tijeras"
        elif eleccion_jugador == "tijeras": 

            eleccion_ordenador = "piedra"
        else: print("error 02 ;c")

        sleep(2)

        print("el ordenador elijió " + str(eleccion_ordenador))

        sleep(1)

        if eleccion_jugador == "piedra": 
            if str(eleccion_ordenador) == "papel":
                print("perdiste!")
                derrotas = derrotas + 1
            elif  str(eleccion_ordenador) == "tijeras"  : 
                print("ganaste!")
                number = number + 1
        elif eleccion_jugador == "papel":  
            if str(eleccion_ordenador) == "piedra":
                print("ganaste!")
                
                number = number + 1
            elif  str(eleccion_ordenador) == "tijeras"  : 
                print("perdiste!")
                derrotas = derrotas + 1
        elif eleccion_jugador == "tijeras": 
            if  str(eleccion_ordenador) == "piedra":
                print("perdiste!")
                derrotas = derrotas + 1
            elif  str(eleccion_ordenador) == "papel"  :
                 print("ganaste!")
                 number = number + 1
            else: print("empate")
        else: print("error 02 ;c")
        print("número de victorias: " + str(number) + "/10")
        print("número de derrotas: " + str(derrotas))