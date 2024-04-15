import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

# URL de la página a hacer scraping
url = 'https://www.wikipedia.org/'

# Realizar la solicitud HTTP
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontrar todo el texto dentro de las etiquetas <p>, <h1>, <h2>, <h3>, <h4>, <h5>, <h6> y <a>
    texto = ' '.join([p.get_text() for p in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a'])])
    
    # Eliminar caracteres no alfabéticos y convertir a minúsculas
    texto_limpio = re.sub(r'[^a-zA-Z\s]', '', texto).lower()
    
    # Dividir el texto en palabras
    palabras = texto_limpio.split()
    
    # Contar las palabras
    contador_palabras = Counter(palabras)
    
    # Imprimir las palabras y su conteo
    for palabra, conteo in contador_palabras.items():
        print(f'{palabra}: {conteo}')
else:
    print('Error al cargar la página:', response.status_code)
