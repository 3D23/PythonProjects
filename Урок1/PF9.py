number = int(input('Введи число: '))
first = number//100
second = (number//10)%10
third =  number%10
print(third*100 + second*10 + first)