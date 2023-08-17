cadena = "La verdad solo se puede encontrar en un lugar el codigo"

# Dividir la cadena en palabras
palabras = cadena.split()

# Crear un diccionario para contar las repeticiones
contador = {}
for palabra in palabras:
    palabra = palabra.lower()  # Convertir a minúsculas para evitar diferencias de mayúsculas y minúsculas
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

# Imprimir el diccionario de repeticiones
for palabra, contador_repeticiones in contador.items():
    print(f'Palabra: {palabra}, Repeticiones: {contador_repeticiones}')