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
    "desired items": "Considera cambiar 'desired item' por 'preferred item'",
    "desired outcomes": "Considera cambiar 'desired outcomes' por 'appropriate outcomes'",
    "desired outcome": "Considera cambiar 'desired outcome' por 'appropriate outcome'",
    "desired tangibles": "Considerar cambiar 'desired tangibles' por 'preferred tangibles'",
    "desired tangible": "Considerar cambiar 'desired tangible' por 'preferred tangible'",
    "desirable behaviors": " Considerar cambiar 'desirable behaviors' por 'appropriate behaviors' ",
    "desirable behavior": " Considerar cambiar 'desirable behavior' por 'appropriate behavior' ",
    "desirable": " Considerar cambiar 'desirable' por 'appropriate' ",
    "countering": "Considera cambiar 'countering' por 'addressing'",
    "counteracts": "Considera cambiar 'counteracts' por 'addresses'",
    "countered": "Considera cambiar 'countered' por 'addressed'",
    "counteract": "Considera cambiar 'counteract' por 'address'",
    "counter": "Considera cambiar 'counter' por 'address'",
    "target": "Considera cambiar 'target' por 'address or manage'",
    "cope": "Considera cambiar 'cope' por 'manage or self-regulate'",
    "coping": "Considera cambiar 'coping' por 'self-regulating'",
    "combat": "Considera cambiar 'combat' por 'address'",
    "they": "They: Pronombre sujeto (realiza la acción): Ejemplo: They are studying. (Ellos/Ellas están estudiando.). Ejemplo: I think they will enjoy the movie. (Creo que ellos/ellas disfrutarán de la película).",
    "their": "Their: Pronombre posesivo (pertenece a ellos/as): Ejemplo: Their house is big. (Su casa es grande.)  I like their style.(Me gusta su estilo.)",
    "them": "Them: Pronombre objeto (recibe la acción): Ejemplo: I saw them. (Los vi.). I gave them the book. (Les di el libro.).Significa que se usa cuando 'ellos' o 'ellas' son el objeto de la acción. Es el equivalente de 'los/las' o 'a ellos/a ellas'. Ejemplo: I saw them at the park.(Los vi en el parque.)'",  
    "tackling": "Considera cambiar 'tackling' por 'addressing'",
    "targeted interventions": "No es necesario reemplazar 'targeted interventions' o 'targeted intervention'.",
    "targeted": "It is recommended to use 'addressed' instead of targeted when 'addressed' is used to describe behaviors or issues that have been dealt with."

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
During today's visit at home, the RBT observed several maladaptive behaviors exhibited by Allen, including tantrums, pushing others, throwing objects, physical aggression, elopement, self-injury behaviors (SIB), throwing himself on the floor, and playing with saliva. To address these behaviors, the RBT implemented various replacement behaviors. For instance, Allen was guided to request tangibles and activities appropriately using manding, learn to accept "no," and wait for tangibles or activities for 5 seconds. Other strategies included helping Allen comply with transitions using a daily visual schedule, keeping his shoes on, remaining seated while engaging in a preferred activity, and playing with toys as intended. Additionally, Allen was encouraged to initiate and reciprocate greetings, use a chewing necklace when attempting to play with saliva, walk next to an adult while holding hands, and wait 5 seconds for attention. The skill acquisition programs focused on teaching Allen to approach when a response is required for reinforcement, attend to his name, follow instructions in routine situations, perform enjoyable actions following instructions, wait for 5 seconds without touching stimuli, and seek approval upon task completion. To motivate Allen, social reinforcement through verbal praise and slime were used as rewards. Regarding interventions, two specific maladaptive behaviors were addressed. When Allen threw himself on the floor, which typically occurred at the beginning of activities and served the function of escape, the RBT applied interventions like redirection and used if/then statements. Additionally, when Allen had tantrums when asked to put something away, indicating a desire for tangibles, the RBT used redirection along with the Premack Principle to manage the behavior. Overall, today's session involved tackling various behavioral challenges while emphasizing the development of more adaptive skills and strategies for Allen.


"""

















palabras_buscar = [
    'replacement behavior',
    'replacement behaviors',
    'replacement behavior programs',
    'replace program',
    'replace programs',
    'plannned ignorin',
    'planned ignoring in terms of extinction',
    'express emotion',
    'express emotions',
    'expressed emotions',
    'unwarranted',
    'desired tangibles',
    'desire',
    'desires',
    'desired',
    'desired outcomes',
    'desired outcome',
    'desirable behaviors',
    'desirable behavior',
    'desirable',
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
    'desired tangibles',
    'desired tangigle',
    'she',
    'he',
    'met',  # Solo debe contar cuando sea palabra completa
    'desired tangibles',
    'adaptative',
    'express emotion',
    'counteract',
    'counteracting',
    'countered',
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
    'customer',
    'receipt',
    'student',
    'child',
    'subject',
    'observer',
    'desirables activities',
    'undesired',
    'provider',
    'targeted interventions',
    'tackled',
    'tackling',
    'tackle',
    'targeted'
]

def top_bottomn(n):
    for _ in range(n):
        print()


# Obtener los resultados de las palabras encontradas en el texto
resultados = contar_palabras_parciales(texto_ejemplo, palabras_buscar)

# Mostrar resultados con sugerencias cuando corresponda
# Imprimir la línea de inicio solo una vez
print("********************************************")
top_bottomn(4)

# Iterar sobre los resultados
for palabra, conteo in resultados.items():
    salida = f"{palabra}: {conteo}"
    
    # Si existe una sugerencia para la palabra en el diccionario, agregarla
    if palabra in sugerencias:
        salida += f"  {sugerencias[palabra]}"  # Sugerencia en la misma línea
    
    print(salida)
    print("-----------------------------")

# Imprimir la línea final
top_bottomn(4)
print("********************************************")
