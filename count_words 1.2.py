import re
from collections import Counter

# proyecto vinculado a git

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
During today's visit, the session took place at a community center following a caregiver's request, intending to evaluate the client's behavior in the new environment and to help the client engage in various community classes in the future (depending on the client's response). The analyst conducted assessments using the ABC Data Recording Chart and the VB-MAPP Assessment to observe and measure the client's behaviors. Several maladaptive behaviors were observed, including off-task behavior, inappropriate touching of others, non-compliance, vocal stereotypes, elopement, and touching private parts in front of others. To address these behaviors, the participants implemented targeted interventions, evaluating their effectiveness. For off-task behavior associated with delayed access to tangibles, interventions included Differential Reinforcement of Alternative Behaviors (DRA) and Tangible Extinction. For non-compliance in response to non-preferred tasks, strategies incorporated DRA, escape independent response delivery or mini-breaks, and extinction. Inappropriate touching of others was addressed with attention-independent response delivery (NCR) and DRA, addressing the function of gaining attention when adults or caregivers spoke to others. Vocal stereotypes during downtime triggered by automatic reinforcement were approached using DRA. Concerning touching private parts when others were nearby for attention, interventions executed involved DRA, attention extinction, and NCR techniques. The analyst also modeled various replacement behavior programs, such as maintaining appropriate physical proximity to peers and adults, politely manding to stop undesirable activities, following complex instructions, and engaging in communicative exchanges through tacting and labeling. The client was also guided to participate in sustained entertainment activities without maladaptive behaviors, to communicate likes and dislikes, and to keep their area organized. Additionally, protocol modifications were made with the introduction of a visual schedule to help the client manage the novel setting and activities more effectively, aiming to enhance their adaptability and reduce anxiety in this new environment.





"""

palabras_buscar = [
    'replacement behavior',
    'replacement behavior programs',
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
