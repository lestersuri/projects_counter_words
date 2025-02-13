import re
import json
import os

# Función para contar las coincidencias de las palabras
def contar_palabras_parciales(texto, palabras_buscar):
    texto = texto.lower()
    resultados = {}

    for palabra in palabras_buscar:
        patron = re.compile(rf'{re.escape(palabra.lower())}')
        coincidencias = patron.findall(texto)

        # Verificación de las coincidencias encontradas
        if coincidencias:
            resultados[palabra] = len(coincidencias)
        else:
            # Si no se encuentra la palabra, imprimir que no se encontró
            print(f"No se encontraron coincidencias para: '{palabra}'")

    return resultados

# Función para cargar el texto desde un archivo
def cargar_texto(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {archivo}")
        return ""

# Función para cargar las palabras y sugerencias desde un archivo JSON
def cargar_palabras_json(archivo_json):
    try:
        with open(archivo_json, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {archivo_json}")
        return {}

def main():
    # Obtener el directorio actual del script
    dir_actual = os.path.dirname(os.path.realpath(__file__))

    # Rutas predefinidas para el archivo de texto y el archivo JSON
    archivo_texto = "texto.txt"  # Asegúrate de que este archivo esté en el mismo directorio que el script
    archivo_json = "palabras.json"  # Asegúrate de que este archivo esté en el mismo directorio que el script

    # Construir las rutas completas de los archivos
    archivo_texto_completo = os.path.join(dir_actual, archivo_texto)
    archivo_json_completo = os.path.join(dir_actual, archivo_json)

    # Cargar el texto desde el archivo
    texto = cargar_texto(archivo_texto_completo)
    
    # Verificación de que el archivo de texto se cargó correctamente
    if not texto:
        print("El archivo de texto está vacío o no se cargó correctamente.")
        return
    
    # Cargar las palabras y sugerencias desde el archivo JSON
    sugerencias = cargar_palabras_json(archivo_json_completo)
    
    # Verificación de que el archivo JSON se cargó correctamente
    if not sugerencias:
        print("El archivo JSON está vacío o no se cargó correctamente.")
        return
    
    # Obtener las palabras a buscar desde las claves del diccionario
    palabras_buscar = list(sugerencias.keys())

    # Obtener los resultados de las palabras encontradas en el texto
    resultados = contar_palabras_parciales(texto, palabras_buscar)

    # Verificar si se encontraron resultados
    if not resultados:
        print("No se encontraron coincidencias en el texto.")
    else:
        # Mostrar resultados con sugerencias cuando corresponda
        for palabra, conteo in resultados.items():
            salida = f"{palabra}: {conteo}"

            # Si la palabra tiene una sugerencia, agregarla
            if palabra in sugerencias:
                salida += f" (Sugerencia: {sugerencias[palabra]})"
            
            print(salida)

if __name__ == '__main__':
    main()
