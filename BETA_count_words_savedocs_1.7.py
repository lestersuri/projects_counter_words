from docx import Document

# Función para guardar el texto en un archivo Word
def guardar_en_word(texto, nombre_documento="resultado2.docx"):
    doc = Document()
    
    # Agregar el texto al documento Word
    doc.add_paragraph(texto)
    
    # Guardar el documento en la ruta indicada
    doc.save(nombre_documento)
    print(f"Documento guardado en {nombre_documento}")

# Texto de ejemplo que deseas almacenar
texto_ejemplo = """
12121212123


"""

# Llamar a la función para guardar el texto en un documento Word
guardar_en_word(texto_ejemplo, "C:/Users/Admon/OneDrive/Desktop/word_replace.docx")
