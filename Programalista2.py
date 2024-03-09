archivo_nombre="hola.txt"
with open(archivo_nombre, "r") as archivo:
    lineas_lista=archivo.readlines()
num_linea=1
for linea in lineas_lista:
    print("num_linea ",num_linea," : ",linea)
    num_linea=num_linea+1
    