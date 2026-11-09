#!/usr/bin/python3
"""Módulo Utilitarios"""

import random
import os
import json

SCORES_FILE = "scores.json"


# funcion de palabra random
def get_random_word(chosen_file: str):

    with open(chosen_file, mode='r', encoding='utf-8') as file:
        words = file.read().splitlines()
    #  Limpio las palabras antes de la selección, recomendación de Cape.
    words = [w.strip() for w in words if w.strip()]
    return random.choice(words)


# Menu de seleccion de nivel
def chosen_level():
    """Muestra el menú y permite al usuario seeleccionar el nivel."""
    print("\n   SELECCIONA EL NIVEL   \n")
    print("1. Palabras 5-8 letras")
    print("2. Palabras +10 letras")
    print("3. Frases en ingles con números y símbolos")
    print("4. Salir")

    while True:
        opcion = input("\nElige una opción: ").strip()

        if opcion == "1":
            return "wordlist.txt"
        elif opcion == "2":
            return "wordlist_1.txt"
        elif opcion == "3":
            return "wordlist_2.txt"
        elif opcion == "4":
            return None  # Salir
        else:
            print("Opción no válida. Intenta de nuevo.")


# Fincion para limpiar la pantalla
def clear_screen():
    """Limpia la pnatlla detectando."""
    # 'nt' corresponde a Windows; posix a Linux y macOS
    os.system("cls" if os.name == "nt" else "clear")


# Mantenimiento de puntuación
def load_scores():
    """Carga las puntuaciones desde el archivo JSON.
    Si el archivo no existe, retorna una lista vacía."""
    if not os.path.exists(SCORES_FILE):
        return []

    try:
        with open(SCORES_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_score(player_name, score):
    """Guarda una nueva puntuación y mantiene solo los 5 mejores."""
    scores = load_scores()  # carga el Json a una lista de diccionarios

    # Se agrega un nuevo registo
    scores.append({"name": player_name, "score": score})

    # Se ordenan los puntajes
    scores = sorted(scores, key=lambda x: x["score"], reverse=True)

    # Persisto solo los mejores 5
    top_scores = scores[:5]

    with open(SCORES_FILE, "w", encoding="utf-8") as f:
        json.dump(top_scores, f, indent=4, ensure_ascii=False)


def display_scores():
    """Imprime la tabla de mejores puntuaciones."""
    scores = load_scores()

    print("\n   RANKING (TOP 5)   ")
    if not scores:
        print("Aún no hay puntuaciones.")
        return

    for idx, entry in enumerate(scores, start=1):
        print(f"{idx}. {entry['name']} - {entry['score']} pts")
    print()
