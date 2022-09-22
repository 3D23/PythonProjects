mySeconds = int(input('Введи количество секунд: '))
seconds_in_one_age = 365*24*60*60
Age = mySeconds//seconds_in_one_age
Answer = 1970 + Age
print(Answer)
