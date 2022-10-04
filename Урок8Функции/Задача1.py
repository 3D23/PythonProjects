def badge(_name,_group):
    print('"Колледж Сириус"')
    print('Имя:',_name)
    print('Группа',_group)

count = int(input('Введите количество учеников:'))
for i in range(count):
    name = input('Введите ФИО: ')
    group = input('Введите группу: ')
    badge(name,group)