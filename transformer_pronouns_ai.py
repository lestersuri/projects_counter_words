import spacy

# Cargar el modelo de lenguaje de SpaCy en inglés
nlp = spacy.load('en_core_web_sm')

# Función para sustituir pronombres por nombres
def replace_pronouns_with_name(text, name_dict):
    doc = nlp(text)  # Analizar el texto usando SpaCy
    
    # Crear una lista para guardar las palabras modificadas
    modified_tokens = []

    for token in doc:
        # Revisar si el token es un pronombre
        if token.pos_ == 'PRON':
            # Sustituir el pronombre por el nombre correspondiente si está en el diccionario
            if token.text.lower() in name_dict:
                modified_tokens.append(name_dict[token.text.lower()])
            else:
                modified_tokens.append(token.text)
        else:
            # Si no es un pronombre, añadir la palabra tal cual
            modified_tokens.append(token.text)

    # Unir los tokens modificados en un solo texto
    modified_text = ' '.join(modified_tokens)
    return modified_text

# Diccionario con los pronombres y sus correspondientes nombres
name_dict = {
    'he': 'John',
    'she': 'Mary',
    'they': 'Alex',  # Puede ser un nombre común para "they" en singular
    'them': 'Alex',
    'i': 'I'  # El pronombre 'I' ya es el nombre de la persona que habla, no necesita cambio
}

# Texto de ejemplo con pronombres
text = "They went to the park and then they played basketball. He loves it, and she does too."

# Reemplazar pronombres por nombres
modified_text = replace_pronouns_with_name(text, name_dict)
print("Texto original:", text)
print("Texto modificado:", modified_text)
