symbols_one = ['А','Я','Г','М']
symbols_two = ['О','Ь','Л','Н']
name = input('Введите своё имя (off - выйти): ')
while (name.lower() != 'off'):
    if (name.upper()[-1] in symbols_one):
       a = lambda _name : _name + ' - гений'
       print(a(name))
    elif (name.upper()[-1] in symbols_two):
        b = lambda _name : _name + ' - сверхразум'
        print(b(name))
    else:
        c = lambda  _name : 'Просто ' +  _name
        print(c(name))
    name = input('Введите своё имя (off - выйти): ')