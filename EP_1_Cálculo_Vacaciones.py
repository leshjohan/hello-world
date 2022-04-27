print("================================")
print("Sistema de cálculo de vacaciones")
print("================================\n")

nombre = input("Para comenzar, por favor introduce tu nombre: ")

años = float(input(nombre + ", indica la cantidad de años de servicio: "))

clave = input("Muy bien, " + nombre + ", ahora introduce la clave de tu departamento: ")

if clave == "clave1":
    if años == 1 and años < 2:
        print(nombre, ", tienes derecho a 6 días de vacaciones.")
    elif años >= 2 and años <= 6:
        print(nombre, ", tienes derecho a 14 días de vacaciones.")
    elif años >= 7:
        print(nombre, ", tienes derecho a 20 días de vacaciones.")
    else:
        print(nombre, ", no tienes derecho a días de vacaciones.")

elif clave == "clave2":
    if años == 1 and años < 2:
        print(nombre, ", tienes derecho a 7 días de vacaciones.")
    elif años >= 2 and años <= 6:
        print(nombre, ", tienes derecho a 15 días de vacaciones.")
    elif años >= 7:
        print(nombre, ", tienes derecho a 22 días de vacaciones.")
    else:
        print(nombre, ", no tienes derecho a días de vacaciones.")

elif clave == "clave3":
    if años == 1 and años < 2:
        print(nombre, ", tienes derecho a 7 días de vacaciones.")
    elif años >= 2 and años <= 6:
        print(nombre, ", tienes derecho a 20 días de vacaciones.")
    elif años >= 7:
        print(nombre, ", tienes derecho a 30 días de vacaciones.")
    else:
        print(nombre, ", no tienes derecho a días de vacaciones.")

else:
    print("Lo sentimos, la clave introducida no se encuentra registrada. Por favor, intente nuevamente.")
