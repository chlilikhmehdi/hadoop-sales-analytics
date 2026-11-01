
#!/usr/bin/env python3

import sys
from decimal import Decimal, InvalidOperation

categorie_actuelle = None
total_ca = Decimal("0")

for line in sys.stdin:
    try:
        categorie, montant = line.strip().split("\t", 1)
        montant = Decimal(montant)

        if categorie_actuelle == categorie:
            total_ca += montant
        else:
            if categorie_actuelle is not None:
                print(f"{categorie_actuelle}\t{total_ca:.2f}")

            categorie_actuelle = categorie
            total_ca = montant

    except (ValueError, InvalidOperation):
        continue

if categorie_actuelle is not None:
    print(f"{categorie_actuelle}\t{total_ca:.2f}")
