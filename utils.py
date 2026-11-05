#!/usr/bin/python3
"""Módulo Utilitarios"""

#libreria random
import random

#funcion de palabra random
def get_random_word():

    with open('wordlist.txt', 'r', encoding='utf-8') as f:
        palabras = f.read().splitlines()

    palabra_elegida = random.choice(palabras)
    return palabra_elegida.strip()
