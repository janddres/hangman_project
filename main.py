#!/usr/bin/python3
"""Módulo principal"""


#  import de clases y funciones
import draw
import utils
from game import HangmanGame


def main():
    print(draw.TITLE)
    #  Seleccion del nivel, obtiene uno de los archivos.
    file = utils.chosen_level()
    if file is None:
        print("\nSaliste del juego. ¡Hasta la próxima!\n")
        return

    # selecciona una palabra enviado el archivo obtenido en el paso anterior.
    chosen_word = utils.get_random_word(file)

    game = HangmanGame(chosen_word)

    while not game.is_won() and not game.is_lost():
        print(f"\nTe quedan {game.max_errors - game.errors} intentos")
        print(draw.HANGMAN[game.errors])  # Dibujo ASCII del ahorcado
        print(game.display_progress())  # Palabra enmascarada (_ _ A _)

        letter = input("\nIngresa una letra: ").lower().strip()

        utils.clear_screen()  # Limpio la pantalla

        # Mejora . Opción de salida
        if letter in ["esc", "salir", "exit"]:
            print("\nSaliste del juego. ¡Hasta la próxima!\n")
            return

        #  validación, verifica que el usuario ingrese solo 1 letra
        if len(letter) != 1 or not letter.isalpha():
            print("\nPor favor, ingresa una sola letra")
            continue

        #  valida que la letra no haya sido ingresada
        if letter in game.guessed_letters:
            print("\nEsa letra ya fué ingresa, ingresa otra")
            continue

        game.process_guess(letter)

    if game.is_won():
        print("\n¡Ganaste!")
        print(f"\nLa palabra era: {game.word}\n")

        # Puntuación
        score = game.calculate_score()
        print(f"Tu puntuación fue: {score} pts")

        name = input("\nIngresa tu nombre: ").strip()
        if not name:
            name = "Anónimo"

        utils.save_score(name, score)
        utils.display_scores()
    else:
        print(draw.HANGMAN[game.errors])
        print(f"\nFin del juego\n\nLa palabra era: {game.word}\n")


if __name__ == "__main__":
    main()
