number = int(input('Введи число: '))
answer = (number//100) + ((number//10)%10) + (number%10)
print(answer)
