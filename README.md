# Juego del Ahorcado

## Descripción

Este proyecto consiste en desarrollar un juego del ahorcado en Python que funciona desde la consola. El jugador debe adivinar una palabra oculta, ingresando letras una por una, antes de alcanzar el límite de intentos incorrectos.

El juego utiliza una lista de palabras en español almacenadas en un archivo de texto, del cual selecciona una palabra aleatoriamente al comenzar cada partida.

## Estructura del Proyecto

```text
hangman_project/
├── main.py           # Inicio y bucle principal del juego
├── game.py           # Clase HangmanGame con la lógica del juego
├── utils.py          # Funciones auxiliares
├── wordlist.txt      # Lista de palabras en español
└── README.md         # Información e instrucciones del proyecto
```

### Descripción de Archivos

- **main.py**: Contiene el bucle principal del juego, solicita las letras al jugador y muestra los resultados de cada intento.
- **game.py**: Contiene la clase `HangmanGame`, encargada de almacenar la palabra, los intentos y las condiciones para ganar o perder.
- **utils.py**: Incluye la función `get_random_word()`, que permite seleccionar una palabra aleatoria.
- **wordlist.txt**: Contiene las palabras utilizadas durante el juego, una por línea.

## Reglas del Juego

1. El programa selecciona una palabra aleatoria en español.
2. El jugador debe adivinar la palabra ingresando una letra por turno.
3. Solo se aceptan letras individuales.
4. Cada letra incorrecta aumenta el contador de errores.
5. El jugador puede cometer hasta 6 errores.
6. Los espacios, guiones y signos de puntuación se muestran automáticamente.
7. El jugador gana cuando descubre todas las letras de la palabra.
8. El jugador pierde cuando alcanza los 6 errores permitidos.

## Cómo Ejecutar

1. Abrir una terminal o línea de comandos.
2. Ingresar a la carpeta `hangman_project`.
3. Ejecutar el siguiente comando:

```bash
python main.py
```

Para iniciar una nueva partida, se puede volver a ejecutar el programa.

## Ejemplo de Juego

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
Palabra: _ a _ a
Letras intentadas: a
Intentos restantes: 6
========================================

Ingresá una letra: e
La letra no está en la palabra.

========================================
Palabra: _ a _ a
Letras intentadas: a, e
Intentos restantes: 5
========================================
```

## Validación de Entrada

El programa comprueba que las letras ingresadas sean válidas.

No permite:

- Entradas vacías.
- Más de una letra a la vez.
- Números o símbolos.
- Letras que ya hayan sido intentadas.

Cuando se ingresa un valor incorrecto, el programa muestra un mensaje y solicita nuevamente una letra sin descontar intentos.

## Componentes Principales

### Clase HangmanGame

La clase `HangmanGame` permite guardar y administrar los datos de cada partida.

Sus atributos principales son:

- `word`: Palabra que debe adivinar el jugador.
- `guessed_letters`: Lista de letras acertadas.
- `errors`: Cantidad de intentos incorrectos.
- `max_errors`: Número máximo de errores permitidos, establecido en 6.

### Métodos Principales

- `display_progress()`: Muestra las letras descubiertas y oculta las que faltan.
- `process_guess(letter)`: Comprueba si la letra ingresada pertenece a la palabra.
- `is_won()`: Comprueba si el jugador completó la palabra.
- `is_lost()`: Comprueba si el jugador alcanzó el límite de errores.

### Función get_random_word()

Esta función se encuentra en `utils.py`.

Se encarga de leer las palabras almacenadas en `wordlist.txt` y seleccionar una de manera aleatoria utilizando el módulo `random` de Python.

## Notas de Desarrollo

El programa fue organizado en diferentes archivos para separar las funciones principales y facilitar su lectura.

Se utilizaron variables, condicionales, bucles, listas, funciones y una clase para desarrollar el funcionamiento del juego.

Los nombres de las variables, funciones y métodos están escritos en inglés, siguiendo las convenciones habituales de Python. Los comentarios y mensajes que aparecen en la consola están escritos en español.

La lista inicial contiene palabras en español y sin tildes para simplificar la entrada de letras.

## Requisitos

- Python 3.x instalado.
- Los archivos del proyecto deben encontrarse dentro de la misma carpeta.
- No se necesitan bibliotecas adicionales.

## Proyecto académico

**Universidad Tecnológica (UTEC)**

Proyecto: Python - Ahorcado
