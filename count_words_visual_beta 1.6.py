import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import re
from collections import Counter

# Diccionario con sugerencias para palabras específicas
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

# ... rest of the code remains the same ...

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
    'met',
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
    'targets',
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

texto_ejemplo = """ """



def contar_palabras_parciales(texto, palabras_buscar):
    # [Mantener la función exactamente igual que en el archivo original]
    texto = texto.lower()
    resultados = {}

    frases_completas = [
        "replacement behavior programs",
        "planned ignoring in terms of extinction",
        "desired behaviors",
        "desired behavior",
        "targeted interventions",
        "targeted intervention"
    ]

    for frase in frases_completas:
        patron = re.compile(rf'\b{re.escape(frase.lower())}\b')
        coincidencias = patron.findall(texto)
        if coincidencias:
            resultados[frase] = len(coincidencias)
            texto = texto.replace(frase.lower(), '')

    for palabra in palabras_buscar:
        if palabra in ['he', 'she']:
            patron = re.compile(rf'\b{re.escape(palabra)}\b \w+')
            coincidencias = patron.findall(texto)
            if coincidencias:
                for coincidencia in coincidencias:
                    palabra_completa = coincidencia.strip()
                    resultados[palabra_completa] = resultados.get(palabra_completa, 0) + 1
            continue
        
        if palabra not in frases_completas:
            patron = re.compile(rf'\b{re.escape(palabra.lower())}\b')
            coincidencias = patron.findall(texto)
            if coincidencias:
                resultados[palabra] = len(coincidencias)
    
    return resultados


# ... [previous code with sugerencias, palabras_buscar, etc.] ...

class WordCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador de Texto")
        self.root.geometry("730x780")
        
        # Frame principal
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Área de entrada de texto
        ttk.Label(main_frame, text="Ingrese el texto a analizar:", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky=tk.W)
        self.text_input = scrolledtext.ScrolledText(main_frame, width=100, height=15, font=('Arial', 10))
        self.text_input.grid(row=1, column=0, columnspan=2, pady=5)

        
        # Botones
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Analizar Texto", command=self.analyze_text).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Limpiar", command=self.clear_all).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Cargar Ejemplo", command=self.load_example).grid(row=0, column=2, padx=5)
        
        # Área de resultados
        ttk.Label(main_frame, text="Resultados:", font=('Arial', 10, 'bold')).grid(row=3, column=0, sticky=tk.W)
        self.results_area = scrolledtext.ScrolledText(main_frame, width=100, height=25, font=('Arial', 10))
        self.results_area.grid(row=4, column=0, columnspan=2, pady=5)

    def load_example(self):
        self.text_input.delete(1.0, tk.END)
        self.text_input.insert(tk.END, texto_ejemplo)

    def clear_all(self):
        self.text_input.delete(1.0, tk.END)
        self.results_area.delete(1.0, tk.END)
        
    def analyze_text(self):
        self.results_area.delete(1.0, tk.END)
        texto = self.text_input.get(1.0, tk.END)
        
        if not texto.strip():
            self.results_area.insert(tk.END, "Por favor, ingrese algún texto para analizar.")
            return
            
        resultados = contar_palabras_parciales(texto, palabras_buscar)
        
        self.results_area.insert(tk.END, "********************************************\n\n")
        
        for palabra, conteo in resultados.items():
            if palabra in sugerencias:
                salida = f"{palabra}: {conteo} {sugerencias[palabra]}"
            else:
                salida = f"{palabra}: {conteo}"
            
            self.results_area.insert(tk.END, salida + "\n")
            self.results_area.insert(tk.END, "-----------------------------\n")
        
        self.results_area.insert(tk.END, "\n********************************************")

if __name__ == "__main__":
    root = tk.Tk()
    app = WordCounterApp(root)
    root.mainloop()
