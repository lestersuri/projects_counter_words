import requests
from bs4 import BeautifulSoup
import pandas as pd




def obtener_contenido_html(url):
    """Obtiene el contenido HTML de la página."""
    response = requests.get(url)
    return response.content

def extraer_datos_html(soup, etiqueta, clase=None):
    """Extrae los textos de una etiqueta específica."""
    if clase:
        elementos = soup.find_all(etiqueta, class_=clase)
    else:
        elementos = soup.find_all(etiqueta)
    return [elemento.get_text() for elemento in elementos]


def guardar_datos_excel(data, nombre_archivo='datos_extraidos.xlsx', vista_previa=True, limite_vista=10):
    """Guarda los datos extraídos en un archivo Excel y muestra una vista previa."""
    
    # Crear DataFrame con los datos extraídos
    df = pd.DataFrame(data, columns=['Título'])
    
    # Mostrar vista previa de los datos antes de exportar
    if vista_previa:
        print("\nVista previa de los datos extraídos:")
        print(df.head(limite_vista))  # Muestra las primeras filas
    
    # Exportar a Excel
    df.to_excel(nombre_archivo, index=False, engine='openpyxl')
    print(f"\n¡Exportación exitosa! Los datos se han guardado en {nombre_archivo}")






def main(url, etiqueta='h2', clase=None, nombre_archivo='datos_extraidos.xlsx'):
    """Función principal que orquesta la extracción y exportación de datos."""
    # Obtener el contenido HTML de la página
    html = obtener_contenido_html(url)
    
    # Parsear el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    # Extraer los datos
    data = extraer_datos_html(soup, etiqueta, clase)
    # Guardar los datos extraídos en un archivo Excel
    guardar_datos_excel(data, nombre_archivo)




# URL de la página a extraer (cámbiala a la que necesitas)
url = "https://app.abamatrix.com/oversight"

# Llamar a la función principal
main(url)
