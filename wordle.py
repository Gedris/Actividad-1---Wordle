

import random 
import linecache
import time

f = open("diccionario.txt", "r")
print("Nivel de dificultad: \n" "- FACIL (5 letras) presiona 1 \n" "- MEDIO (6 letras) presiona 2 \n" "- DIFICIL (7 letras) presiona 3") 
modo = int(input("Selecciona un modo de dificultad: "))


if (modo == 1):
    start = time.perf_counter()
    palabra = linecache.getline("diccionario.txt",random.randint(1,80383))
    while len(palabra) != 6:
        palabra = linecache.getline("diccionario.txt",random.randint(1,80383))
        palabra = palabra.lower()
    print(palabra)
    
    palabraIngresada = ""

    while palabraIngresada != palabra:
        palabraIngresada = str(input("ingrese palabra: "))
        if len(palabraIngresada) != 5:
             while len(palabraIngresada) != 5:
                print("LA PALABRA DEBE SER DE 5 LETRAS")
                palabraIngresada = str(input("ingrese palabra: "))
        
        palabraIngresada = palabraIngresada.lower()
        comparativa = ["", "", "", "", ""]
        i = 1
        for i in range (len(palabra)):
            if palabraIngresada[i-1] == palabra[i-1]:
                comparativa[i-1] = "="
            elif palabraIngresada[i-1] in palabra:
                comparativa[i-1] = "-"
            else:
                comparativa[i-1] = " "
            i += 1
        

        print(palabraIngresada[0], " ", palabraIngresada[1], " ", palabraIngresada[2], " ", palabraIngresada[3], " ", palabraIngresada[4])
        print(comparativa[0], " ", comparativa[1], " ", comparativa[2], " ", comparativa[3], " ", comparativa[4])
        if comparativa == ["=","=","=","=","="]:
            print("ganaste!!  gg")
            end = round(time.perf_counter()) 
            end = round(end - start)
            print("Tardaste ", end, " segundos en terminar el juego")
            break

elif (modo == 2):
    start = time.perf_counter()
    palabra = linecache.getline("diccionario.txt",random.randint(1,80383))
    while len(palabra) != 7:
        palabra = linecache.getline("diccionario.txt",random.randint(1,80383))
        palabra = palabra.lower()
    print(palabra)
    
    palabraIngresada = ""


    while palabraIngresada != palabra:
        palabraIngresada = str(input("ingrese palabra: "))
        if len(palabraIngresada) != 6:
             while len(palabraIngresada) != 6:
                 print("LA PALABRA DEBE TENER 6 LETRAS")
                 palabraIngresada = str(input("ingrese palabra: "))
        
        palabraIngresada = palabraIngresada.lower()
        comparativa = ["", "", "", "", "",""]
        i = 1
        for i in range (len(palabra)):
            if palabraIngresada[i-1] == palabra[i-1]:
                comparativa[i-1] = "="
            elif palabraIngresada[i-1] in palabra:
                comparativa[i-1] = "-"
            else:
                comparativa[i-1] = " "
            i += 1


        print(palabraIngresada[0], " ", palabraIngresada[1], " ", palabraIngresada[2], " ", palabraIngresada[3], " ", palabraIngresada[4], " ", palabraIngresada[5])
        print(comparativa[0], " ", comparativa[1], " ", comparativa[2], " ", comparativa[3], " ", comparativa[4], " ", comparativa[5])
        if comparativa == ["=","=","=","=","=","="]:
            print("ganaste!!  gg")
            end = round(time.perf_counter()) 
            end = round(end - start)
            print("Tardaste ", end, " segundos en terminar el juego")
            break

elif (modo == 3):
    start = time.perf_counter()
    palabra = linecache.getline("diccionario.txt",random.randint(1,80383))
    while len(palabra) != 8:
        palabra = linecache.getline("diccionario.txt",random.randint(1,80383))
        palabra = palabra.lower()
    print(palabra)
    
    palabraIngresada = ""


    while palabraIngresada != palabra:
        palabraIngresada = str(input("ingrese palabra: "))
        if len(palabraIngresada) != 7:
            while len(palabraIngresada) != 7:
                print("LA PALABRA DEBE SER DE 7 LETRAS")
                palabraIngresada = str(input("ingrese palabra: "))
        
        palabraIngresada = palabraIngresada.lower()
        comparativa = ["", "", "", "", "","",""]
        i = 1
        for i in range (len(palabra)):
            if palabraIngresada[i-1] == palabra[i-1]:
                comparativa[i-1] = "="
            elif palabraIngresada[i-1] in palabra:
                comparativa[i-1] = "-"
            else:
                comparativa[i-1] = " "
            i += 1

        print(palabraIngresada[0], " ", palabraIngresada[1], " ", palabraIngresada[2], " ", palabraIngresada[3], " ", palabraIngresada[4], " ", palabraIngresada[5], " ", palabraIngresada[6])
        print(comparativa[0], " ", comparativa[1], " ", comparativa[2], " ", comparativa[3], " ", comparativa[4], " ", comparativa[5], " ", comparativa[6])
        if comparativa == ["=","=","=","=","=","=","="]:
            print("ganaste!!  gg")
            end = round(time.perf_counter()) 
            end = round(end - start)
            print("Tardaste ", end, " segundos en terminar el juego")
            break
else:
    print("No existe esa dificultad")