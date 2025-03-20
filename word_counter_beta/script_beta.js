// Importar las variables y funciones del archivo Python original
const sugerencias = {
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
    "desired outcomes": "Considera cambiar 'desired outcomes' por 'appropriate outcomes'",
    "desired outcome": "Considera cambiar 'desired outcome' por 'appropriate outcome'",
    "desired tangibles": "Considerar cambiar 'desired tangibles' por 'preferred tangibles'",
    "desired tangible": "Considerar cambiar 'desired tangible' por 'preferred tangible'",
    "desirable behaviors": "Considerar cambiar 'desirable behaviors' por 'appropriate behaviors'",
    "desirable behavior": "Considerar cambiar 'desirable behavior' por 'appropriate behavior'",
    "desirable": "Considerar cambiar 'desirable' por 'appropriate'",
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
    "them": "Them: Pronombre objeto (recibe la acción): Ejemplo: I saw them. (Los vi.). I gave them the book. (Les di el libro.).Significa que se usa cuando 'ellos' o 'ellas' son el objeto de la acción. Es el equivalente de 'los/las' o 'a ellos/a ellas'. Ejemplo: I saw them at the park.(Los vi en el parque.)",
    "tackled": "Considera cambiar 'tackled' por 'addressed'",
    "tackling": "Considera cambiar 'tackling' por 'addressing'",
    "replacement behaviors": "Considera cambiar 'replacement behaviors' por 'replacement behavior programs'",
    "targeted interventions": "No es necesario reemplazar 'targeted interventions' o 'targeted intervention'.",
    "targeted": "It is recommended to use 'addressed' instead of targeted when 'addressed' is used to describe behaviors or issues that have been dealt with."
};

const palabrasBuscar = [
    'replacement behavior', 'replacement behaviors', 'replacement behavior programs',
    'replace program', 'replace programs', 'plannned ignorin',
    'planned ignoring in terms of extinction', 'express emotion', 'express emotions',
    'expressed emotions', 'unwarranted', 'desired tangibles', 'desire', 'desires',
    'desired', 'desired outcomes', 'desired outcome', 'desirable behaviors',
    'desirable behavior', 'desirable', 'planned ignore', 'undesired', 'desired items',
    'desired item', 'desire to item', 'desired behavior', 'desired behaviors',
    'undesirable', 'desrired task', 'desired task', 'desire to escape',
    'desired attention', 'desired tangibles', 'desired tangigle', 'she', 'he',
    'met', 'adaptative', 'express emotion', 'counteract', 'counteracting',
    'countered', 'countering', 'frustation', 'cope', 'coping', 'planned ignoring',
    'they', 'them', 'their', 'combat', 'counter', 'counteracts', 'counteract',
    'target', 'targeted behaviors', 'targeting', 'individual', 'targets',
    'consumer', 'customer', 'receipt', 'student', 'child', 'subject',
    'therapist', 'observer', 'desirables activities', 'undesired', 'provider',
    'targeted interventions', 'tackled', 'tackling', 'tackle', 'targeted'
];

function contarPalabrasParciales(texto) {
    texto = texto.toLowerCase();
    const resultados = {};
    const posiciones = {};

    const frasesCompletas = [
        "replacement behavior programs",
        "planned ignoring in terms of extinction",
        "desired behaviors",
        "desired behavior",
        "targeted interventions",
        "targeted intervention",
        "desirable behavior",
        "desirable behaviors"
    ];

    // Buscar frases completas primero
    frasesCompletas.forEach(frase => {
        const regex = new RegExp('\\b' + frase.toLowerCase() + '\\b', 'g');
        let match;
        
        while ((match = regex.exec(texto)) !== null) {
            resultados[frase] = (resultados[frase] || 0) + 1;
            if (!posiciones[frase]) posiciones[frase] = [];
            posiciones[frase].push(match.index);
        }
    });

    // Buscar palabras individuales
    palabrasBuscar.forEach(palabra => {
        if (['he', 'she'].includes(palabra)) {
            const regex = new RegExp('\\b' + palabra + '\\s+\\w+\\b', 'gi');
            let match;
            while ((match = regex.exec(texto)) !== null) {
                const palabraCompleta = match[0].trim();
                resultados[palabraCompleta] = (resultados[palabraCompleta] || 0) + 1;
                if (!posiciones[palabraCompleta]) posiciones[palabraCompleta] = [];
                posiciones[palabraCompleta].push(match.index);
            }
        } else if (!frasesCompletas.includes(palabra)) {
            const regex = new RegExp('\\b' + palabra.toLowerCase() + '\\b', 'g');
            let match;
            
            while ((match = regex.exec(texto)) !== null) {
                resultados[palabra] = (resultados[palabra] || 0) + 1;
                if (!posiciones[palabra]) posiciones[palabra] = [];
                posiciones[palabra].push(match.index);
            }
        }
    });

    return { resultados, posiciones };
}

