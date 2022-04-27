print("Sistema para calcular el promedio de un alumno.")

name = input("Para comenzar, ¿Cuál es tu nombre?: ")

math_cal = int(input(name + ", ¿Cuál es tu calificación en Matemáticas?: "))
quem_cal = int(input(name + ", ¿Cuál es tu calificación en Química?: "))
phys_cal = int(input(name + ", ¿Cuál es tu calificación en Física?: "))

average = (math_cal + quem_cal + phys_cal) / 3
average = int(average)

if average >= 6:
    result = ' "Aprobaste" '
    print("Felicidades " + name + "," + result + "con un promedio de: " + str(average))

if average < 6:
    result2 = ' "Reprobaste" '
    print(name + "," + result2 + "con un promedio de: " + str(average))

print("Fin.")
