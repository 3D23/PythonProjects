surname = input('Введите фамилию: ')
Post = input('Введите должность: ')
countList = []
count = int(input('Введите количество учеников (0 - закончить ввод): '))
while (count != 0):
    countList.append(count)
    count = int(input('Введите количество учеников (0 - закончить ввод): '))
personalInformation = [surname,Post,countList]
print(personalInformation)