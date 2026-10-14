#!/usr/bin/env python3
"""Trie les caractères d'une chaîne par ordre alphabétique."""

import sys
import unicodedata


def cle_alphabetique(caractere: str) -> tuple:
    """Clé de tri insensible à la casse et aux accents (é se range avec e)."""
    base = unicodedata.normalize("NFD", caractere)
    base = "".join(c for c in base if not unicodedata.combining(c))
    return (base.casefold(), caractere)


def trier_chaine(texte: str, ignorer_espaces: bool = True) -> str:
    """Retourne les caractères de `texte` triés par ordre alphabétique."""
    caracteres = [c for c in texte if not (ignorer_espaces and c.isspace())]
    return "".join(sorted(caracteres, key=cle_alphabetique))


def main() -> None:
    if len(sys.argv) > 1:
        texte = " ".join(sys.argv[1:])
    else:
        texte = input("Chaîne à trier : ")
    print(trier_chaine(texte))


if __name__ == "__main__":
    main()
