def F1(animal,name,age):
    if (animal != None) and (name != None) and (age != None):
        print('Animal:', animal)
        print('Name:', name)
        print('Age:',age)

F1(name = input('Введите имя: '),animal = input('Введите животное: '),age = int(input('Введите возраст: ')))