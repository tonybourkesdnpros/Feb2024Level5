
import json

file = open('results.json', 'r')

results = json.load(file)

for interface in results['result'][0]['interfaces']:
    print(interface+':', results['result'][0]['interfaces'][interface]['interfaceAddress']['ipAddr']['address'])


