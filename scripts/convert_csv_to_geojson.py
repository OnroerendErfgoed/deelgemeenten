# -*- coding: utf-8 -*-

import csv
import json

geojsonfile = open('../data/json/deelgemeenten.geojson', 'w')
jsonfile = open('../data/json/deelgemeenten.json', 'w')

geojsondata = {
    "type": "FeatureCollection",
    "features": [
    ]
}

jsondata = []

with open('../data/csv/deelgemeenten.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, quotechar='"')
    headers = []
    for row in reader:
        if headers == []:
            headers = row
            continue
        props= {
            headers[0]: row[0],
            headers[1]: row[1],
            headers[2]: row[2],
            headers[3]: row[3]
        }
        jsondata.append(props)
        f = {
            "type": "Feature",
            "properties": props
        }
        geojsondata['features'].append(f)

json.dump(geojsondata, geojsonfile, indent=4, sort_keys=True)
json.dump(jsondata, jsonfile, indent=4, sort_keys=True)
