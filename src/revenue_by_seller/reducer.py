
#!/usr/bin/env python3

import sys

vendeur_actuel = None
total_ca = 0.0

for line in sys.stdin:

    try:
        # Séparer la clé et la valeur
        vendeur_id, chiffre_affaires = line.strip().split("\t")

        chiffre_affaires = float(chiffre_affaires)

        # Vérifier si le vendeur change
        if vendeur_actuel == vendeur_id:
            total_ca += chiffre_affaires

        else:
            # Afficher le résultat du vendeur précédent
            if vendeur_actuel is not None:
                print(f"{vendeur_actuel}\t{total_ca:.2f}")

            # Initialiser le nouveau vendeur
            vendeur_actuel = vendeur_id
            total_ca = chiffre_affaires

    except (ValueError, TypeError):
        continue

# Afficher le dernier vendeur
if vendeur_actuel is not None:
    print(f"{vendeur_actuel}\t{total_ca:.2f}")
