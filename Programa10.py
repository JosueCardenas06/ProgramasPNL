import os

def buscar_documento(carpeta, nombre_archivo):
    # Lista todos los archivos en la carpeta
    archivos = os.listdir(carpeta)

    # Busca el nombre del documento en la lista de archivos
    if nombre_archivo in archivos:
        print("El documento", nombre_archivo, "ha sido encontrado en la carpeta", carpeta)
    else:
        print("El documento", nombre_archivo, "no ha sido encontrado en la carpeta", carpeta)
        nuevo_nombre = input("Por favor, ingresa otro nombre de archivo: ")
        buscar_documento(carpeta, nuevo_nombre)

# Carpeta donde se encuentra el documento
carpeta = "C:\\Users\\jcard\\OneDrive - Universidad de Colima\\Documentos\\ProgramasPNL"

# Nombre del documento a buscar
nombre_archivo = "Historia.docx"

# Llamada a la función para buscar el documento
buscar_documento(carpeta, nombre_archivo)
