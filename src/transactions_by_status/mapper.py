
#!/usr/bin/env python3

import sys
import csv
from decimal import Decimal, InvalidOperation

reader = csv.DictReader(sys.stdin)

for row in reader:
    try:
        statut = row["statut"].strip().lower()

        quantite = Decimal(row["quantite"])
        prix_unitaire = Decimal(row["prix_unitaire"])

        chiffre_affaires = quantite * prix_unitaire

        if statut in ("validée", "validee", "annulée", "annulee"):
            print(f"{statut}\t1\t{chiffre_affaires}")

    except (KeyError, ValueError, InvalidOperation, TypeError):
        continue
