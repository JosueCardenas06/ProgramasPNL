import fitz  # PyMuPDF
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

# Función para extraer texto de un archivo PDF
def extraer_texto_pdf(nombre_archivo):
    texto = ""
    with fitz.open(nombre_archivo) as doc:
        for pagina in doc:
            texto += pagina.get_text()
    return texto

# Función para realizar análisis de texto con NLTK
def analizar_texto(texto):
    # Convertir texto a minúsculas
    texto = texto.lower()

    # Tokenizar el texto
    palabras = word_tokenize(texto)

    # Contar las palabras totales
    total_palabras = len(palabras)

    # Calcular la distribución de frecuencia
    distribucion_frecuencia = FreqDist(palabras)

    # Obtener las palabras que aparecen una sola vez
    palabras_unicas = distribucion_frecuencia.hapaxes()

    # Graficar las 20 palabras más comunes
    distribucion_frecuencia.plot(20, cumulative=False)

    # Mostrar las palabras que aparecen una sola vez
    print("Palabras que aparecen una sola vez:", palabras_unicas)

    # Mostrar el total de palabras
    print("Total de palabras:", total_palabras)

# Nombre del archivo PDF
nombre_archivo = "C:\\Users\\jcard\\OneDrive - Universidad de Colima\\Documentos\\ProgramasPNL\\Investigacion.pdf"

# Extraer texto del archivo PDF
texto_pdf = extraer_texto_pdf(nombre_archivo)

# Realizar análisis de texto con NLTK
analizar_texto(texto_pdf)

# Mostrar el gráfico de las 20 palabras más comunes
plt.show()
