
#!/usr/bin/env python3

import sys
from decimal import Decimal, InvalidOperation

totaux = {}

for line in sys.stdin:
    try:
        client_id, montant = line.strip().split("\t", 1)
        montant = Decimal(montant)

        totaux[client_id] = totaux.get(
            client_id, Decimal("0")
        ) + montant

    except (ValueError, InvalidOperation):
        continue

top_10 = sorted(
    totaux.items(),
    key=lambda item: item[1],
    reverse=True
)[:10]

for client_id, total_ca in top_10:
    print(f"{client_id}\t{total_ca:.2f}")
