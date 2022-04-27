print("Introduce dos números a comparar: \n")

num_one = int(input("Introduce el primer número: "))
num_two = int(input("Introduce el segundo número: \n"))

print("Los números a comparar son: ", num_one, "y", num_two, "\n")

if num_one != num_two:
    print("Es diferente...")

    if num_one > num_two:
        print("Es mayor...")

        if num_one >= num_two:
            print ("Es mayor o igual...")

    elif num_one < num_two:
        print ("Es menor...")

        if num_one <= num_two:
            print("Es menor o igual...")

    else:
        print("Ha ocurrido un problema. Por favor, intente nuevamente.")

elif num_one == num_two :
    print ("Es igual...")

    if num_one > num_two:
        print("Es mayor...")

    elif num_one >= num_two:
            print ("Es mayor o igual...")

    elif num_one < num_two:
        print ("Es menor...")
    
    elif num_one <= num_two:
            print ("Es menor o igual...")

    
