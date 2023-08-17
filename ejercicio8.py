class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def es_mayor_de_edad(self):
        return self.__edad >= 18
class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad
    
    def get_titular(self):
        return self.__titular
    
    def get_cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        print("Titular:", self.__titular.get_nombre())
        print("Cantidad:", self.__cantidad)
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    
    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad
            
#CuentaJoven hereda de Cuenta y agrega bonificacion
#Get y set son para acceder y modificar

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    def get_bonificacion(self):
        return self.__bonificacion
    
    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    #verifica si el titular es mayor de edad pero menor de 25 años
    def es_titular_valido(self):
        return self.get_titular().es_mayor_de_edad() and self.get_titular().get_edad() < 25
    
    def retirar(self, cantidad): #si el titular es valido, retira
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No se puede retirar dinero. El titular no es válido.")
    
def mostrar(self): #muestra mensaje
    return "Cuenta Joven\n" + f"Bonificación: {self.__bonificacion}%\n" + super().mostrar()

# Ejemplo
persona_joven = Persona("Barbara", 24)
cuenta_joven = CuentaJoven(persona_joven, 500.0, 10)
cuenta_joven.mostrar()
cuenta_joven.ingresar(200.0)
cuenta_joven.retirar(100.0)
cuenta_joven.mostrar()

