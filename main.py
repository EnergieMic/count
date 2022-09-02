# Micaël Brouillet 404
# word count
# Je crée une loupe pour reperter le programme.
while True:
# Je demande quelle phrase l'utilisateur veut.
 chaine = input('Écriver une phrase.')
# Si on ecrit rien et on presse enter le programme se ferme.
 if not chaine:
  print("Vous avez quitter le programme.")
  exit()
# Le programme print le nombre de mot dans la phrase.
 print("Votre phrase a", len(chaine.split(" ")), "mot(s).")

