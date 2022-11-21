#Proyecto2 - Segunda parte/funciones lambda
#Teoría de la computación 
#Autor: Mariana David, Fredy Velazquez, Angel Higueros 
#Carnet: 201055, 201011, 20963


#importaciones 
import os
import functions
#from functions import sucesor, suma, multiplicacion, potencia, alfa_beta

#menu 
def menu():

    #Funcion que limpia pantalla
    #os.system('cls')
    print ("\n Seleccione la opción del ejercicio que desea ejecutar")
    print ("1. Ejemplo con sucesor")
    print ("2. Ejemplo con suma")
    print ("3. Ejemplo con multiplicación")
    print ("4. Ejemplo con potencia")
    print ("5. Salir")

while True: 
    menu()

    opcionMenu = input("\nInserte un valor numérico para seleccionar la opcion: ")
    if opcionMenu == "1":
        resultado = functions.sucesor()
    elif opcionMenu == "2":
        resultado = functions.suma()
    elif opcionMenu == "3":
        resultado = functions.multiplicacion()
    elif opcionMenu == "4":
        resultado = functions.potencia()
    elif opcionMenu == "5":
        print("¡Usted ha salido exitosamente!")
        break
    else:
        print ("")
        input("ERROR: Inserto un valor incorrecto. Pulse una tecla para continuar: ")