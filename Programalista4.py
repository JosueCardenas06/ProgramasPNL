carpeta_nombre=("C:\\Users\\jcard\\OneDrive - Universidad de Colima\\Documentos\\Actividades\\")
arhivo_nombre="escuela.txt"

with open(carpeta_nombre+arhivo_nombre,"r") as archivo:
    texto=archivo.read()

simbolos=["(",")",",",".",";",":","\""]

for simbolo in simbolos:
    texto=texto.replace(simbolo," " + simbolo + " ")

palabras_lista=texto.split()
palabras_lista.sort()
for palabra in palabras_lista:
    print(palabra)
    