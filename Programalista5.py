import nltk
from nltk.tokenize import word_tokenize
from nltk.text import Text

nltk.download('punkt')
nltk.download('cess_esp')  # Descargar el corpus para español (opcional, según necesidades)

archivo_nombre = "cuento.txt"

with open(archivo_nombre, "r", encoding="utf-8") as archivo:
    texto = archivo.read()

# Tokenización y creación del objeto Text
tokens = word_tokenize(texto, "spanish")
texto_nltk = Text(tokens)

# Riqueza léxica
riqueza_lexica = len(set(texto_nltk)) / len(texto_nltk)

print("Riqueza léxica del texto:", riqueza_lexica)
