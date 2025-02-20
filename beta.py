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
            "they": "They: Pronombre sujeto (realiza la acción): Ejemplo: They are studying. (Ellos/Ellas están estudiando.). Ejemplo: I think they will enjoy the movie. (Creo que ellos/ellas disfrutarán de la película).",
            "their": "Their: Pronombre posesivo (pertenece a ellos/as): Ejemplo: Their house is big. (Su casa es grande.)  I like their style.(Me gusta su estilo.)",

            "them": "Them: Pronombre objeto (recibe la acción): Ejemplo: I saw them. (Los vi.). I gave them the book. (Les di el libro.).Significa que se usa cuando 'ellos' o 'ellas' son el objeto de la acción. Es el equivalente de 'los/las' o 'a ellos/a ellas'. Ejemplo: I saw them at the park.(Los vi en el parque.)",
            "target": "Considera cambiar 'target' por 'address or manage'",
            "cope": "Considera cambiar 'cope' por 'manage or self-regulate'",
            "coping": "Considera cambiar 'coping' por 'self-regulating'",
            "targeted interventions": "No es necesario reemplazar 'targeted interventions' o 'targeted intervention'."
        }

    def get_suggestion(self, word):
        return self.sugerencias.get(word, None) # Devuelve None si la palabra no tiene sugerencia


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
        print()
        print()
        print("********************************************")


# Example usage
texto_ejemplo = """
During today's visit to the "Other Place of Service," a range of maladaptive behaviors were observed, and a set of structured interventions were implemented to address these. Matthew displayed several maladaptive behaviors, including elopement, tantrums, off-task behavior, placing non-edible items in his mouth, climbing, refusal to comply, throwing objects, and physical aggression. For each of these behaviors, specific antecedents were identified, and targeted interventions were applied. When Matthew attempted to elope after being asked to complete a non-preferred task, which served the function of escape, verbal prompts and the provision of choices were utilized to direct his actions effectively. In response to throwing objects when asked to work, redirection strategies were implemented, recognizing the escape function of this behavior. When Matthew exhibited tantrums upon being told that a preferred item was unavailable, RBTs employed redirection combined with verbal prompts to shift his focus and address his need for tangibles. For refusal to comply during transitions from preferred to non-preferred activities, antecedent manipulation and functional communication training were applied to help Matthew navigate these transitions, addressing the escape function of his behavior. When Matthew placed non-edible items in his mouth while attention was diverted elsewhere, he was supported through antecedent manipulation and functional communication training to redirect his need for attention. Physical aggression arising from work requests was managed with verbal prompts, redirection, and antecedent manipulation, again addressing the escape function. Additionally, when off-task behavior was noted due to schedule changes, functional communication training was leveraged to support task engagement. Climbing, prompted by being told "no," with a tangible-seeking function, was addressed using a combination of redirection, verbal prompts, and antecedent manipulation. Throughout the session, replacement behavior programs were emphasized, including increasing Matthew's requests for items, his ability to mand for a break, follow instructions, stay on task for one minute, follow stop-and-go instructions, learn to wait without touching materials for five seconds, and take turns. Positive social reinforcements, such as verbal praise, high fives, thumbs up, and commendations for a job well done, were consistently used to encourage and reinforce Matthew's engagement in appropriate behaviors and compliance with interventions. he ride













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
