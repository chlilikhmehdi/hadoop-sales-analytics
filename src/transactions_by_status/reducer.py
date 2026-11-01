
#!/usr/bin/env python3

import sys
from decimal import Decimal, InvalidOperation

statut_actuel = None
nombre_transactions = 0
total_ca = Decimal("0")

for line in sys.stdin:
    try:
        statut, nombre, montant = line.strip().split("\t")

        nombre = int(nombre)
        montant = Decimal(montant)

        if statut_actuel == statut:
            nombre_transactions += nombre
            total_ca += montant

        else:
            if statut_actuel is not None:
                print(
                    f"{statut_actuel}\t"
                    f"{nombre_transactions}\t"
                    f"{total_ca:.2f}"
                )

            statut_actuel = statut
            nombre_transactions = nombre
            total_ca = montant

    except (ValueError, InvalidOperation):
        continue

if statut_actuel is not None:
    print(
        f"{statut_actuel}\t"
        f"{nombre_transactions}\t"
        f"{total_ca:.2f}"
    )
