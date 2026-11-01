
#!/usr/bin/env python3

import sys

client_actuel = None
nombre_transactions = 0

for line in sys.stdin:
    try:
        client_id, valeur = line.strip().split("\t")
        valeur = int(valeur)

        if client_actuel == client_id:
            nombre_transactions += valeur
        else:
            if client_actuel is not None:
                print(f"{client_actuel}\t{nombre_transactions}")

            client_actuel = client_id
            nombre_transactions = valeur

    except ValueError:
        continue

if client_actuel is not None:
    print(f"{client_actuel}\t{nombre_transactions}")
