
#!/usr/bin/env python3

import sys
from decimal import Decimal, InvalidOperation

mois_actuel = None
total_ca = Decimal("0")

for line in sys.stdin:

    try:
        # Séparer le mois et le chiffre d'affaires
        mois, chiffre_affaires = line.strip().split("\t", 1)

        chiffre_affaires = Decimal(chiffre_affaires)

        # Vérifier si le mois est identique
        if mois_actuel == mois:
            total_ca += chiffre_affaires

        else:
            # Afficher le résultat du mois précédent
            if mois_actuel is not None:
                print(f"{mois_actuel}\t{total_ca:.2f}")

            # Initialiser le nouveau mois
            mois_actuel = mois
            total_ca = chiffre_affaires

    except (ValueError, InvalidOperation):
        continue


# Afficher le dernier mois
if mois_actuel is not None:
    print(f"{mois_actuel}\t{total_ca:.2f}")
