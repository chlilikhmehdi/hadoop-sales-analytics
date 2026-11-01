#!/usr/bin/env python3

import sys
import csv

reader = csv.DictReader(sys.stdin)

for row in reader:
    try:
        vendeur_id = row["vendeur_id"]
        quantite = float(row["quantite"])
        prix_unitaire = float(row["prix_unitaire"])

        chiffre_affaires = quantite * prix_unitaire

        print(f"{vendeur_id}\t{chiffre_affaires}")

    except (ValueError, KeyError, TypeError):
        continue