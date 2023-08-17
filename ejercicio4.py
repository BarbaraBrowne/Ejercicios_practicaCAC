

def contar_palabras(cadena):
    palabras = cadena.split()
    contador = {}
    
    for palabra in palabras:
        palabra = palabra.lower()
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
            
    return contador

def palabra_mas_repetida(diccionario):
    palabra_max = None
    frecuencia_max = 0
    
    for palabra, frecuencia in diccionario.items():
        if frecuencia > frecuencia_max:
            palabra_max = palabra
            frecuencia_max = frecuencia
            
    return (palabra_max, frecuencia_max)


cadena_ejemplo = "La verdad solo se puede encontrar en un lugar el codigo"
diccionario = contar_palabras(cadena_ejemplo)
palabra_repetida, frecuencia_repetida = palabra_mas_repetida(diccionario)

print("Diccionario de frecuencias:", diccionario)
print("Palabra más repetida:", palabra_repetida)
print("Frecuencia:", frecuencia_repetida)
# La función contar_palabras toma cadena y devuelve un diccionario con frecuencia de cada palabra. 
# La función palabra_mas_repetida toma el diccionario generado y devuelve una tupla con la palabra más repetida y su frecuencia.