import requests
from bs4 import BeautifulSoup

# URL de la página a hacer scraping
url = 'https://www.youtube.com/'

# Realizar la solicitud HTTP
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Ejemplo: obtener todos los enlaces de la página
    enlaces = soup.find_all('a')
    
    # Imprimir los enlaces encontrados
    for enlace in enlaces:
        print(enlace.get('href'))
else:
    print('Error al cargar la página:', response.status_code)
