
#!/usr/bin/env python3

import sys
import csv

reader = csv.DictReader(sys.stdin)

for row in reader:
    try:
        client_id = row["client_id"].strip()

        if client_id:
            print(f"{client_id}\t1")

    except (KeyError, AttributeError):
        continue