// Elementos del DOM
const textInput = document.getElementById('text-input');
const analyzeBtn = document.getElementById('analyze-btn');
const clearBtn = document.getElementById('clear-btn');
const loadExampleBtn = document.getElementById('load-example-btn');
const resultsDiv = document.getElementById('results');

// Función para resaltar palabras en el texto
function escapeHtml(text) {
    return text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}

function resaltarPalabras(texto, posiciones) {
    const displayDiv = document.createElement('div');
    displayDiv.className = 'highlighted-text';
    displayDiv.style.whiteSpace = 'pre-wrap';
    displayDiv.style.minHeight = '200px';
    displayDiv.style.maxHeight = '400px';
    displayDiv.style.overflowY = 'auto';
    displayDiv.style.padding = '20px';
    displayDiv.style.border = '1px solid #ddd';
    displayDiv.style.borderRadius = '8px';
    displayDiv.style.marginTop = '20px';
    displayDiv.style.backgroundColor = '#fafafa';
    displayDiv.style.fontSize = '14px';
    displayDiv.style.lineHeight = '1.6';
    
    // Clean and escape the input text first
    let resultado = escapeHtml(texto);
    
    // Create a map of positions to avoid overlapping highlights
    const highlightMap = new Map();
    
    // Process all positions and create highlight map
    for (const [palabra, pos] of Object.entries(posiciones)) {
        const palabraLower = palabra.toLowerCase();
        pos.forEach(posicion => {
            const length = palabra.length;
            // Check for overlapping highlights
            let canHighlight = true;
            for (let i = posicion; i < posicion + length; i++) {
                if (highlightMap.has(i)) {
                    canHighlight = false;
                    break;
                }
            }
            
            if (canHighlight) {
                // Mark all positions as taken
                for (let i = posicion; i < posicion + length; i++) {
                    highlightMap.set(i, {
                        palabra: palabraLower,
                        start: posicion,
                        length: length
                    });
                }
            }
        });
    }
    
    // Convert the map to array and sort by position
    const sortedPositions = Array.from(highlightMap.entries())
        .filter(([_, data]) => data.start === _)
        .sort((a, b) => b[0] - a[0]);
    
    // Apply highlights
    for (const [posicion, data] of sortedPositions) {
        const inicio = data.start;
        const fin = inicio + data.length;
        const sugerencia = sugerencias[data.palabra] ? escapeHtml(sugerencias[data.palabra]) : '';
        const originalText = resultado.slice(inicio, fin);
        
        const beforeText = resultado.slice(0, inicio);
        const afterText = resultado.slice(fin);
        
        resultado = beforeText + 
                   `<span class="highlighted" data-word="${escapeHtml(data.palabra)}" title="${sugerencia}">${originalText}</span>` + 
                   afterText;
    }



    displayDiv.innerHTML = resultado;
    return displayDiv;
}



// Eventos
analyzeBtn.addEventListener('click', analizarTexto);

clearBtn.addEventListener('click', () => {
    textInput.value = '';
    resultsDiv.innerHTML = '';
});

loadExampleBtn.addEventListener('click', () => {
    textInput.value = texto_ejemplo;
    if (texto_ejemplo.trim()) {
        analizarTexto();
    }
});

