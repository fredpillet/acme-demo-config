#!/usr/bin/env python3
"""Trie les caractères d'une chaîne par ordre alphabétique."""

import sys
import unicodedata


def cle_alphabetique(caractere: str) -> tuple:
    """Clé de tri insensible à la casse et aux accents (é se range avec e)."""
    sans_accent = unicodedata.normalize("NFD", caractere)[0]
    return (sans_accent.lower(), caractere)


def trier_chaine(texte: str, ignorer_espaces: bool = True) -> str:
    """Retourne les caractères de `texte` triés par ordre alphabétique."""
    if ignorer_espaces:
        texte = "".join(c for c in texte if not c.isspace())
    return "".join(sorted(texte, key=cle_alphabetique))


def main() -> None:
    if len(sys.argv) > 1:
        texte = " ".join(sys.argv[1:])
    else:
        texte = input("Entrez une chaîne de caractères : ")
    print(trier_chaine(texte))


if __name__ == "__main__":
    main()
