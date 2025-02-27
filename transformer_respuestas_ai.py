from transformers import pipeline

respuesta_preguntas = pipeline("question-answering", model="deepset/xlm-roberta-base-squad2", tokenizer="deepset/xlm-roberta-base-squad2", use_fast=False)

contexto = "La Torre Eiffel se encuentra en París y es uno de los monumentos más emblemáticos de Francia."
pregunta = "¿Dónde se encuentra la Torre Eiffel?"
resultado = respuesta_preguntas(question=pregunta, context=contexto)

print(resultado['answer'])
