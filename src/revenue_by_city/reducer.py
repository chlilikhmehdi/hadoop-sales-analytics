
#!/usr/bin/env python3

import sys
from decimal import Decimal, InvalidOperation

ville_actuelle = None
total_ca = Decimal("0")

for line in sys.stdin:

    try:
        # Séparer la ville et le chiffre d'affaires
        ville, chiffre_affaires = line.strip().split("\t", 1)

        chiffre_affaires = Decimal(chiffre_affaires)

        # Vérifier si la ville est identique
        if ville_actuelle == ville:
            total_ca += chiffre_affaires

        else:
            # Afficher le résultat de la ville précédente
            if ville_actuelle is not None:
                print(f"{ville_actuelle}\t{total_ca:.2f}")

            # Initialiser une nouvelle ville
            ville_actuelle = ville
            total_ca = chiffre_affaires

    except (ValueError, InvalidOperation):
        continue


# Afficher le résultat de la dernière ville
if ville_actuelle is not None:
    print(f"{ville_actuelle}\t{total_ca:.2f}")
