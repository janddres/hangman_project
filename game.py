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

    def play(self):
        """Método del juego."""
        while self.errors < self.max_errors:
            print(f"\nTe quedan {self.max_errors - self.errors} intentos")
            self.display_progress()

            letter = input("Ingresa una letra: ").lower().strip()
            #validación, verifica que el usuario ingrese solo 1 letra
            if len(letter) != 1 or not letter.isalpha():
                print("Por favor, ingresa una sola letra, no se permiten numeros")
                continue

            #valida que la letra no haya sido ingresada    
            if letter in self.guessed_letters:
                print("Esa letra ya fué ingresa, ingresa otra")
                continue

            self.guess_letters(letter)

            if self.is_success():
                print("Ganaste")
                self.display_progress()
                break

        if self.errors >= self.max_errors:
            print("Perdiste")