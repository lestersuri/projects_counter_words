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
During the school visit today, the RBT observed various maladaptive behaviors exhibited by the client. Notable behaviors included property destruction, tantrums, physical aggression, non-compliance, elopement, spitting, inappropriate social behaviors, self-injurious behavior (SIB), and stereotypy. These behaviors were addressed through several targeted replacement behavior programs to teach the client constructive and adaptive responses. Specifically, the RBT focused on helping the client to escape by effectively asking for a break, mand using single words, accepting alternative items, complying with instructions within 15 seconds, staying on task for at least three minutes with prompts, respecting personal space and boundaries, maintaining eye contact with adults for 10 seconds while receiving instructions, remaining in designated areas, keeping hands appropriately during work and free time, and requesting help when necessary. To address the specific maladaptive behaviors, the RBT applied various interventions. For property destruction, which typically occurred when asked to work and seemed to serve an escape function, interventions included interruption and redirection, delaying reinforcers, and antecedent environmental manipulation. Tantrums, often triggered by transitions from preferred to non-preferred activities with escape as the function, were managed through functional communication training and a delay of reinforcers. Physical aggression, which also stemmed from an escape function when given tasks to complete, was addressed through antecedent environmental manipulation and delaying reinforcers. Non-compliance, often seen when the client was asked to work, was also managed by delaying reinforcers and employing if/then statements. Elopement, typically triggered when asked to complete non-preferred tasks and functioning as an escape mechanism, was mitigated using functional communication training along with antecedent environmental manipulation. Spitting, another escape-motivated behavior, was managed through antecedent environmental manipulation. To curb inappropriate social behaviors, particularly in the presence of specific individuals that served an attention-seeking function, the RBT utilized antecedent environmental manipulation and functional communication training. Self-injurious behaviors and stereotypy were observed in both preferred and non-preferred activities with a sensory function; these were addressed through intervention strategies such as interruption and redirection. Notably, stereotypy was more prevalent in outdoor or brightly lit environments, informing the nuanced approach taken by the RBT to address its sensory-driven nature.




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
