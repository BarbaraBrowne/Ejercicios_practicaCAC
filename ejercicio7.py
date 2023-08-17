#Cuenta atrib privados
class cuenta
def __init__(self, titular="", cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad    

#get para acceder
def get_titular(self):
        return self.__titular
    
def get_cantidad(self):
        return self.__cantidad   
    
#muestra los datos de la cuenta. 
       
def mostrar(self):
        print("Titular:", self.__titular.get_nombre())
        print("Cantidad:", self.__cantidad)
    
def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    
def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad
# ingresar y retirar dejan modificar la cantidad, pero no permiten valores negativos

# Ejemplo
class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

persona = Persona("Barbara")
cuenta = Cuenta(persona, 1000.0)

cuenta.mostrar()
cuenta.ingresar(500.0)
cuenta.retirar(200.0)

cuenta.mostrar()




