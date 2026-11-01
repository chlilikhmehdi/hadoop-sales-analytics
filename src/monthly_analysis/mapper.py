
#!/usr/bin/env python3

import sys
import csv
from datetime import datetime
from decimal import Decimal, InvalidOperation

# Lire les transactions depuis l'entrée standard
reader = csv.DictReader(sys.stdin)

# Correspondance entre numéro et nom du mois
MOIS = {
    1: "Janvier",
    2: "Fevrier",
    3: "Mars",
    4: "Avril",
    5: "Mai",
    6: "Juin",
    7: "Juillet",
    8: "Aout",
    9: "Septembre",
    10: "Octobre",
    11: "Novembre",
    12: "Decembre"
}

for row in reader:
    try:
        # Récupérer la date
        date_transaction = row["date"].strip()

        # Convertir la date
        date_obj = datetime.strptime(
            date_transaction, "%Y-%m-%d"
        )

        # Extraire le mois
        mois = MOIS[date_obj.month]

        # Récupérer quantité et prix
        quantite = Decimal(row["quantite"])
        prix_unitaire = Decimal(row["prix_unitaire"])

        # Calculer le chiffre d'affaires
        chiffre_affaires = quantite * prix_unitaire

        # Envoyer mois et chiffre d'affaires
        print(f"{date_obj.month:02d}-{mois}\t{chiffre_affaires}")

    except (KeyError, ValueError, InvalidOperation, TypeError):
        continue
