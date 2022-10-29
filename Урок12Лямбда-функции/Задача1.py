name = input('Введите своё имя (off - выйти): ')
while (name.lower() != 'off'):
     answer = lambda _name : _name + ' - гений'
     print(answer(name))
     name = input('Введите своё имя (off - выйти): ')