print("***********************************************************************")
print("Programa para determinar ¿Cuál es el número más grande de tres números?")
print("***********************************************************************")

num1 = int(input("\nIntroduce el primer número: "))
num2 = int(input("\nIntroduce el segundo número: "))
num3 = int(input("\nIntroduce el tercer número: "))

if num1 > num2 and num1 > num3:
    print("\nEl número ", num1, " es el número más grande de los tres.")
elif num2 > num1 and num2 > num3:
    print("\nEl número ", num2, " es el número más grande de los tres.")
elif num3 > num1 and num3 > num2:
    print("\nEl número ", num3, " es el número más grande de los tres.")
else:
    print("\nLos números introducidos son iguales")
