import re
from collections import Counter

# Diccionario con sugerencias para palabras específicas
sugerencias = {
    "desired task": "Considera cambiar 'desired task' por 'preferred task'",
    "desired behavior": "Considera cambiar 'desired behavior' por 'appropriate behavior'",
    "desired behaviors": "Considera cambiar 'desired behaviors' por 'appropriate behavior'",
    "desired items": "Considera cambiar 'desired items' por 'wanted items'",
    "desired item": "Considera cambiar 'desired item' por 'wanted items'",
    "desire to item": "Considera cambiar 'desire to item' por 'want to item'",
    "targeted behaviors": "Considera cambiar 'targeted behaviors' por 'addressed behavior'",
    "desire to escape": "Considera cambiar 'desire to escape' por 'want to escape'",
    "desire for tangibles": "Considere cambiar 'desire for tangibles' por 'want for tangibles'",
    "desired attention": "Considerar cambiar 'desired attention' por 'preferred attention'",
    "undesirable": "Considerar cambiar 'undesarible' por 'non-preferred'",
    "counteracting": "Considera cambiar 'counteracting' por 'addressing'",
    "countering": "Considera cambiar 'countering' por 'addressing'",
    "counteracts": "Considera cambiar 'counteracts' por 'addresses'",
    "counteract": "Considera cambiar 'counteract' por 'address'",
    "targeted interventions": "No es necesario reemplazar 'targeted interventions' o 'targeted intervention'."
}

# Función para contar las ocurrencias de las palabras en el texto
def contar_palabras_parciales(texto, palabras_buscar):
    # Convertir el texto a minúsculas para hacer la búsqueda insensible a mayúsculas
    texto = texto.lower()
    resultados = {}

    # Definir las frases que no deben ser contadas palabra por palabra
    frases_completas = [
        "replacement behavior programs",
        "planned ignoring in terms of extinction",
        "targeted interventions"  # Añadir "targeted interventions" a las frases completas
    ]

    # Contar las frases completas primero para que no se cuenten las partes de ellas
    for frase in frases_completas:
        patron = re.compile(rf'\b{re.escape(frase.lower())}\b')
        coincidencias = patron.findall(texto)
        if coincidencias:
            resultados[frase] = len(coincidencias)
            # Una vez que contamos la frase completa, eliminamos las palabras que la componen
            # Esto asegura que no se cuenten las partes de la frase por separado
            texto = texto.replace(frase.lower(), '')

    # Ahora contar las palabras individuales
    for palabra in palabras_buscar:
        # No contar la palabra "targeted" si ya se ha contado como parte de "targeted interventions"
        if palabra == "targeted" and "targeted interventions" in resultados:
            continue  # Saltamos la palabra "targeted" si ya se contó "targeted interventions"
        
        # No contar las palabras que ya forman parte de una frase completa
        if palabra not in frases_completas:
            patron = re.compile(rf'\b{re.escape(palabra.lower())}\b')  # Para otras palabras, usar delimitadores de palabra
            coincidencias = patron.findall(texto)
            if coincidencias:
                resultados[palabra] = len(coincidencias)
    
    return resultados

texto_ejemplo = input("Ingrese el texto: ")

palabras_buscar = [
    'replacement behavior',
    'replacement behaviors',
    'replacement behavior programs',
    'plannned ignorin',
    'planned ignoring in terms of extinction',
    'desire',
    'undesired',
    'desired items',
    'desire to item',
    'desired behavior',
    'desired behaviors',
    'undesirable',
    'desrired task',
    'desired task',
    'desire to escape',
    'desired attention',
    'she',
    'he',
    'met',  # Solo debe contar cuando sea palabra completa
    'desired tangibles',
    'adaptative',
    'express emotion',
    'counteract',
    'counteracting',
    'countering',
    'frustation',
    'cope',
    'coping',
    'planned ignoring',
    'they',
    'them',
    'their',
    'combat',
    'counter',
    'counteracts',
    'counteract',
    'target',
    'targeted behaviors',
    'targeting',
    'individual',
    'consumer',
    'student',
    'child',
    'subject',
    'desirables activities',
    'undesired',
    'provider',
    'targeted interventions',
    'targeted'
]

# Obtener los resultados de las palabras encontradas en el texto
resultados = contar_palabras_parciales(texto_ejemplo, palabras_buscar)

# Mostrar resultados con sugerencias cuando corresponda
for palabra, conteo in resultados.items():
    salida = f"{palabra}: {conteo}"
    # Si existe una sugerencia para la palabra en el diccionario, agregarla
    if palabra in sugerencias:
        salida += f"  {sugerencias[palabra]}"  # Sugerencia en la misma línea
    print(salida)
