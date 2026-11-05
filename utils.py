#!/usr/bin/python3
"""Módulo Utilitarios"""

def get_random_word():
    #libreria random
    import random

    with open('wordlist.txt', 'r', encoding='utf-8') as f:
        palabras = f.read().splitlines()

    palabra_elegida = random.choice(palabras)
    return palabra_elegida.strip()

#print(palabra_elegida)
