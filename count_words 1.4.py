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
        if palabra not in ['replacement behavior programs', 'planned ignoring in terms of extinction']:
            patron = re.compile(rf'\b{re.escape(palabra.lower())}\b')  # Para otras palabras, usar delimitadores de palabra
            coincidencias = patron.findall(texto)
            if coincidencias:
                resultados[palabra] = len(coincidencias)
    
    return resultados

# Ejemplo de uso
texto_ejemplo = """
During today's home visit, the RBT observed a series of maladaptive behaviors and implemented targeted interventions various interventions to address them. The maladaptive behaviors displayed included Tantrums, Elopement, Property Destruction, Self-Injury with head banging, Self-Scratching, Task Refusal Behavior, and Isolation. To foster positive behavior changes, the RBT introduced several replacement behavior programs. These included prompting Ramzi to request a break, request attention, engage in an alternative activity when denied a preferred one, and respond appropriately when told to "Stop." The RBT also encouraged Ramzi to request permission to exit, follow instructions in a group, adhere to one-step instructions, and maintain eye contact for 5 seconds when prompted. Additionally, the RBT worked on social skills by initiating and returning greetings, engaging in conversational skills such as keeping their body facing a peer or adult during a two-way conversation for no more than one minute and complying with simple non-preferred tasks for no more than two minutes. Other replacement behavior programs included manding for items or activities, requesting help, requesting a delay of transition, responding to peer play-initiation statements, and playing with peers with prompting for at least five minutes. The RBT applied specific interventions to address particular maladaptive behaviors. For Task Refusal Behavior, where the antecedent was being asked to work, and the function was identified as an escape. Ramzi would signal "No" by shaking his head or saying "No" when the client turned his back on a task or demand. The RBT applied Antecedent Manipulation, Blocking, and Behavioral Momentum. In cases of Elopement, triggered by being given a task to complete, with the function being escape. Ramzi would take off or walk outside a designated/supervised area without adult permission for any duration of time. The RBT implemented Blocking and Antecedent Environmental Manipulation. When addressing Tantrums, they would occur when attention was not given as wanted. Ramzi would engage in crying, yelling, and throwing self on the floor. The RBT applied Behavioral Momentum, Antecedent Manipulation, and Blocking to redirect the behavior toward more positive outcomes. To reinforce positive behaviors, the RBT utilized various reinforcements categorized as Edible, Non-Edible, and Social. Edible reinforcements included Skittles and fruit snacks, while Non-Edible reinforcements consisted of playtime with a trampoline, the use of an iPad, and access to books. Social reinforcement was provided through verbal praise. Overall, the RBT employed a structured approach to mitigate maladaptive behaviors while encouraging the development of appropriate replacement behavior programs, using a combination of reinforcements and targeted interventions to facilitate positive behavioral change during the visit."""

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
