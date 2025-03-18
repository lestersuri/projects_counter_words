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
    "tackled": "Considera cambiar 'tackled' por 'addressed'",
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
During today's visit to the school, the RBT observed a range of maladaptive behaviors displayed by the client, including tantrums, being off task, elopement, property destruction, and inappropriate play. In response, the RBT implemented a variety of replacement behavior programs to help guide the client towards more acceptable actions. These replacement behavior programs included gestures for 'yes' and 'no,' adjusting clothing properly, using the potty, accepting transitions between activities, taking 'no' for an answer, using toys appropriately according to her design, agreeing to have tangibles removed, requesting by indicating (tact), and accepting help. The RBT utilized different categories of reinforcements to encourage the client's positive behavior. Non-edible reinforcements included engaging items like kinetic sand, magnets, play-doh, dolls, paint, coloring books, bubbles, and access to a tablet. Social reinforcements such as applause, verbal praise, and high fives were also provided to reward and motivate the client. To address the maladaptive behaviors specifically, the RBT applied targeted interventions. For elopement, which occurred during transitions from preferred to non-preferred activities with an escape function, interventions included antecedent manipulation, response blocking, and redirection. Inappropriate play, driven by sensory needs in the absence of demands, was managed using functional communication training, redirection, and providing choices. Property destruction, associated with escape from non-preferred tasks, was addressed through antecedent manipulation, response blocking, and redirection. The off-task behavior, triggered by being denied access to a preferred item or activity for tangible reasons, was mitigated using behavioral momentum, the Premack Principle, and redirection. Lastly, tantrums related to being asked to put something away were handled with functional communication training, the Premack Principle, and the offering of choices. Overall, the RBT's strategic application of replacement behavior programs, reinforcements, and specific interventions aimed to reduce maladaptive behaviors and promote positive engagement during the school visit."""

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
    'therapist',
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
