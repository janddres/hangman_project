#!/usr/bin/python3
"""Módulo principal"""

#import de clases y funciones
import utils
import game

def main():
    palabra_elegida = utils.get_random_word()

    juego = game.HangmanGame(palabra_elegida)

    while not juego.is_success() and not juego.game_over():
        print(f"\nTe quedan {juego.max_errors - juego.errors} intentos")
        juego.display_progress()

        letter = input("Ingresa una letra: ").lower().strip()
        #validación, verifica que el usuario ingrese solo 1 letra
        if len(letter) != 1 or not letter.isalpha():
            print("Por favor, ingresa una sola letra, no se permiten numeros")
            continue

        #valida que la letra no haya sido ingresada    
        if letter in juego.guessed_letters:
            print("Esa letra ya fué ingresa, ingresa otra")
            continue

        juego.process_guess(letter)

    if juego.is_success():
        print("Ganaste")
        juego.display_progress()
    else:
        print(f"\nPerdiste. La palabra era: {juego.word}")


if __name__ == "__main__":
    main()
