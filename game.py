#!/usr/bin/python3
"""Módulo de juego"""

import draw


class HangmanGame:
    """Clase de juego"""
    def __init__(self, word: str):
        self.word = word  # la palabra objetivo
        self.guessed_letters = []  # las letras que el usuario ha adivinado
        self.max_errors = 6  # errores maximo, establecido en 6
        self.errors = 0  # número de respuestas incorrectas

    def process_guess(self, letter: str):
        """Método de letras que va proponieddo el jugador"""
        self.guessed_letters.append(letter)
        if letter not in self.word:
            self.errors += 1
        else:
            print(f"\nCorrecto, la letra '{letter}' está en la palabra")
            #  devolver correcto o incorrecto

    def display_progress(self):
        """Método para mostrar las letras adivinadas"""
        text = ""
        for letter in self.word:
            # Si la letra esta en la palabra
            # no es alfabetica se muestra (Punto 6)
            if letter in self.guessed_letters or not letter.isalpha():
                text = text + letter + " "
            else:
                text = text + "_ "
        if self.guessed_letters:
            print(f"\nLas letras que ya probaste son {self.guessed_letters}")
        print(draw.HANGMAN[self.errors])
        print(text.strip())

    def is_won(self):
        """Valida que se hallan ingresado todas las letras de la palabra"""
        for letter in self.word:
            #  Solo tiene en cuenta los caracteres alfabeticos (Punto 6)
            if letter.isalpha() and letter not in self.guessed_letters:
                return False  # Faltan letras
        return True  # Se ingresaron todas las letras

    def is_lost(self):
        return self.errors >= self.max_errors

    def calculate_score(self):
        """Calcula el puntaje basado en intentos
        restantes y longitud de la palabra."""
        remaining_attempts = self.max_errors - self.errors
        return (remaining_attempts * 100) + (len(self.word) * 10)
