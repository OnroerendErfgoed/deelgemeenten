# -*- coding: utf-8 -*-

# Script to sync Provincie and Gemeentenamen through CRABpy. Requires
# installation.

import csv
from pathlib import Path

from crabpy.gateway.adressenregister import AdressenRegisterClient
from crabpy.gateway.adressenregister import Gateway


# api_key can be None safely.
# This is not a problem because getting provincie or gemeente does not do any calls
client = AdressenRegisterClient(
    base_url="https://api.basisregisters.vlaanderen.be",
    api_key=None,
)
adressenregister = Gateway(client)

_script_folder = Path().parent
CSV_FILE_PATH = _script_folder.parent / "data" / "csv" / "deelgemeenten.csv"

with CSV_FILE_PATH.open() as csvfile:
    reader = csv.DictReader(csvfile)
    fieldnames = reader.fieldnames
    data = list(reader)

for d in data:
    if provincie := adressenregister.get_provincie_by_niscode(d["provincie_id"]):
        d["provincie_naam"] = provincie.naam
    if gemeente := adressenregister.get_gemeente_by_niscode(d["gemeente_id"]):
        d["gemeente_naam"] = gemeente.naam()

with CSV_FILE_PATH.open(mode="w", newline="\n") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for d in data:
        writer.writerow(d)
