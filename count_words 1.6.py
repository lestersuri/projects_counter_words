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
    "countering": "Considera cambiar 'countering' por 'addressing'",
    "counteracts": "Considera cambiar 'counteracts' por 'addresses'",
    "countered": "Considera cambiar 'countered' por 'addressed'",
    "counteract": "Considera cambiar 'counteract' por 'address'",
    "target": "Considera cambiar 'target' por 'address or manage'",
    "cope": "Considera cambiar 'cope' por 'manage or self-regulate'",
    "coping": "Considera cambiar 'coping' por 'self-regulating'",
    "combat": "Considera cambiar 'combat' por 'address'",
    "they": "They: Pronombre sujeto (realiza la acción): Ejemplo: They are studying. (Ellos/Ellas están estudiando.). Ejemplo: I think they will enjoy the movie. (Creo que ellos/ellas disfrutarán de la película).",
    "their": "Their: Pronombre posesivo (pertenece a ellos/as): Ejemplo: Their house is big. (Su casa es grande.)  I like their style.(Me gusta su estilo.)",
    "them": "Them: Pronombre objeto (recibe la acción): Ejemplo: I saw them. (Los vi.). I gave them the book. (Les di el libro.).Significa que se usa cuando 'ellos' o 'ellas' son el objeto de la acción. Es el equivalente de 'los/las' o 'a ellos/a ellas'. Ejemplo: I saw them at the park.(Los vi en el parque.)",  
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
During today's home visit, the RBT observed a range of maladaptive behaviors exhibited by the client, including tantrums, disruptive behaviors, off-task instances, elopement, inappropriate social interactions, task refusal, topic preservation, and verbal confrontation. In response, the RBT implemented a variety of replacement behaviors to address these issues. These included strategies such as delay of reinforcement, encouraging time on-task, teaching the acceptance of losing in games, and assisting with the giving up of requested items. Other efforts focused on improving social skills, such as responding to stop-and-go cues, accepting corrective feedback, using an appropriate tone of voice, and following a visual schedule with daily routines. Furthermore, the sessions aimed to promote task completion, appropriate requests for breaks, and staying seated during activities. The RBT also carried out skill acquisition programs, introducing the client to skills like waiting for their turn during conversations, identifying community signals related to ADL/safety, walking next to a caregiver by holding hands, and working independently. Reinforcement for positive behaviors was provided using edibles such as popcorn and M&M's. To tackle specific maladaptive behaviors, targeted interventions were applied. For disruptive behaviors exhibited by the client resulting because attention was not given at the time he wanted because the caregiver was busy, a Differential Reinforcement of Alternate Behaviors (DRA)  was used to shift the client's focus and counter the attention-seeking function. Off-task behavior observed when the client was working on a puzzle activity, motivated by an escape function, was managed using a most-to-least prompt fading technique. Inappropriate social interactions exhibited by the client during a conversation, seeking attention, were managed using redirection.T ask refusal behaviors exhibited by the client in response to being given a task to complete were addressed through the provision of choices as intervention, managing the escape function. For elopement, which occurred when the client was asked to pick up their room,  representing an escape function, extinction was used as the intervention strategy. During incidents of tantrums exhibited by the client, which were driven by the attention given to another person, Functional Communication Training (FCT) was utilized. Verbal confrontation behaviors exhibited by the client with a family member while playing electronic games seeking attention were managed using Differential Reinforcement of Other Behaviors (DRO) to prioritize alternative positive behaviors. For topic preservation behaviors exhibited by the client while the caregiver conversed with others in the room, redirection was used to counter attention-seeking function. Overall, the RBT strategically addressed the client's maladaptive behaviors while encouraging positive behaviors through well-structured interventions, replacement behavior programs, and skill acquisition programs. No medical or safety issues occurred during the visit. The next visit will take place on Sunday the 23rd.





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
    'desirable behaviors',
    'desirable behavior',
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
    'student',
    'child',
    'subject',
    'desirables activities',
    'undesired',
    'provider',
    'targeted interventions',
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
