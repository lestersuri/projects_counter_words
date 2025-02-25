from transformers import pipeline

def resumir_texto(texto, max_longitud=100, min_longitud=30):
    """
    Resume un texto dado utilizando un modelo de Transformer.

    :param texto: El texto a resumir.
    :param max_longitud: Longitud máxima del resumen.
    :param min_longitud: Longitud mínima del resumen.
    :return: Resumen del texto.
    """
    resumidor = pipeline("summarization", model="facebook/bart-large-cnn")
    resumen = resumidor(texto, max_length=max_longitud, min_length=min_longitud, do_sample=False)
    
    return resumen[0]['summary_text']

# Ejemplo de uso
texto_original = """
La inteligencia artificial está revolucionando el mundo. Cada día, se desarrollan nuevos modelos y algoritmos 
que mejoran la forma en que interactuamos con la tecnología. Empresas de todo el mundo están invirtiendo en 
soluciones basadas en IA para optimizar procesos, reducir costos y mejorar la eficiencia. En los próximos años, 
se espera que la IA tenga un impacto aún mayor en la medicina, la educación y la industria en general.
"""

resumen = resumir_texto(texto_original, max_longitud=50, min_longitud=20)
print(resumen)
