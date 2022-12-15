import json

task = ['oleg', 24, ['Belarus', 'Russia'], (24, 1), ['Moscow', 'Vladikavkaz', 'Krasnodar', 'Rostov', 'Nalchik']]
d = {'name': task[0],
     'age': task[1],
     'countries': [{'name': task[2][0],
                    'time': task[3][0],
                    'cities': []},
                   {'name': task[2][1],
                    'time':task[3][1],
                    'cities': task[4]}
                  ]
     }

with open("Dmitrichenkov-3.json", "w") as f:
    json.dump(d, f, indent=4)
