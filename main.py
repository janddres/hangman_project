#!/usr/bin/python3
"""Módulo principal"""

#import de clases y funciones
import utils

def main():
    palabra_elegida = utils.get_random_word()
    print(palabra_elegida)

if __name__ == "__main__":
    main()