import re
from collections import Counter
from difflib import get_close_matches
from fuzzywuzzy import fuzz  # Usaremos fuzzywuzzy para comparar las distancias de Levenshtein

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
    "undesirable": "Considerar cambiar 'undesarible' por 'non-preferred'",
    "targeted behaviors": "Considere cambiar 'targeted behaviors' por 'addressed behaviors'",
    "counteracting": "Considera cambiar 'counteracting' por 'addressing'",
    "countering": "Considera cambiar 'countering' por 'addressing'",
    "counteracts": "Considera cambiar 'counteracts' por 'addresses'",
    "counteract": "Considera cambiar 'counteract' por 'address'"
}

# Lista de palabras clave para buscar
palabras_clave = [
    "replacement behavior",
    "replacement behavior programs",
    "planned ignoring in terms of extinction",
    "planned ignoring",
    "desire",
    "undesired",
    "desired items",
    "desire to item",
    "desired behavior",
    "undesirable",
    "desired task",
    "desire to escape",
    "desired attention",
    "she",
    "he",
    "met",
    "desired tangibles",
    "counteract",
    "counteracting",
    "countering",
    "frustration",
    "cope",
    "coping",
    "target",
    "targeting",
    "individual",
    "consumer",
    "student",
    "child",
    "subject",
    "desired activities",
    "provider",
    "targeted"
]

# Función para contar las ocurrencias de las palabras y frases
def contar_palabras_parciales(texto, palabras_buscar):
    texto = texto.lower()  # Convertir el texto a minúsculas
    resultados = {}
    
    # Encontrar las frases completas primero para evitar contar las partes
    frases_completas = [
        "replacement behavior programs",
        "planned ignoring in terms of extinction"
    ]
    
    # Contamos las frases completas primero
    for frase in frases_completas:
        patron = re.compile(rf'\b{re.escape(frase.lower())}\b')
        coincidencias = patron.findall(texto)
        if coincidencias:
            resultados[frase] = len(coincidencias)
            texto = texto.replace(frase.lower(), '')  # Eliminar las coincidencias de las frases completas
    
    # Ahora, para cada palabra clave, buscamos coincidencias exactas y también errores tipográficos
    for palabra in palabras_buscar:
        # Buscar coincidencias exactas
        patron = re.compile(rf'\b{re.escape(palabra.lower())}\b')
        coincidencias = patron.findall(texto)
        
        # Si no encontramos coincidencias exactas, buscamos coincidencias cercanas
        if not coincidencias:
            # Usamos fuzz para comparar distancias de Levenshtein
            palabras_texto = texto.split()
            coincidencias = [w for w in palabras_texto if fuzz.ratio(palabra.lower(), w) > 80]  # Umbral de similitud del 80%
        
        if coincidencias:
            resultados[palabra] = len(coincidencias)
            # Eliminar las palabras encontradas del texto para no contarlas más de una vez
            for coincidencia in coincidencias:
                texto = texto.replace(coincidencia, '')

    return resultados

# Función para obtener la palabra siguiente después de 'he' o 'she'
def obtener_palabra_siguiente(texto, palabra_buscar):
    patron = re.compile(rf'\b{re.escape(palabra_buscar)}\b (\w+)')  # Buscar palabra después de 'he' o 'she'
    coincidencias = patron.findall(texto)
    return coincidencias

# Ejemplo de uso
texto_ejemplo = """
During today's visit to the ABA Center, the client exhibited several maladaptive behaviors influenced by both environmental and situational factors. The client was observed sneezing and coughing, potentially impacting their overall mood and behavior. Among the maladaptive behaviors documented were task refusal, off-task behavior, tantrums, stereotyped behavior, elopement, and self-injurious behavior (SIB). To address these behaviors, the RBT implemented a variety of interventions tailored to each specific maladaptive behavior. For stereotyped behavior, which occurred during downtime and was motivated by automatic reinforcement, the RBT applied differential reinforcement techniques. Elopement incidents arose when the client was asked to wait, leading to escape-motivated behavior; the RBT addressed this with escape extinction and errorless teaching methods. In instances of SIB during free time or recess, characterized by automatic reinforcement, the RBT employed response blocking and redirection strategies. Task refusal was primarily triggered by the introduction of new tasks or activities, driven by an escape function. It was addressed using differential reinforcement of alternative behaviors (DRA) along with the Premack Principle. Off-task behavior, which appeared during transitions from preferred to non-preferred activities, was similarly motivated by escape; it was managed through DRA and redirection. Tantrums emerged when the client was denied access to a wanted item or activity, resulting from a need for tangibles, and were handled through planned ignoring in terms of extinction. To encourage appropriate replacement behavior programs, the RBT utilized strategies like providing the client opportunities to wait for reinforcers as per ABLLS-R A17, engaging in block design activities, following two-step instructions, adhering to stop and go commands, coloring between the lines, seeking approval for task completion (A18), and selecting pictures per ABLLS-R W1, W2, and C17 criteria. Reinforcement in the form of independent playtime with spinning toys and activities in the playground was provided as a reward for demonstrating appropriate behaviors aimed at increasing motivation and encouraging positive conduct. Overall, the session focused on reducing maladaptive behaviors and fostering adaptive behaviors through specialized interventions and reinforcement strategies. The RBT has also collected behavioral data, and the next session is scheduled. No medical or safety concerns arose throughout this visit.
"""

# Obtener los resultados de las palabras encontradas en el texto
resultados = contar_palabras_parciales(texto_ejemplo, palabras_clave)

# Mostrar resultados con sugerencias cuando corresponda
for palabra, conteo in resultados.items():
    salida = f"{palabra}: {conteo}"
    # Si la palabra tiene sugerencia, agregarla
    if palabra in sugerencias:
        salida += f" (Sugerencia: {sugerencias[palabra]})"
    print(salida)
