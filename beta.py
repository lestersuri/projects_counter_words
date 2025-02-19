import re
from collections import Counter


class WordSuggestion:
    def __init__(self):
        self.sugerencias = {
            "desired task": "Considera cambiar 'desired task' por 'preferred task'",
            "desired behavior": "Considera cambiar 'desired behavior' por 'appropriate behavior'",
            "desired behaviors": "Considera cambiar 'desired behaviors' por 'appropriate behavior'",
            "desired items": "Considera cambiar 'desired items' por 'wanted items'",
            "desired item": "Considera cambiar 'desired item' por 'wanted item'",
            "desire to item": "Considera cambiar 'desire to item' por 'want to item'",
            "targeted behaviors": "Considera cambiar 'targeted behaviors' por 'addressed behavior'",
            "desire to escape": "Considera cambiar 'desire to escape' por 'want to escape'",
            "express emotions": "Considera cambiar 'express emotions' por 'internal events'",
            "desire for tangibles": "Considere cambiar 'desire for tangibles' por 'want for tangibles'",
            "desire tangibles": "Considere cambiar 'desired tangibles' por 'preferred tangibles'",
            "desired attention": "Considerar cambiar 'desired attention' por 'preferred attention'",
            "undesirable": "Considerar cambiar 'undesirable' por 'non-preferred'",
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

    def get_suggestion(self, word):
        return self.sugerencias.get(word, None)


class WordCounter:
    def __init__(self, text, word_list, suggestions):
        self.text = text.lower()
        self.word_list = word_list
        self.suggestions = suggestions

    def count_word_occurrences(self):
        results = {}
        phrases_to_ignore = [
            "replacement behavior programs",
            "planned ignoring in terms of extinction",
            "desired behaviors",
            "desired behavior",
            "targeted interventions",
            "targeted intervention"
        ]

        # Count complete phrases first (to avoid counting parts of phrases)
        for phrase in phrases_to_ignore:
            pattern = re.compile(rf'\b{re.escape(phrase.lower())}\b')
            matches = pattern.findall(self.text)
            if matches:
                results[phrase] = len(matches)
                # Remove matched phrases from text to avoid counting parts of the phrase
                self.text = self.text.replace(phrase.lower(), '')

        # Now count individual words
        for word in self.word_list:
            if word not in phrases_to_ignore:
                # Buscar la palabra con delimitadores de palabras
                pattern = re.compile(rf'\b{re.escape(word.lower())}\b')
                matches = pattern.findall(self.text)
                if matches:
                    results[word] = len(matches)

        return results


class WordCountProcessor:
    def __init__(self, text, word_list):
        self.text = text
        self.word_list = word_list
        self.suggestions = WordSuggestion()
        self.counter = WordCounter(self.text, self.word_list, self.suggestions)

    def process(self):
        # Count word occurrences
        results = self.counter.count_word_occurrences()

        # Output the results with suggestions
        print("********************************************")
        print()
        print()


        for word, count in results.items():
            output = f"{word}: {count}"
            suggestion = self.suggestions.get_suggestion(word)
            if suggestion:
                output += f"  {suggestion}"
            print(output)
            print("-----------------------------")
         
            
        print()
        print()
        print("********************************************")


# Example usage
texto_ejemplo = """
Durante la visita de hoy al Centro ABA, desired, desire, desired item , targeted interventions el enfoque fue evaluar y mejorar las habilidades conductuales y comunicativas del cliente a través de la implementación de la Evaluación de Habilidades Básicas de Lenguaje y Aprendizaje (ABLLS-R). La sesión observó múltiples comportamientos desadaptativos, incluyendo fuga, comportamiento autolesivo (SIB) y rechazo de tareas. Para abordar estos comportamientos, el analista modeló una variedad de programas de comportamientos sustitutos, con el objetivo de desarrollar habilidades más adaptativas. Estos programas de comportamientos sustitutos incluyeron enseñar al cliente a esperar un refuerzo, aceptar el "no" como respuesta, seguir un horario de actividades, transitar entre actividades, permanecer en tareas y compartir elementos pidiéndolos. Además, el analista trabajó en fomentar habilidades como actividades competitivas, solicitar atención y acercarse cuando se requiere una respuesta para reforzamiento. El cliente también practicó caminar junto a un cuidador para minimizar los incidentes de fuga. Para abordar comportamientos desadaptativos específicos, se modelaron varias estrategias de intervención. Para el rechazo de tareas, donde el cliente intentaba escapar de completar una tarea, se emplearon el principio de Premack y técnicas de redirección. En casos de comportamiento autolesivo durante situaciones donde se retuvieron demandas, se combinó el bloqueo de respuestas de menos de 15 segundos con redirección para mitigar el comportamiento. Para la fuga, que ocurría durante transiciones entre áreas con una función subyacente de obtener atención, el analista utilizó bloqueo de respuestas, redirección y Refuerzo Diferencial de Comportamientos Incompatibles (DRI). El analista también enfatizó la importancia de la generalización y mantenimiento de estas habilidades en diferentes entornos y con distintos individuos. Este enfoque asegura que las habilidades adquiridas sean robustas y transferibles más allá del entorno estructurado de la terapia. A lo largo de la visita, no estuvo presente ningún Técnico de Conducta Registrado (RBT), lo que se señaló como un cambio ambiental. En general, la sesión estuvo enfocada en mejorar la capacidad del cliente para funcionar de manera adaptativa e independiente, reduciendo la ocurrencia de comportamientos desadaptativos mientras se fomentaban habilidades efectivas de comunicación e interacción.
"""

palabras_buscar = [
    'replacement behavior',
    'replacement behaviors',
    'replacement behavior programs',
    'plannned ignoring',
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

# Initialize the processor and process the text
processor = WordCountProcessor(texto_ejemplo, palabras_buscar)
processor.process()
