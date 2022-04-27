print("Calculadora con una sola variable\n")

print("********************")
print("* Menú de opciones *")
print("********************")

print("1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. División entera\n6. Exponente\n7. Resto o residuo\n")

variable = int(input("Introduce la opción deseada: "))

if variable == 1:
    
    print("Elegiste suma\n")
    variable = int(input("Introduce el primer número: "))
    variable += int(input("Introduce el segundo número: "))
    print("El resultado de la suma es: ", variable)
    
elif variable == 2:

    print("Elegiste resta\n")
    variable = int(input("Introduce el primer número: "))
    variable -= int(input("Introduce el segundo número: "))
    print("El resultado de la resta es: ", variable)

elif variable == 3:
    
    print("Elegiste multiplicación\n")
    variable = int(input("Introduce el primer número: "))
    variable *= int(input("Introduce el segundo número: "))
    print("El resultado de la multiplicación es: ", variable)
    
elif variable == 4:

    print("Elegiste división\n")
    variable = int(input("Introduce el primer número: "))
    variable /= int(input("Introduce el segundo número: "))
    print("El resultado de la división es: ", variable)
    
elif variable == 5:
    
    print("Elegiste división entera\n")
    variable = int(input("Introduce el primer número: "))
    variable //= int(input("Introduce el segundo número: "))
    print("El resultado de la división es: ", variable)
    
elif variable == 6:

    print("Elegiste Exponente\n")
    variable = int(input("Introduce el primer número: "))
    variable **= int(input("Introduce el segundo número: "))
    print("El resultado de la potencia es: ", variable)
    
elif variable == 7:
    
    print("Elegiste resto o residuo\n")
    variable = int(input("Introduce el primer número: "))
    variable %= int(input("Introduce el segundo número: "))
    print("El resultado del resto o residuo es: ", variable)
    
else:
    print("La opción seleccionada no está disponible.")


