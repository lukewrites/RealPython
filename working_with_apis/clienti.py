import json

output = json.load(open('cars.json'))

print output[0]["CAR"][3]["MODEL"]