#Iterativa

def get_int():
    while True:
        try:
            valor = int(input("Ingresa un valor entero: "))
            return valor
        except ValueError:
            print("El valor ingresado no es un entero válido. Intenta de nuevo.")

# Ejemplo
entero = get_int()
print("Valor entero ingresado:", entero)



#recursiva

def get_int_recursivo():
    try:
        valor = int(input("Ingresa un valor entero: "))
        return valor
    except ValueError:
        print("El valor ingresado no es un entero válido. Intenta de nuevo.")
        return get_int_recursivo()

# Ejemplo
entero = get_int_recursivo()
print("Valor entero ingresado:", entero)