
#!/usr/bin/env python3

import sys
import csv
from decimal import Decimal, InvalidOperation

reader = csv.DictReader(sys.stdin)

for row in reader:
    try:
        client_id = row["client_id"].strip()
        quantite = Decimal(row["quantite"])
        prix_unitaire = Decimal(row["prix_unitaire"])

        chiffre_affaires = quantite * prix_unitaire

        if client_id:
            print(f"{client_id}\t{chiffre_affaires}")

    except (KeyError, ValueError, InvalidOperation, TypeError):
        continue
