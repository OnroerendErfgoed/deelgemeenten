# -*- coding: utf-8 -*-

import csv
import json

jsonfile = open('../data/json/deelgemeente.json', 'w')

data = {
    "type": "FeatureCollection",
    "features": [
    ]
}

with open('../data/csv/deelgemeenten.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    headers = []
    for row in reader:
        if headers == []:
            headers = row
            continue
        f = {
            "type": "Feature",
            "properties": {
                headers[0]: row[0],
                headers[1]: row[1],
                headers[2]: row[2],
                headers[3]: row[3]
            }
        }
        data['features'].append(f)

json.dump(data, jsonfile)
