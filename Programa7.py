import re

carpeta_nombre = "C:\\Users\\jcard\\OneDrive - Universidad de Colima\\Documentos\\Actividades\\"
archivo_nombre = "cuento.txt"

with open(carpeta_nombre + archivo_nombre, "r") as archivo:
    texto = archivo.read()

expresion_regular = re.compile(r"...? ")

resultados_busqueda = expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))