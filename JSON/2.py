import json

task = ['oleg', 24, ['Belarus', 'Russia']]
d = {'name': task[0], 'age': task[1], 'countries': task[2]}

with open("two.json", "w") as f:
    json.dump(d, f, indent=4)

