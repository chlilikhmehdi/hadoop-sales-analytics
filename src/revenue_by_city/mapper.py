
#!/usr/bin/env python3

import sys
import csv
from decimal import Decimal, InvalidOperation

# Charger les clients et leurs villes
clients = {}

with open("clients.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        client_id = row["client_id"].strip()
        ville = row["ville"].strip()

        if client_id and ville:
            clients[client_id] = ville


# Lire les transactions depuis l'entrée standard
reader = csv.DictReader(sys.stdin)

for row in reader:
    try:
        # Récupérer les informations de la transaction
        client_id = row["client_id"].strip()
        quantite = Decimal(row["quantite"])
        prix_unitaire = Decimal(row["prix_unitaire"])

        # Vérifier si le client existe
        if client_id not in clients:
            continue

        # Récupérer la ville du client
        ville = clients[client_id]

        # Calculer le chiffre d'affaires
        chiffre_affaires = quantite * prix_unitaire

        # Envoyer ville et chiffre d'affaires
        print(f"{ville}\t{chiffre_affaires}")

    except (KeyError, ValueError, InvalidOperation, TypeError):
        continue
