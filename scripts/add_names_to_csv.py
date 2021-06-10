# -*- coding: utf-8 -*-

# Script to sync Provincie and Gemeentenamen through CRABpy. Requires
# installation.

import csv

from crabpy.client import crab_factory

from crabpy.gateway.crab import CrabGateway

crab = CrabGateway(crab_factory())

FILENAME = '../data/csv/deelgemeenten.csv'

data = []
with open(FILENAME, 'r', newline='') as csvfile:
    reader= csv.DictReader(
        csvfile,
    )

    fieldnames = reader.fieldnames
    for b in reader:
        data.append(b)

for d in data:
    d['provincie_naam'] = crab.get_provincie_by_id(int(d['provincie_id'])).naam
    d['gemeente_naam'] = crab.get_gemeente_by_niscode(int(d['gemeente_id'])).naam

with open(FILENAME, 'w', newline='\n') as csvfile:
    writer = csv.DictWriter(
        csvfile,
        fieldnames=fieldnames
    )

    writer.writeheader()
    for d in data:
        writer.writerow(d)
