# Juego del Ahorcado

## Descripción

Este es un juego del ahorcado desarrollado en Python que funciona desde la consola. El jugador debe adivinar una palabra oculta letra por letra antes de alcanzar el límite de intentos incorrectos.

El programa selecciona aleatoriamente una palabra en español desde un archivo de texto.

## Estructura del Proyecto

```text
hangman_project/
├── main.py           # Punto de entrada y bucle principal del juego
├── game.py           # Clase HangmanGame con la lógica del juego
├── utils.py          # Funciones auxiliares para cargar palabras
├── wordlist.txt      # Lista de palabras en español
└── README.md         # Instrucciones y descripción del proyecto
```

### Descripción de Archivos

- **main.py**: Contiene el bucle principal del juego, valida las letras ingresadas y muestra el progreso.
- **game.py**: Define la clase `HangmanGame`, que administra el estado y las reglas del juego.
- **utils.py**: Contiene la función `get_random_word()`, encargada de seleccionar una palabra aleatoria.
- **wordlist.txt**: Contiene 20 palabras en español, una por línea.

## Reglas del Juego

1. El programa selecciona una palabra aleatoria en español.
2. El jugador intenta adivinarla ingresando una letra por turno.
3. Solo se aceptan letras individuales.
4. Las letras ya intentadas no se pueden repetir.
5. Cada letra incorrecta aumenta el contador de errores.
6. El jugador puede cometer hasta 6 errores.
7. Los caracteres que no son letras, como espacios y guiones, se muestran automáticamente.
8. El jugador gana cuando descubre todas las letras de la palabra.
9. El jugador pierde cuando alcanza 6 errores.

## Cómo Ejecutar

1. Tener Python 3 instalado.
2. Abrir una terminal e ingresar a la carpeta del proyecto:

   ```bash
   cd hangman_project
   ```

3. Ejecutar el juego:

   ```bash
   python main.py
   ```

Para jugar otra partida, se puede volver a ejecutar el programa.

## Ejemplo de Juego

El siguiente ejemplo utiliza la palabra `gato` para mostrar cómo se desarrolla una partida. En el juego real, la palabra se selecciona al azar.

```text
¡Bienvenido al juego del ahorcado!

Se ha seleccionado una palabra. ¡A adivinar!

========================================
Palabra: _ _ _ _
Letras intentadas: ninguna
Intentos restantes: 6
========================================

Ingresá una letra: a
¡Correcto! La letra está en la palabra.

========================================
Palabra: _ a _ _
Letras intentadas: a
Intentos restantes: 6
========================================

Ingresá una letra: e
La letra no está en la palabra.

========================================
Palabra: _ a _ _
Letras intentadas: a, e
Intentos restantes: 5
========================================

Ingresá una letra: g
¡Correcto! La letra está en la palabra.

========================================
Palabra: g a _ _
Letras intentadas: a, e, g
Intentos restantes: 5
========================================

Ingresá una letra: t
¡Correcto! La letra está en la palabra.

========================================
Palabra: g a t _
Letras intentadas: a, e, g, t
Intentos restantes: 5
========================================

Ingresá una letra: o
¡Correcto! La letra está en la palabra.

========================================
Palabra: g a t o
Letras intentadas: a, e, g, t, o
Intentos restantes: 5
========================================
¡Ganaste!
========================================
```

## Validación de Entrada

El juego no permite:

- Entradas vacías.
- Más de una letra por intento.
- Números y símbolos.
- Letras que ya fueron intentadas, sean correctas o incorrectas.

Cuando la entrada no es válida, se muestra un mensaje de error y se solicita otra letra sin descontar intentos.

## Componentes Principales

### Clase HangmanGame

La clase `HangmanGame`, definida en `game.py`, guarda la información de la partida:

- `word`: Palabra que debe adivinar el jugador.
- `guessed_letters`: Lista de todas las letras intentadas, tanto correctas como incorrectas.
- `errors`: Cantidad de intentos incorrectos.
- `max_errors`: Límite máximo de errores, establecido en 6.

### Métodos Principales

- `display_progress()`: Muestra las letras descubiertas y oculta las que faltan mediante guiones bajos.
- `process_guess(letter)`: Comprueba la letra ingresada y actualiza el estado del juego.
- `is_won()`: Comprueba si el jugador adivinó todas las letras.
- `is_lost()`: Comprueba si el jugador alcanzó el límite de errores.

### Función get_random_word()

La función `get_random_word()`, ubicada en `utils.py`, lee el archivo `wordlist.txt` y utiliza `random.choice()` para seleccionar una palabra al azar.

## Notas de Desarrollo

El proyecto está dividido en varios archivos para separar la lógica del juego, la entrada del usuario y la carga de palabras.

Para desarrollar el programa se utilizaron variables, condicionales, bucles, listas, funciones, clases y lectura de archivos de texto.

Los nombres de las variables, clases y funciones están en inglés. Los comentarios, los mensajes que aparecen en pantalla y la documentación están en español.

Las palabras del archivo están escritas en minúsculas y sin tildes para facilitar las adivinanzas. La letra `ñ` se conserva y el archivo se lee con codificación UTF-8.

## Requisitos

- Python 3.x.
- Los archivos del proyecto deben estar en la misma carpeta.
- No se requieren bibliotecas adicionales.

## Proyecto Académico

**Universidad Tecnológica (UTEC)**

**Proyecto:** Python - Ahorcado

**Integrantes:**

- Federico Ramos
- Juan Aranda
