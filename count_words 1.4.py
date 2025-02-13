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
    "desire to escape": "Considera cambiar 'desire to escape' por 'want to escape'",
    "desire for tangibles": "Considere cambiar 'desire for tangibles' por 'want for tangibles'",
    "desired attention": "Considerar cambiar 'desired attention' por 'preferred attention'",
    "undesirable": "Considerar cambiar 'undesarible' por 'non-preferred'",
    "targeted behaviors": "Considere cambiar 'targeted behaviors' por 'addressed behaviors'",
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
        "planned ignoring in terms of extinction"
    ]

    # Contar las frases completas primero para que no se cuenten las partes de ellas
    for frase in frases_completas:
        patron = re.compile(rf'\b{re.escape(frase.lower())}\b')
        coincidencias = patron.findall(texto)
        if coincidencias:
            resultados[frase] = len(coincidencias)
            # Una vez que contamos la frase completa, eliminamos las palabras que la componen
            # Esto asegura que no se cuenten "replacement behavior" o "planned ignoring" por separado
            texto = texto.replace(frase.lower(), '')

    # Ahora contar las palabras individuales
    for palabra in palabras_buscar:
        # Si la palabra es 'targeted' y está seguida de 'interventions' o 'intervention'
        if palabra == 'targeted':
            patron = re.compile(rf'\b{re.escape(palabra)}\b \b(interventions|intervention)\b')
            coincidencias = patron.findall(texto)
            if coincidencias:
                # Contar la ocurrencia de "targeted interventions" o "targeted intervention"
                resultados['targeted interventions'] = len(coincidencias)  # Usamos 'targeted interventions' como clave final
                # No realizar más acciones sobre 'targeted' porque ya fue contada correctamente
                continue

        # No contar las palabras que ya forman parte de una frase completa
        if palabra not in ['replacement behavior programs', 'planned ignoring in terms of extinction']:
            patron = re.compile(rf'\b{re.escape(palabra.lower())}\b')  # Para otras palabras, usar delimitadores de palabra
            coincidencias = patron.findall(texto)
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
During the school visit, the RBT observed several maladaptive behaviors exhibited by the client, including throwing objects, tantrums, elopement, and task refusal. To address these behaviors, the RBT implemented several replacement behavior programs designed to foster more appropriate responses. For example, the client was encouraged to stop leisure activities when asked, share or take turns obtaining preferred items, and accept the removal of access to certain items by an authority figure. Furthermore, the client was taught to transition from preferred activities to required tasks, to wait after requesting gradually increasing periods, and to complete single-response tasks during one-on-one instruction and therapy. Functional Communication Training was also utilized, specifically to encourage the client to ask for assistance appropriately and to seek attention appropriately. As part of the reinforcement strategy, social reinforcements such as verbal praise, "Good job," and high fives were provided to encourage and reinforce positive behaviors. The RBT applied targeted interventions to manage the maladaptive behaviors. For instance, tantrums, which often arose when attention was given to others, were addressed using Differential Reinforcement of Alternative behaviors (DRA) for attention-motivated behaviors. Task refusal, typically triggered by being asked to perform a task, was managed through DRA for behaviors maintained by escape, focusing on helping the client complete tasks to avoid avoidance-related behaviors. In dealing with throwing objects, an intervention involving Non-contingency Reinforcement for escape was applied, aimed at preventing the client from becoming overwhelmed when asked to work. Finally, for behaviors related to elopement, which tended to occur during transitions from preferred to non-preferred activities, the RBT again utilized DRA for behaviors maintained by escape to encourage more constructive responses. Overall, the visit was structured to guide the client towards more adaptive behaviors, employing a combination of reinforcement, teaching replacement behavior programs, and specific interventions addressing the functions of maladaptive behaviors.




"""

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
    salida = f"{palabra}: {conteo}"
    # Si existe una sugerencia para la palabra en el diccionario, agregarla
    if palabra in sugerencias:
        salida += f"  {sugerencias[palabra]}"  # Sugerencia en la misma línea
    print(salida)
