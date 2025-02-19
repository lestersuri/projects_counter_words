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
    "express emotions": "Considera cambiar 'express emotions' por 'internal events'",
    "desire for tangibles": "Considere cambiar 'desire for tangibles' por 'want for tangibles'",
    "desire tangibles": "Considere cambiar 'desired tangibles' por 'preferred tangibles'",
    "desired attention": "Considerar cambiar 'desired attention' por 'preferred attention'",
    "undesirable": "Considerar cambiar 'undesarible' por 'non-preferred'",
    "undesired": "Considere cambiar 'undesired' por 'inappropriate'",
    "counteracting": "Considera cambiar 'counteracting' por 'addressing'",
    "desired items": "Considera cambiar 'desired item' por 'wanted item'",
    "desired outcomes": "Considera cambiar 'desired outcomes' por 'appropriate outcomes'",
    "desired outcome": "Considera cambiar 'desired outcome' por 'appropriate outcome'",
    "countering": "Considera cambiar 'countering' por 'addressing'",
    "counteracts": "Considera cambiar 'counteracts' por 'addresses'",
    "counteract": "Considera cambiar 'counteract' por 'address'",
    "target": "Considera cambiar 'target' por 'address or manage'",
    "cope": "Considera cambiar 'cope' por 'manage or self-regulate'",
    "coping": "Considera cambiar 'coping' por 'self-regulating'",
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
During today's visit at home, the RBT worked diligently to address and improve various maladaptive behaviors observed in the client. The maladaptive behaviors identified included task refusal, tantrums, disruptive behaviors, verbal aggression, socially inappropriate behaviors, and elopement. To address these behaviors, a range of replacement behavior programs were implemented by the RBT. These included fostering compliance with non-preferred activities, encouraging self-management of verbal responses, ensuring tasks were completed within the given time frame, and promoting the completion of house chores. Additionally, the client was guided to engage in appropriate social interactions, ask for help or clarification, provide correct answers, accept corrective feedback, and manage expectations when situations did not go as planned. The RBT also encouraged the client to obtain permission before borrowing items, complete hygiene activities independently, and maintain healthy habits. The RBT utilized skill acquisition programs specifically addressing the reduction of disruptive behaviors, promotion of socially acceptable behaviors, following instructions from multiple caregivers, cooperation and rule-following in various locations, as well as taking appropriate action to deal with and report any wrongdoing by others. Positive reinforcements, such as the use of an iPad, phone, card games, playtime with a turtle or a cat, verbal praise, word games, and bubbles, were employed to encourage and sustain appropriate behaviors. In particular, the RBT applied several interventions tailored to the specific maladaptive behaviors encountered. For disruptive behaviors, which typically occurred during transitions from preferred to non-preferred activities and were driven by the function of escape, the RBT divided complex activities into smaller, manageable steps and reduced task demands. To address tantrums, which were often triggered by a lack of attention, the RBT employed strategies like planned ignoring in terms of extinction and Differential Reinforcement of Other Behaviors (DRO) to refocus attention on positive behaviors. When faced with socially inappropriate behaviors resulting from restricted access to items or activities, the RBT utilized extinction techniques and if/then statements to manage and redirect these behaviors effectively. Overall, today's visit was rich in strategic interventions and positive reinforcements, aiming to decrease maladaptive behaviors and enhance skill acquisition in a home setting.
"""
palabras_buscar = [
    'replacement behavior',
    'replacement behaviors',
    'replacement behavior programs',
    'plannned ignorin',
    'planned ignoring in terms of extinction',
    'express emotion',
    'express emotions',
    'expressed emotions',
    'unwarranted',
    'desired tangibles',
    'desire',
    'desires',
    'desired outcomes',
    'desired outcome',
    'planned ignore',
    'undesired',
    'desired items',
    'desired item',
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
# Imprimir la línea de inicio solo una vez
print("********************************************")
print()  # Espacio entre la línea de inicio y la primera salida
print()
print()

# Iterar sobre los resultados
for palabra, conteo in resultados.items():
    salida = f"{palabra}: {conteo}"
    
    # Si existe una sugerencia para la palabra en el diccionario, agregarla
    if palabra in sugerencias:
        salida += f"  {sugerencias[palabra]}"  # Sugerencia en la misma línea
    
    print(salida)
    print("-----------------------------")

# Imprimir la línea final
print()
print()
print()
print("********************************************")
