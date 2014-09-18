import json

output = json.load(open('cars.json'))

print json.dumps(output, indent=1, sort_keys=True)