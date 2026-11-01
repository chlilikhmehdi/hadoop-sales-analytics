
#!/usr/bin/env python3

import sys
import csv
from decimal import Decimal, InvalidOperation

# Charger les catégories depuis produits.csv
produits = {}

with open(
    "produits.csv",
    "r",
    encoding="utf-8-sig",
    newline=""
) as file:

    reader = csv.DictReader(file)

    for row in reader:
        produit_id = row["produit_id"].strip()
        categorie = row["categorie"].strip()

        if produit_id and categorie:
            produits[produit_id] = categorie

# Lire les transactions
reader = csv.DictReader(sys.stdin)

for row in reader:
    try:
        produit_id = row["produit_id"].strip()

        quantite = Decimal(row["quantite"])
        prix_unitaire = Decimal(row["prix_unitaire"])

        if produit_id not in produits:
            continue

        categorie = produits[produit_id]

        chiffre_affaires = quantite * prix_unitaire

        print(f"{categorie}\t{chiffre_affaires}")

    except (KeyError, ValueError, InvalidOperation, TypeError):
        continue
