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
            patron = re.compile(rf'\b{re.escape(palabra.lower())}\b(\s+\w+)')
        elif palabra == "met":
            # Para "met", solo contar como palabra completa, no como parte de otra palabra
            patron = re.compile(rf'\b{re.escape(palabra)}\b')
        else:
            # Para otras palabras, seguimos con la búsqueda de coincidencias parciales
            patron = re.compile(rf'{re.escape(palabra.lower())}')
        
        # Encontrar todas las coincidencias
        coincidencias = patron.findall(texto)
        
        # Almacenar el conteo y las palabras siguientes si hay coincidencias
        if coincidencias:
            if palabra not in resultados:
                resultados[palabra] = {'count': 0, 'following_words': []}
            for match in coincidencias:
                # Contamos la aparición de la palabra
                resultados[palabra]['count'] += 1
                # Si es 'he' o 'she', almacenamos la palabra que sigue
                if match:
                    resultados[palabra]['following_words'].append(match.strip())
    
    return resultados

# Ejemplo de uso
texto_ejemplo = """
During today's visit to the school, the RBT worked diligently to address several maladaptive behaviors observed in Ramzi, who was also experiencing an environmental change by participating in a field trip to Urban Air. The maladaptive behaviors displayed included tantrums, elopement, property destruction, self-injury through head banging, self-scratching, task refusal behavior, and isolation. To counter these behaviors, a variety of replacement behaviors were implemented by the RBT. These included teaching Ramzi to request a break, ask for attention, and engage in alternative activities when a preferred one was denied. Ramzi was also encouraged to respond appropriately when told to stop, request permission to exit a situation, and follow instructions both in a group and as one-step commands. Maintaining eye contact for five seconds when prompted, returning or initiating greetings, engaging in brief conversational skills, and demonstrating compliance with simple, non-preferred tasks were also part of the intervention strategies.Specific interventions were applied by the RBT targeting particular maladaptive behaviors. For isolation, it was observed as a response to the antecedent of a community outing and served the escape function. Ramzi moved away (more than 2 feet) or turns back from people interacting with him. It also included avoiding eye contact during social interaction. The RBT used behavioral momentum, blocking, and antecedent environmental manipulation as intervention strategies. In cases of task refusal behavior, notably when the individual was asked to wait, the function was escape. Ramzi signaled "No" by shaking his head or saying “No”, or when he turns his back on a task or demand. Interventions used included blocking, delay of reinforcers, and antecedent manipulation. To reinforce positive behaviors, the RBT used both social and edible reinforcements. Social reinforcements included high fives and verbal praise, while edible reinforcements involved providing ICEE and fruit snacks as treats. Throughout the session, the RBT's approaches aimed to create a supportive environment, fostering a sense of safety and encouraging Ramzi to adopt more adaptive behaviors in the face of change and challenge.


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
for palabra, info in resultados.items():
    # Mostrar el conteo de la palabra
    salida = f"{palabra}: {info['count']}"
    
    # Si la palabra tiene sugerencia, agregarla
    if palabra in sugerencias:
        salida += f" (Sugerencia: {sugerencias[palabra]})"
    
    # Si la palabra es 'he' o 'she', agregar las palabras siguientes con el formato "palabra siguiente: 1"
    if palabra in ['he', 'she']:
        for following_word in info['following_words']:
            salida += f" - {palabra} {following_word}: 1"
    
    # Imprimir la salida
    print(salida)
