import re
from collections import Counter

# Diccionario con sugerencias para palabras específicas
sugerencias = {
    "desired task": "Considera cambiar 'desired task' por 'preferred task'",
    "desired behavior": "Considera cambiar 'desired behavior' por 'appropriate behavior'",
    "desired items": "Considera cambiar 'desired items' por 'wanted items'",
    "desired item": "Considera cambiar 'desired item' por 'wanted items'",
    "desire to item": "Considera cambiar 'desire to item' por 'want to item'",
    "desire to escape": "Considera cambiar 'desire to escape' por 'want to escape'",
    "desire for tangibles": "Considere cambiar 'desire for tangibles' por 'want for tangibles'",
    "desired attention": "Considerar cambiar 'desired attention' por 'preferred attention'",
    "targeted behaviors": "Considere cambiar 'targeted behaviors' por 'addressed behaviors'",
    "counteracting": "Considera cambiar 'counteracting' por 'addressing'",
    "countering": "Considera cambiar 'countering' por 'addressing'",
    "counteracts": "Considera cambiar 'counteracts' por 'addresses'",
    "counteract": "Considera cambiar 'counteract' por 'address'"
}

def contar_palabras_parciales(texto, palabras_buscar):
    # Convertir el texto a minúsculas para hacer la búsqueda insensible a mayúsculas
    texto = texto.lower()
    resultados = {}

    for palabra in palabras_buscar:
        # Si la palabra es 'he' o 'she', usamos los límites de palabra para que solo se cuenten como palabras completas
        if palabra in ['he', 'she']:
            patron = re.compile(rf'\b{re.escape(palabra.lower())}\b')
        elif palabra == "met":
            # Para "met", solo contar como palabra completa, no como parte de otra palabra
            patron = re.compile(rf'\b{re.escape(palabra)}\b')
        else:
            # Para otras palabras, seguimos con la búsqueda de coincidencias parciales
            patron = re.compile(rf'{re.escape(palabra.lower())}')
        
        # Encontrar todas las coincidencias
        coincidencias = patron.findall(texto)
        
        # Almacenar el conteo si hay coincidencias
        if coincidencias:
            resultados[palabra] = len(coincidencias)
    
    return resultados

# Función para obtener la palabra siguiente después de 'he' o 'she'
def obtener_palabra_siguiente(texto, palabra_buscar):
    patron = re.compile(rf'\b{re.escape(palabra_buscar)}\b (\w+)')  # Buscar palabra después de 'he' o 'she'
    coincidencias = patron.findall(texto)
    return coincidencias

# Ejemplo de uso
texto_ejemplo = """
Services were delivered at a previously agreed time, with Ramzi, the teacher, and RBT present at the client's school. The BCBA implemented various instructional approaches, including Discrete Trial Training (DTT), Functional Communication Training (FCT), Incidental Teaching, and Errorless Teaching. Adjustments were made to the current protocol during the therapy session. The modifications included changing materials, identifying triggers or discriminative stimuli, and introducing preventive strategies by manipulating antecedents to decrease tantrum behaviors. Direct observation was used to evaluate treatment integrity. During this visit, the RBT received supervision from the BCBA, who provided direct observation throughout the treatment. The objectives of the supervision included active direction of the RBT during services to ensure proper implementation and fidelity of procedures, supervisory discussion and feedback, covering items from the BACB Task List, and observing the RBT's interaction with the client. The following items from the BACB Task List were revised: preparing for data collection, entering data and updating graphs, reporting variables that might affect the client in a timely manner, and maintaining client dignity. The overall evaluation for today was "Satisfactory," and supervisory feedback was provided to the supervisor. The lead analyst completed probing of the programs, maintaining eye contact, and responding to peer play initiation, showing difficulties for Ramzi in initiating a conversation or game when given directions by a peer. He required modeling from the RBT with a maximum time of 20 seconds of interaction. Highly preferred reinforcers were used for the training of this program later to evaluate progression after at least one week of training. The supervisor developed performance expectations for the supervisee and observed the provision of behavioral skills training. The analyst guided the development of problem-solving and ethical decision-making skills and evaluated the effects of supervision and behavior-analytic processes. No environmental changes or medical or safety concerns were noted throughout the session. Data were collected following the existing service plan.
"""

palabras_buscar = [
    'replacement behavior',
    'desire',
    'undesired',
    'desired items',
    'desire to item',
    'desired behavior',
    'undesirable',
    'desrired task',
    'desired task',
    'desire to escape',
    'desired attention',
    'she',
    'he',
    'met',
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
    'targeting',
    'individual',
    'consumer',
    'student',
    'child',
    'subject',
    'desirables activities',
    'undesired',
    'provider',
    'targeted'
]

# Obtener los resultados de las palabras encontradas en el texto
resultados = contar_palabras_parciales(texto_ejemplo, palabras_buscar)

# Mostrar resultados con sugerencias cuando corresponda
for palabra, conteo in resultados.items():
    if palabra in ['he', 'she']:
        # Obtener la palabra siguiente y mostrar en el formato solicitado
        palabras_siguientes = obtener_palabra_siguiente(texto_ejemplo, palabra)
        for siguiente in palabras_siguientes:
            salida = f"{palabra} {siguiente}: {conteo}"
            print(salida)
    else:
        salida = f"{palabra}: {conteo}"
        # Si la palabra tiene sugerencia, agregarla
        if palabra in sugerencias:
            salida += f" (Sugerencia: {sugerencias[palabra]})"
        print(salida)
