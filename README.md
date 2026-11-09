# Juego del Ahorcado en Python

Juego del ahorcado desarrollado en Python para ejecutarse desde la consola. El jugador debe adivinar una palabra o frase ingresando una letra por turno antes de cometer seis errores.

El programa incluye tres niveles, dibujos ASCII que muestran el progreso del ahorcado, una opción para abandonar la partida y un ranking con las cinco mejores puntuaciones.

## Estructura del proyecto

```text
hangman_project/
├── main.py          # Punto de entrada y desarrollo de la partida
├── game.py          # Clase HangmanGame y reglas del juego
├── utils.py         # Selección de nivel, palabras y puntuaciones
├── draw.py          # Título y dibujos ASCII
├── wordlist.txt     # Lista del nivel 1: palabras de 5 a 8 letras
├── wordlist_1.txt   # Lista del nivel 2: palabras de más de 10 letras
├── wordlist_2.txt   # Lista del nivel 3: frases en inglés
├── scores.json      # Ranking de puntuaciones (se crea al guardar)
└── README.md        # Documentación
```

> Los nombres y las características de los archivos de palabras corresponden a las opciones configuradas en `utils.py`. Los archivos de listas deben existir para jugar los niveles correspondientes.

## Descripción de los archivos

- **`main.py`:** muestra el título, coordina el menú, desarrolla el bucle principal, valida las entradas y presenta el resultado de cada partida.
- **`game.py`:** contiene la clase `HangmanGame`, responsable de las letras probadas, los errores, el progreso, la victoria, la derrota y los puntos.
- **`utils.py`:** selecciona el archivo del nivel, obtiene una palabra aleatoria, limpia la consola y administra las puntuaciones.
- **`draw.py`:** define `TITLE` y `HANGMAN`, con el título y los siete estados gráficos (de cero a seis errores).
- **`wordlist.txt`, `wordlist_1.txt` y `wordlist_2.txt`:** suministran las palabras o frases para cada nivel.
- **`scores.json`:** guarda los resultados en formato JSON. Se crea al registrar una puntuación, si no existía.

## Niveles de dificultad

Al iniciar el juego aparece este menú:

```text
SELECCIONA EL NIVEL

1. Palabras 5-8 letras
2. Palabras +10 letras
3. Frases en ingles con números y símbolos
4. Salir
```

Cada una de las tres primeras opciones utiliza un archivo de texto diferente. Si la opción no es válida, se solicita nuevamente. La cuarta opción finaliza el programa.

## Reglas del juego

1. El jugador elige un nivel y el programa selecciona una palabra o frase aleatoria del archivo correspondiente.
2. Se ingresa **una letra por turno**; la entrada se convierte a minúsculas y se eliminan los espacios iniciales y finales.
3. No se aceptan entradas vacías, números, símbolos ni más de una letra como intento.
4. Tampoco se permiten letras ya utilizadas. Las entradas inválidas o repetidas **no descuentan intentos**.
5. Cada letra equivocada suma un error. El máximo permitido es **seis**.
6. Los espacios, números y otros caracteres no alfabéticos aparecen automáticamente en el progreso de la palabra o frase.
7. El dibujo del ahorcado cambia según los errores acumulados.
8. Se gana al descubrir todas las letras alfabéticas; se pierde al alcanzar los seis errores.
9. Durante una partida se puede escribir `esc`, `salir` o `exit` para terminarla sin guardar puntuación.
10. Si se gana, se calcula el puntaje, se solicita el nombre y se muestra el ranking actualizado.

## Cómo ejecutar

**Requisito:** Python 3. No se necesitan bibliotecas de terceros.

Desde una terminal, ingresar a la carpeta que contiene el proyecto:

```bash
cd hangman_project
```

Ejecutar:

```bash
python main.py
```

En sistemas donde el comando sea `python3`, usar:

```bash
python3 main.py
```

Para comenzar otra partida, hay que ejecutar nuevamente el programa.

## Ejemplo de partida

Este ejemplo es ilustrativo: supone que la palabra seleccionada es `gato` y resume algunas rondas.

```text
SELECCIONA EL NIVEL

1. Palabras 5-8 letras
2. Palabras +10 letras
3. Frases en ingles con números y símbolos
4. Salir

Elige una opción: 1

Te quedan 6 intentos
_ _ _ _

Ingresa una letra: a
Correcto, la letra 'a' está en la palabra

Te quedan 6 intentos
Las letras que ya probaste son ['a']
_ a _ _

Ingresa una letra: e

Te quedan 5 intentos
Las letras que ya probaste son ['a', 'e']
_ a _ _

[El jugador adivina g, t y o]

¡Ganaste!
La palabra era: gato
Tu puntuación fue: 540 pts

Ingresa tu nombre: Federico

RANKING (TOP 5)
1. Federico - 540 pts
```

