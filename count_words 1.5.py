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
        "desired behaviors",  # Añadimos la frase completa para no contar "desired" por separado
        "desired behavior",
        "targeted interventions",  # Añadimos la frase completa para no contar "targeted" por separado
        "targeted intervention"
    ]

    # Contar las frases completas primero para que no se cuenten las partes de ellas
    for frase in frases_completas:
        patron = re.compile(rf'\b{re.escape(frase.lower())}\b')
        coincidencias = patron.findall(texto)
        if coincidencias:
            resultados[frase] = len(coincidencias)
            # Una vez que contamos la frase completa, eliminamos las palabras que la componen
            # Esto asegura que no se cuenten "desired behavior" o "planned ignoring" por separado
            texto = texto.replace(frase.lower(), '')

    # Ahora contar las palabras individuales
    for palabra in palabras_buscar:
        # Si la palabra es 'he' o 'she' seguida de otra palabra (por ejemplo, 'he wanted')
        if palabra in ['he', 'she']:
            patron = re.compile(rf'\b{re.escape(palabra)}\b \w+')  # Coincidir 'he' o 'she' seguido de cualquier palabra
            coincidencias = patron.findall(texto)
            if coincidencias:
                for coincidencia in coincidencias:
                    palabra_completa = coincidencia.strip()
                    resultados[palabra_completa] = resultados.get(palabra_completa, 0) + 1
            continue
        
        # No contar las palabras que ya forman parte de una frase completa
        if palabra not in ['replacement behavior programs', 'planned ignoring in terms of extinction', 'desired behaviors', 'desired behavior', 'targeted interventions', 'targeted intervention']:
            patron = re.compile(rf'\b{re.escape(palabra.lower())}\b')  # Para otras palabras, usar delimitadores de palabra
            coincidencias = patron.findall(texto)
            if coincidencias:
                resultados[palabra] = len(coincidencias)
    
    return resultados

texto_ejemplo ="""
During today's visit at home, the RBT observed a range of maladaptive behaviors, including task refusal, off-task behavior, tantrums, physical aggression, property destruction, repetitive vocalizations, inappropriate play, stereotyped behavior such as hand flapping, and self-injurious behaviors, particularly hitting and scratching. In response, the RBT implemented several replacement behaviors designed to teach adaptive alternatives. These included requesting attention and breaks, asking for tangibles and help, staying on task, following instructions, making eye contact, sharing items, and accepting "no" as an answer. Also emphasized were toilet training, complying with transition and stop commands, waiting appropriately, and keeping hands at one's sides during idle times. To encourage these replacement behaviors, the RBT used a mix of social and material reinforcements. Social reinforcements like verbal praise and high fives were frequently utilized to affirm positive actions, alongside offering cookies as edible reinforcement and stickers as additional motivational tools. The RBT also applied tailored interventions to specific maladaptive behaviors. For task refusal, which typically occurred during transitions from preferred to non-preferred activities and served as an escape function, strategies such as the Premack Principle and providing choices were employed. To address stereotyped hand-flapping behavior that arose during free time, interventions focused on offering choices and redirecting to alternative responses were used, targeting the sensory needs underlying this behavior. Property destruction triggered by being told to turn off a TV or device was managed through Differential Reinforcement of Alternate Behaviors (DRA) and redirection strategies, addressing the tangible function of this behavior. Tantrums, often incited by being asked to engage in non-preferred tasks, were approached with environmental manipulation and escape-extinction techniques, emphasizing the need to break the cycle of escape-motivated behavior. Lastly, for self-injurious scratching observed during alone time, a combination of DRA, environmental manipulation, and offering choices was employed to provide sensory alternatives and reinforce non-harmful behaviors. Through these targeted interventions and reinforcements, the RBT aimed to decrease maladaptive behaviors while strengthening adaptive skills.

"""

palabras_buscar = [
    'replacement behavior',
    'replacement behaviors',
    'replacement behavior programs',
    'plannned ignorin',
    'planned ignoring in terms of extinction',
    'desire',
    'desires',
    'planned ignore',
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
