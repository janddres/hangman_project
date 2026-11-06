#!/usr/bin/python3
"""Módulo de juego"""

class HangmanGame:
    """Clase de juego"""
    def __init__(self, word: str):
        self.word = word #la palabra objetivo
        self.guessed_letters = [] #las letras que el usuario ha adivinado
        self.max_errors = 6 #errores maximo, establecido en 6
        self.errors = 0 #número de respuestas incorrectas  

    def process_guess(self, letter: str):
        """Método de letras que va proponieddo el jugador"""
        self.guessed_letters.append(letter)
        if letter not in self.word:
            self.errors += 1

    def display_progress(self):
        """Método para mostrar las letras adivinadas"""
        progress = []
        for i in self.word:
            if i in self.guessed_letters:
                progress.append(i)
            else:
                progress.append("_")    
        print(progress)

    def is_success(self):
        """Valida que se hallan ingresado todas las letras de la palabra"""
        for i in self.word:
            if i not in self.guessed_letters:
                return False #Faltan letras
        return True #Se ingresaron todas las letras

    def game_over(self):
        return self.errors >= self.max_errors

 