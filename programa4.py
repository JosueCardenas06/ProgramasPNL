import nltk
nltk.download()

archivo_nombre="cuento.txt"

with open(archivo_nombre,"r") as archivo:
    texto=archivo.read()
tokens=nltk.word_tokenize(texto,"spanish")
for token in tokens:
    print(token)

print('--------------------------')
#Aqui nuestra lista de token se llama tokens
palabras_total=len(tokens)
print(palabras_total)
print("-------------------------------------------------------------------")
