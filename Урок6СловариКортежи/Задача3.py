all_information = input('Введите через запятую: место в чарте, исполнитель, название (off - для выхода)')
while (all_information != 'off'):
    chart,singer,name = all_information.split(',')
    plus = '('+chart+','+singer+')'
    all_informationd = {plus:name}
    print(all_informationd)
    del all_informationd[plus]
    all_information = input('Введите через запятую: место в чарте, исполнитель, название (off - для выхода)')

