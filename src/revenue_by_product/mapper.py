
#!/usr/bin/env python3

import sys
import csv
from decimal import Decimal, InvalidOperation

# Charger les produits
produits = {}

with open("produits.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        produit_id = row["produit_id"].strip()
        nom_produit = row["nom_produit"].strip()

        if produit_id:
            produits[produit_id] = nom_produit


# Lire les transactions depuis l'entrée standard
reader = csv.DictReader(sys.stdin)

for row in reader:
    try:
        # Récupérer les informations de la transaction
        produit_id = row["produit_id"].strip()
        quantite = Decimal(row["quantite"])
        prix_unitaire = Decimal(row["prix_unitaire"])

        # Vérifier l'existence du produit
        if produit_id not in produits:
            continue

        # Récupérer le nom du produit
        nom_produit = produits[produit_id]

        # Calculer le chiffre d'affaires
        chiffre_affaires = quantite * prix_unitaire

        # Envoyer produit et chiffre d'affaires
        print(f"{produit_id}\t{chiffre_affaires}")

    except (KeyError, ValueError, InvalidOperation, TypeError):
        continue
