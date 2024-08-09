import sys
#leer texto externo
with open("Actividad2\lorem_ipsum.txt", "r") as file:  
    texto=file.read()

#conseguir número de carácteres
caracteres = len(set(texto))  #set() no permite elementos duplicados, len() da la cantidad de elementos sin duplicar

palabras = texto.split()
n_palabras = len(set(palabras))

print(f'El número de carácteres distintos es: {caracteres}')
print(f'El número de palabras distintas es: {n_palabras}')