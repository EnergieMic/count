# Micaël Brouillet 404
# word count
import sys
# Je met une loupe pour repeter mon programme.
while True:
    # Je demande quelle phrase l'utilisateur veut.
    chaine = input('Écriver une phrase.')
    # Le programme print le nombre de mot dans la phrase.
    print("Votre phrase a", len(chaine.split(" ")), "mot(s).")
    sys.exit(0)

