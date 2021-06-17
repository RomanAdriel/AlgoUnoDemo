""". Dada una serie de nombres y salarios respectivos, determinar el salario máximo,
el mínimo y la persona que percibe cada uno. No se deben guardar todos los
datos. """

empleado_max = ""
sueldo_max = 0
empleado_min = ""
sueldo_min = 0
sueldo = 0
nombre_empleado = ""


while sueldo != -1:

    sueldo = int(input("ingresar el salario del empleado: "))
    if sueldo != -1:
        nombre_empleado = input("ingrese nombre de empleado: ")

        if sueldo >= sueldo_max:
            sueldo_max = sueldo
            empleado_max = nombre_empleado

        elif sueldo < sueldo_min:
            sueldo_min = sueldo
            empleado_min = nombre_empleado

    else:
        sueldo = -1


print("El empleado con mayor salario es: ", empleado_max, " y cobra: ", sueldo_max)
print("El empleado con menor salario es: ", empleado_min, " y cobra: ", sueldo_min)
