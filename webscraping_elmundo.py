import requests
from bs4 import BeautifulSoup

# URL de la página principal de El Mundo
url = 'https://www.elmundo.es/'

# Hacer la solicitud HTTP a la página
response = requests.get(url)

# Verificar que la solicitud fue exitosa (código 200)
if response.status_code == 200:
    # Parsear el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar todos los elementos <h2> con la clase "ue-c-cover-content__headline"
    titulares = soup.find_all('h2', class_='ue-c-cover-content__headline')

    # Imprimir cada titular
    for i, titular in enumerate(titulares):
        print(f"TITULAR {i}: {titular.get_text()}")
else:
    print(f"Error al acceder a la página: {response.status_code}")
