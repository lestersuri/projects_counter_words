document.addEventListener('DOMContentLoaded', () => {
    const textInput = document.getElementById('text-input');
    const analyzeBtn = document.getElementById('analyze-btn');
    const grammarCheckBtn = document.getElementById('grammar-check-btn');
    const clearBtn = document.getElementById('clear-btn');
    const loadExampleBtn = document.getElementById('load-example-btn');
    const resultsDiv = document.getElementById('results');
    const highlightedTextDiv = document.getElementById('highlighted-text');
    const grammarSuggestionsDiv = document.getElementById('grammar-suggestions');

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
        "targeted interventions": "No es necesario reemplazar 'targeted interventions' o 'targeted intervention'.",
        "targeted": "It is recommended to use 'addressed' instead of targeted when 'addressed' is used to describe behaviors or issues that have been dealt with."
    };

    const palabrasBuscar = [
        'replacement behavior', 'replacement behaviors', 'replacement_behavior_programs',
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

        const frasesCompletas = [
            "replacement behavior programs",
            "planned ignoring in terms of extinction",
            "desired behaviors",
            "desired behavior",
            "targeted interventions",
            "targeted intervention"
        ];

        // Buscar frases completas primero
        frasesCompletas.forEach(frase => {
            const regex = new RegExp('\\b' + frase.toLowerCase().replace(/\s+/g, '\\s+') + '\\b', 'g');
            const coincidencias = texto.match(regex);
            if (coincidencias) {
                resultados[frase] = coincidencias.length;
                texto = texto.replace(new RegExp(frase.toLowerCase(), 'g'), '');
            }
        });

        // Buscar palabras individuales
        palabrasBuscar.forEach(palabra => {
            if (['he', 'she'].includes(palabra)) {
                const regex = new RegExp('\\b' + palabra + '\\b\\s+\\w+', 'g');
                const coincidencias = texto.match(regex);
                if (coincidencias) {
                    coincidencias.forEach(coincidencia => {
                        const palabraCompleta = coincidencia.trim();
                        resultados[palabraCompleta] = (resultados[palabraCompleta] || 0) + 1;
                    });
                }
            } else if (!frasesCompletas.includes(palabra)) {
                const regex = new RegExp('\\b' + palabra.toLowerCase() + '\\b', 'g');
                const coincidencias = texto.match(regex);
                if (coincidencias) {
                    resultados[palabra] = coincidencias.length;
                }
            }
        });

        return resultados;
    }

    function mostrarResultados(resultados) {
        resultsDiv.innerHTML = '<div class="separator"></div>';

        for (const [palabra, conteo] of Object.entries(resultados)) {
            const resultItem = document.createElement('div');
            resultItem.className = 'result-item';

            if (palabra in sugerencias) {
                resultItem.textContent = `${palabra}: ${conteo} ${sugerencias[palabra]}`;
            } else {
                resultItem.textContent = `${palabra}: ${conteo}`;
            }

            resultsDiv.appendChild(resultItem);
            resultsDiv.appendChild(document.createElement('div')).className = 'separator';
        }
    }

    function resaltarPalabrasEnTexto(texto) {
        let textoResaltado = texto;
        const palabrasEncontradas = new Set();

        // Primero buscar frases completas
        const frasesCompletas = [
            "replacement behavior programs",
            "planned ignoring in terms of extinction",
            "desired behaviors",
            "desired behavior",
            "targeted interventions",
            "targeted intervention"
        ];

        frasesCompletas.forEach(frase => {
            const regex = new RegExp('\\b' + frase.replace(/\s+/g, '\\s+') + '\\b', 'gi');
            if (regex.test(texto)) {
                palabrasEncontradas.add(frase);
                textoResaltado = textoResaltado.replace(regex, match => 
                    `<span class="highlighted-word">${match}</span>`);
            }
        });

        // Luego buscar palabras individuales
        palabrasBuscar.forEach(palabra => {
            if (!frasesCompletas.includes(palabra)) {
                const regex = new RegExp('\\b' + palabra + '\\b', 'gi');
                if (regex.test(texto)) {
                    palabrasEncontradas.add(palabra);
                    textoResaltado = textoResaltado.replace(regex, match => 
                        `<span class="highlighted-word">${match}</span>`);
                }
            }
        });

        return {
            textoResaltado,
            palabrasEncontradas: Array.from(palabrasEncontradas)
        };
    }

    async function checkGrammar(text) {
        try {
            const response = await fetch('https://api.languagetool.org/v2/check', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({
                    'text': text,
                    'language': 'en-US',
                    'enabledOnly': 'false'
                })
            });

            const data = await response.json();
            return data.matches;
        } catch (error) {
            console.error('Error al revisar la gramática:', error);
            return [];
        }
    }

    // Eventos
    analyzeBtn.addEventListener('click', () => {
        const texto = textInput.value;
        if (!texto.trim()) {
            resultsDiv.innerHTML = '<p>Por favor, ingrese algún texto para analizar.</p>';
            highlightedTextDiv.innerHTML = '';
            return;
        }

        const resultados = contarPalabrasParciales(texto);
        const { textoResaltado } = resaltarPalabrasEnTexto(texto);
        
        mostrarResultados(resultados);
        highlightedTextDiv.innerHTML = textoResaltado;
    });

    clearBtn.addEventListener('click', () => {
        textInput.value = '';
        resultsDiv.innerHTML = '';
        highlightedTextDiv.innerHTML = '';
        grammarSuggestionsDiv.innerHTML = '';
    });

    loadExampleBtn.addEventListener('click', () => {
        textInput.value = texto_ejemplo;
        if (texto_ejemplo && texto_ejemplo.trim()) {
            const resultados = contarPalabrasParciales(texto_ejemplo);
            const { textoResaltado } = resaltarPalabrasEnTexto(texto_ejemplo);
            
            mostrarResultados(resultados);
            highlightedTextDiv.innerHTML = textoResaltado;
        }
    });

    grammarCheckBtn.addEventListener('click', async () => {
        const texto = textInput.value;
        if (!texto.trim()) {
            grammarSuggestionsDiv.innerHTML = '<p>Por favor, ingrese algún texto para revisar.</p>';
            return;
        }

        const matches = await checkGrammar(texto);
        displayGrammarSuggestions(matches);
    });

    function displayGrammarSuggestions(matches) {
        grammarSuggestionsDiv.innerHTML = '';
        if (matches.length === 0) {
            grammarSuggestionsDiv.innerHTML = '<p>No se encontraron errores gramaticales.</p>';
            return;
        }

        matches.forEach(match => {
            const suggestion = document.createElement('div');
            suggestion.className = 'grammar-suggestion';
            suggestion.innerHTML = `
                <div class="issue">Error: ${match.message}</div>
                <div class="suggestion">Sugerencia: ${match.replacements.length > 0 ? match.replacements[0].value : 'No hay sugerencias disponibles'}</div>
            `;
            grammarSuggestionsDiv.appendChild(suggestion);
        });
    }

    function highlightGrammarErrors(text, matches) {
        let htmlContent = text;
        // Ordenar los matches por posición para procesar desde el final hacia el principio
        const sortedMatches = [...matches].sort((a, b) => b.offset - a.offset);

        sortedMatches.forEach(match => {
            const start = match.offset;
            const end = start + match.length;
            const errorText = text.substring(start, end);
            const suggestion = match.replacements.length > 0 ? match.replacements[0].value : 'No hay sugerencias disponibles';
            
            // Crear un span con la sugerencia y el mensaje de error
            htmlContent = [
                htmlContent.slice(0, start),
                `<span class="highlight-error" 
                    title="Error: ${match.message}\nSugerencia: ${suggestion}" 
                    data-error="${match.message}" 
                    data-suggestion="${suggestion}">`,
                errorText,
                '</span>',
                htmlContent.slice(end)
            ].join('');
        });

        return htmlContent;
    }

    analyzeBtn.addEventListener('click', async () => {
        const texto = textInput.value;
        if (!texto.trim()) {
            resultsDiv.innerHTML = '<p>Por favor, ingrese algún texto para analizar.</p>';
            highlightedTextDiv.innerHTML = '';
            return;
        }

        const resultados = contarPalabrasParciales(texto);
        const { textoResaltado } = resaltarPalabrasEnTexto(texto);
        const matches = await checkGrammar(texto);
        
        mostrarResultados(resultados);
        
        let finalText = textoResaltado;
        if (matches && matches.length > 0) {
            finalText = highlightGrammarErrors(finalText, matches);
        }
        
        highlightedTextDiv.innerHTML = finalText;
    });

    clearBtn.addEventListener('click', () => {
        textInput.value = '';
        resultsDiv.innerHTML = '';
        highlightedTextDiv.innerHTML = '';
        grammarSuggestionsDiv.innerHTML = '';
    });

    loadExampleBtn.addEventListener('click', () => {
        textInput.value = 'The child displayed desired behaviors during the session. The therapist used planned ignoring in terms of extinction to address the targeted behaviors. The student expressed emotions while trying to cope with the situation.';
        const texto = textInput.value;
        const resultados = contarPalabrasParciales(texto);
        const { textoResaltado } = resaltarPalabrasEnTexto(texto);
        
        mostrarResultados(resultados);
        highlightedTextDiv.innerHTML = textoResaltado;
    });

    grammarCheckBtn.addEventListener('click', async () => {
        const texto = textInput.value;
        if (!texto.trim()) {
            grammarSuggestionsDiv.innerHTML = '<p>Por favor, ingrese texto para revisar la gramática.</p>';
            return;
        }

        grammarSuggestionsDiv.innerHTML = '<p>Revisando gramática...</p>';
        const matches = await checkGrammar(texto);
        displayGrammarSuggestions(matches);
    });
});