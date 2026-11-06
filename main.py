#!/usr/bin/python3
"""Módulo principal"""

#import de clases y funciones
import utils
import game

def main():
    palabra_elegida = utils.get_random_word()

    juego = game.HangmanGame(palabra_elegida)

    juego.play()

if __name__ == "__main__":
    main()
