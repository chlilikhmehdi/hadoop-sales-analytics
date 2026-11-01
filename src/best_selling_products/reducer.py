
#!/usr/bin/env python3

import sys

produit_actuel = None
quantite_totale = 0

for line in sys.stdin:
    try:
        produit_id, quantite = line.strip().split("\t")
        quantite = int(quantite)

        if produit_actuel == produit_id:
            quantite_totale += quantite
        else:
            if produit_actuel is not None:
                print(f"{produit_actuel}\t{quantite_totale}")

            produit_actuel = produit_id
            quantite_totale = quantite

    except ValueError:
        continue

if produit_actuel is not None:
    print(f"{produit_actuel}\t{quantite_totale}")
