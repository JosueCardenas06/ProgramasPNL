# Definimos la lista de tokens
tokens = ["este", "es", "un", "ejemplo", "de", "lista", "de", "tokens", "del", "cual", "del"]

#Aqui, nuestra lista de tokens se llama "tokens"

conteo_individual=tokens.count("del")
print(conteo_individual)

palabras_totales1=len(tokens)
porcentaje=100*conteo_individual/palabras_totales1

print(porcentaje, "%")
