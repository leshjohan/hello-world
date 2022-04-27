print("=========")
print("Conversor")
print("=========\n")
print("Menú de opciones: \n")

print("Presiona 1 para convertir de números a palabras.")
print("Presiona 2 para convertir de palabras a números. \n")

opcion = int(input("¿Cuál es la opción deseada?: "))

if opcion == 1:
    print("\n Conversor de números a palabras \n")

    num_pal = int(input("¿Cuál es el número que deseas convertir a palabra?: "))

    if num_pal == 1 :
        print("El número es 'Uno'")
    elif num_pal == 2 :
        print("El número es 'Dos'")
    elif num_pal == 3 :
        print("El número es 'Tres'")
    elif num_pal == 4 :
        print("El número es 'Cuatro'")
    elif num_pal == 5 :
        print("El número es 'Cinco'")
    else :
        print("El número indicado no está registrado.")

elif opcion == 2 :
    print("\n Conversor de palabras a números. \n")
    
    pal_num = str(input("¿Cuál es la palabra que deseas convertir a número?: "))
    pal_num = pal_num.lower()
    
    if pal_num == "uno" :
        print("El número es '1'")
    elif pal_num == "dos" :
        print("El número es '2'")
    elif pal_num == "tres" :
        print("El número es '3'")
    elif pal_num == "cuatro" :
        print("El número es '4'")
    elif pal_num == "cinco" :
        print("El número es '5'")
    else :
        print("La palabra indicada no está registrada.")

else :
    print("La opción seleccionada no está disponible.")

print("Fin.")