En la ejecución real se muestran también los dibujos ASCII y se limpia la pantalla después de cada entrada.

## Componentes principales

### Clase `HangmanGame` (`game.py`)

Atributos:

- `word`: palabra o frase por descubrir.
- `guessed_letters`: lista de las letras ya intentadas.
- `errors`: cantidad de errores acumulados.
- `max_errors`: máximo de errores, fijado en `6`.

Métodos:

- `__init__(word)`: inicializa el estado de una partida.
- `process_guess(letter)`: registra la letra y aumenta los errores si no aparece en la palabra.
- `display_progress()`: devuelve las letras adivinadas y guiones bajos para las pendientes; muestra los caracteres no alfabéticos.
- `is_won()`: comprueba si se adivinaron todas las letras alfabéticas.
- `is_lost()`: comprueba si se alcanzó el límite de errores.
- `calculate_score()`: calcula los puntos usando los intentos restantes y **solo las letras alfabéticas**.

### Funciones de `utils.py`

- `chosen_level()`: muestra el menú y devuelve el nombre del archivo elegido, o `None` para salir.
- `get_random_word(chosen_file)`: lee el archivo, descarta líneas vacías y elige una entrada con `random.choice()`.
- `clear_screen()`: ejecuta `cls` en Windows o `clear` en Linux/macOS.
- `load_scores()`: lee `scores.json` o devuelve una lista vacía si falta o no puede interpretarse.
- `save_score(player_name, score)`: añade una puntuación y conserva las cinco mayores.
- `display_scores()`: muestra el ranking en pantalla.

### Constantes de `draw.py`

- `TITLE`: imagen ASCII inicial.
- `HANGMAN`: dibujos correspondientes a los estados de cero a seis errores.

## Sistema de puntuación

**La puntuación se calcula únicamente cuando el jugador gana.** Se suman 100 puntos por cada intento restante y 10 por cada **letra alfabética** de la palabra o frase. Los espacios, números y símbolos no suman puntos.

La implementación corregida de `calculate_score()` es:

```python
def calculate_score(self):
    """Calcula los puntos por intentos restantes y letras alfabéticas."""
    remaining_attempts = self.max_errors - self.errors
    total_letters = sum(1 for letter in self.word if letter.isalpha())
    return (remaining_attempts * 100) + (total_letters * 10)
```

Por ejemplo, al acertar `gato` con un error:

```text
Intentos restantes: 6 - 1 = 5
Letras alfabéticas: 4
Puntuación: (5 × 100) + (4 × 10) = 540 puntos
```

Con la frase `hello world 2026!`, solo se cuentan las diez letras de `hello` y `world`. No se suman puntos por los espacios, los números ni el signo de exclamación.

> **Importante:** esta documentación describe la fórmula corregida. Para que el programa se comporte así, hay que reemplazar el método `calculate_score()` anterior en `game.py` por la versión mostrada arriba.

## Ranking de jugadores

Después de una victoria, el programa pide un nombre. Si se deja vacío, utiliza `Anónimo`.

La información se almacena en `scores.json`, por ejemplo:

```json
[
  {"name": "Federico", "score": 540},
  {"name": "Juan", "score": 420}
]
```

Cada vez que se registra una puntuación, los resultados se ordenan de mayor a menor y solo permanecen los cinco mejores. El ranking es compartido por los tres niveles de dificultad.

## Notas de desarrollo

El proyecto separa la interacción con el jugador (`main.py`), la lógica de la partida (`game.py`), las utilidades y el almacenamiento (`utils.py`) y los dibujos (`draw.py`).

Se utilizan variables, condicionales, bucles, listas, diccionarios, funciones, clases, módulos, archivos de texto y JSON. Los módulos `random`, `os` y `json` pertenecen a la biblioteca estándar de Python.

Los nombres de las funciones, clases y variables están en inglés; la interfaz y los comentarios están principalmente en español. Los archivos de palabras se leen con codificación UTF-8.

## Proyecto académico

**Universidad Tecnológica (UTEC)**  
**Proyecto:** Python - Ahorcado

**Integrantes:**

- Federico Ramos
- Juan Aranda
