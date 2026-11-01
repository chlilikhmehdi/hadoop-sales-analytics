
#!/usr/bin/env python3

import sys
from decimal import Decimal, InvalidOperation

produit_actuel = None
total_ca = Decimal("0")

for line in sys.stdin:

    try:
        # Séparer l'identifiant et le chiffre d'affaires
        produit_id, chiffre_affaires = line.strip().split("\t", 1)

        chiffre_affaires = Decimal(chiffre_affaires)

        # Vérifier si le produit est identique
        if produit_actuel == produit_id:
            total_ca += chiffre_affaires

        else:
            # Afficher le résultat du produit précédent
            if produit_actuel is not None:
                print(f"{produit_actuel}\t{total_ca:.2f}")

            # Initialiser le nouveau produit
            produit_actuel = produit_id
            total_ca = chiffre_affaires

    except (ValueError, InvalidOperation):
        continue


# Afficher le résultat du dernier produit
if produit_actuel is not None:
    print(f"{produit_actuel}\t{total_ca:.2f}")
