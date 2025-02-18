import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página web a analizar
url = "https://www.python.org/downloads/"  # 🔹 Reemplázala con la URL que desees

# Realizar la solicitud HTTP
respuesta = requests.get(url)

# Verificar si la solicitud fue exitosa
if respuesta.status_code == 200:
    # Parsear el contenido HTML de la página
    soup = BeautifulSoup(respuesta.text, 'html.parser')

    # Extraer todos los enlaces
    enlaces = soup.find_all('a')

    # Crear una lista con los datos
    datos = []
    for enlace in enlaces:
        nombre = enlace.text.strip()  # Nombre del enlace
        url_enlace = enlace.get('href')  # URL del enlace
        
        # Verificar que el enlace tenga un URL válido
        if url_enlace:
            datos.append([nombre, url_enlace])

    # Crear un DataFrame de pandas
    df = pd.DataFrame(datos, columns=['Nombre del Enlace', 'URL'])

    # Exportar a un archivo Excel
    nombre_archivo = "enlaces.xlsx"
    df.to_excel(nombre_archivo, index=False, engine='openpyxl')

    # Mostrar los datos en pantalla
    print(df)
    print(f"Archivo Excel '{nombre_archivo}' guardado con éxito.")
    
else:
    print(f"Error al acceder a la página. Código de estado: {respuesta.status_code}")
