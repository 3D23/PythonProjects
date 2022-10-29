grades = [{'name': 'Jennifer', 'final': 95},
     {'name': 'David', 'final': 92},
    {'name': 'Aaron', 'final': 98}]
names = ['']*len(grades)
sorted_grades_names = sorted(grades, key = lambda x : x['name'])
print(sorted_grades_names)