function analizarTexto() {
    const texto = textInput.value;
    if (!texto.trim()) {
        resultsDiv.innerHTML = '<p>Por favor, ingrese algún texto para analizar.</p>';
        return;
    }

    const { resultados, posiciones } = contarPalabrasParciales(texto);
    
    // Clear previous results
    resultsDiv.innerHTML = '';
    
    // Create and show word count results
    const resultsList = document.createElement('div');
    resultsList.className = 'results-list';
    
    for (const [palabra, cantidad] of Object.entries(resultados)) {
        const resultItem = document.createElement('div');
        resultItem.className = 'result-item';
        
        const wordContainer = document.createElement('div');
        wordContainer.className = 'word-container';
        
        const wordSpan = document.createElement('span');
        wordSpan.className = 'word';
        wordSpan.textContent = palabra;
        
        const countSpan = document.createElement('span');
        countSpan.className = 'count';
        countSpan.textContent = cantidad;
        
        wordContainer.appendChild(wordSpan);
        wordContainer.appendChild(countSpan);
        
        if (sugerencias[palabra]) {
            const suggestionDiv = document.createElement('div');
            suggestionDiv.className = 'suggestion';
            suggestionDiv.textContent = sugerencias[palabra];
            wordContainer.appendChild(suggestionDiv);
        }
        
        resultItem.appendChild(wordContainer);
        resultsList.appendChild(resultItem);
    }
    
    resultsDiv.appendChild(resultsList);
    
    // Create and show highlighted text
    const displayDiv = resaltarPalabras(texto, posiciones);
    resultsDiv.appendChild(displayDiv);
}

function mostrarResultados(resultados) {
    resultsDiv.innerHTML = '<div class="separator"></div>';

    for (const [palabra, conteo] of Object.entries(resultados)) {
        const resultItem = document.createElement('div');
        resultItem.className = 'result-item';

        if (palabra in sugerencias) {
            const sugerenciaDiv = document.createElement('div');
            sugerenciaDiv.innerHTML = `${palabra}: ${conteo} ${sugerencias[palabra]}`;
            resultItem.appendChild(sugerenciaDiv);
        } else {
            resultItem.textContent = `${palabra}: ${conteo}`;
        }

        resultsDiv.appendChild(resultItem);
        resultsDiv.appendChild(document.createElement('div')).className = 'separator';
    }
}

// Estilos CSS para resaltado y botones
const style = document.createElement('style');
style.textContent = `
    .highlighted {
        background-color: #ffeb3b;
        padding: 2px;
        border-radius: 3px;
        cursor: pointer;
        position: relative;
    }
    .highlighted:hover {
        background-color: #ffd700;
    }
    .replace-btn {
        margin-top: 5px;
        padding: 5px 10px;
        background-color: #2196F3;
        color: white;
        border: none;
        border-radius: 3px;
        cursor: pointer;
        font-size: 12px;
        transition: background-color 0.3s;
    }
    .replace-btn:hover {
        background-color: #1976D2;
    }
    .highlighted-text {
        background-color: white;
        font-family: Arial, sans-serif;
        line-height: 1.6;
        margin-bottom: 20px;
        overflow-y: auto;
    }
    .result-item {
        padding: 12px;
        border-bottom: 1px solid #eee;
        background-color: #f9f9f9;
        transition: background-color 0.2s;
    }
    .result-item:hover {
        background-color: #f0f0f0;
    }
    .word-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 6px;
    }
    .word {
        font-weight: bold;
        color: #333;
        font-size: 14px;
    }
    .count {
        background-color: #e0e0e0;
        padding: 2px 8px;
        border-radius: 12px;
        color: #666;
        font-size: 12px;
        min-width: 24px;
        text-align: center;
    }
    .suggestion {
        color: #666;
        font-size: 13px;
        margin-top: 4px;
        font-style: italic;
    }
    .separator {
        margin: 10px 0;
        border-bottom: 1px solid #eee;
    }
`;
document.head.appendChild(style);