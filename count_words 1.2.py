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
    "counteract": "Considera cambiar 'counteract' por 'address'"
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
        # No contar las palabras que ya forman parte de una frase completa
        if palabra not in ['replacement behavior programs', 'planned ignoring in terms of extinction']:
            # Si la palabra es "met", usamos delimitadores de palabra \b para asegurarnos que no se cuente como parte de otras palabras
            if palabra == "met":
                patron = re.compile(rf'\b{re.escape(palabra.lower())}\b')  # Buscar 'met' solo como palabra completa
            else:
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
During today's visit to the ABA Center, the RBT observed maladaptive behaviors that included physical aggression and climbing. In response to these behaviors, the RBT implemented specific replacement behavior programs to modify the client's response in challenging situations. To address the presence of objects in the client's mouth, the RBT encouraged the behavior of handing out items upon request, and to manage impulse control and safety, the client was trained to wait next to a caregiver. For reinforcement, the RBT used the client's favorite toy as a motivational tool, categorized under "Other," to encourage the adoption of positive replacement behavior programs and to reduce reliance on maladaptive responses. The RBT applied targeted interventions for each maladaptive behavior observed. In the case of climbing, which appeared to occur without demands and seemed to serve a sensory function, the RBT used redirection as an intervention strategy. This involved guiding the client towards more appropriate activities or locations to fulfill his sensory needs without climbing. Regarding episodes of physical aggression, which were triggered when the client was denied access to a preferred outing, the RBT inferred the function to be tangible. In dealing with these aggressive behaviors, the RBT interrupted the behavior using physical guidance to prevent escalation and to ensure the safety of all parties involved. Today's visit focused on identifying triggers and functions of maladaptive behaviors while diligently applying reinforcement and interventions to promote adaptive skills and reduce the impact of challenging behaviors.


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
