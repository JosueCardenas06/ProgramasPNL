import nltk
from nltk.tokenize import word_tokenize
from nltk.text import Text
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

# Descargar los recursos necesarios de NLTK
nltk.download('punkt')
# nltk.download('cess_esp') # Descargar el corpus para español si es necesario

# Se asume que el archivo 'cuento.txt' está en el directorio actual
archivo_nombre = "cuento.txt"

with open(archivo_nombre, "r", encoding="utf-8") as archivo:
    texto = archivo.read()

# Tokenización del texto
tokens = word_tokenize(texto, "spanish")

# Creación del objeto Text de NLTK
texto_nltk = Text(tokens)

# Creación de la distribución de frecuencia
distribucion = FreqDist(texto_nltk)

# Mostrar las 10 palabras más comunes
print("Las 10 palabras más comunes en el texto son:", distribucion.most_common(10))

# Visualización de la frecuencia de las 30 palabras más comunes
distribucion.plot(30, title="Frecuencia de las 30 palabras más comunes")

# Frecuencia de una palabra específica
# Ajusta 'palabra_especifica' al término cuya frecuencia te interese
palabra_especifica = 'casa'
frecuencia_palabra = distribucion[palabra_especifica]
print(f"La frecuencia de la palabra '{palabra_especifica}' en el texto es:", frecuencia_palabra)
