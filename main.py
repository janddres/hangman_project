#!/usr/bin/python3
"""Módulo principal"""

#libreria random
import random

with open('wordlist.txt', 'r', encoding='utf-8') as f:
    palabras = f.read().splitlines()

palabra_elegida = random.choice(palabras)

print(palabra_elegida)