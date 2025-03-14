import requests
import time

def verificar_velocidad_conexion(url):
    # Iniciar la medición de tiempo
    inicio = time.time()
    
    try:
        # Realizar la solicitud GET al sitio web
        response = requests.get(url)
        
        # Finalizar la medición de tiempo
        fin = time.time()
        
        # Calcular el tiempo de respuesta
        tiempo_respuesta = fin - inicio
        
        # Imprimir el tiempo de respuesta y el estado de la solicitud
        if response.status_code == 200:
            print(f"La conexión al sitio web {url} fue exitosa.")
            print(f"Tiempo de respuesta: {tiempo_respuesta:.4f} segundos.")
            return tiempo_respuesta
        else:
            print(f"La solicitud no fue exitosa para {url}. Código de estado: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        # Manejar cualquier error que ocurra durante la solicitud
        print(f"Ocurrió un error al intentar conectarse a {url}: {e}")
        return None

def comparar_velocidades(url1, url2):
    print("\nComparando tiempos de respuesta...\n")
    
    # Verificar la velocidad de la primera URL
    tiempo_url1 = verificar_velocidad_conexion(url1)
    
    # Verificar la velocidad de la segunda URL
    tiempo_url2 = verificar_velocidad_conexion(url2)
    
    if tiempo_url1 is not None and tiempo_url2 is not None:
        # Comparar los tiempos de respuesta
        if tiempo_url1 < tiempo_url2:
            print(f"\nLa URL más rápida es {url1} con un tiempo de respuesta de {tiempo_url1:.4f} segundos.")
        elif tiempo_url2 < tiempo_url1:
            print(f"\nLa URL más rápida es {url2} con un tiempo de respuesta de {tiempo_url2:.4f} segundos.")
        else:
            print("\nAmbas URLs tienen el mismo tiempo de respuesta.")
    else:
        print("\nNo se pudieron comparar las URLs debido a un error en la conexión.")

# Reemplaza con las dos URLs que deseas comparar
url1 = "https://www.example.com"
url2 = "https://app.abamatrix.com/oversight"

comparar_velocidades(url1, url2)
