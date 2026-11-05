#!/usr/bin/python3
"""Módulo de juego"""

class HangmanGame:
    """Clase de juego"""
    def __init__(self, word: str):
        self.word = word #la palabra objetivo
        self.guessed_letters = [] #las letras que el usuario ha adivinado
        self.max_errors = 6 #errores maximo, establecido en 6
        self.errors = 0 #número de respuestas incorrectas

    def guess_letters(self, letter: str):
        self.guessed_letters.append(letter)
        if letter not in self.guessed_letters:
            self.errors += 1

    def display_progress(self):
        for i in self.word:
            print("_", end='')
        print()

