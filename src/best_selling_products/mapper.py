
#!/usr/bin/env python3

import sys
import csv

reader = csv.DictReader(sys.stdin)

for row in reader:
    try:
        produit_id = row["produit_id"].strip()
        quantite = int(row["quantite"])

        if produit_id:
            print(f"{produit_id}\t{quantite}")

    except (KeyError, ValueError, TypeError):
        continue
