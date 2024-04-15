import nltk
import matplotlib.pyplot as plt

carpeta_nombre = "C:\\Users\\jcard\\OneDrive - Universidad de Colima\\Documentos\\Actividades\\"
archivo_nombre = "cuento.txt"

with open(carpeta_nombre + archivo_nombre, "r") as archivo:
    texto = archivo.read()
print("----------------------------------------------------------------------")
tokens = nltk.word_tokenize(texto, "spanish")

tokens_conjunto = set(tokens)
palabras_totales = len(tokens)
palabras_diferentes = len(tokens_conjunto)
print(palabras_totales)
print(palabras_diferentes)
texto_nltk = nltk.Text(tokens)
distribucion = nltk.FreqDist(texto_nltk)
print("----------------------------------------------------------------------")
hapaxes = distribucion.hapaxes()
for hapax in hapaxes:
    print(hapax)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
distribucion.plot(cumulative=True)
plt.subplot(1, 2, 2)
distribucion.plot(40, cumulative=True)
plt.show()
