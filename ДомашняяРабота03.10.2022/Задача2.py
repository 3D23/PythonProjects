s = input('Введите строку: ')
answer_s = ''
count = 1
for i in range(0,len(s)-1):
    if (s[i] == s[i+1]):
        count += 1
    else:
        answer_s += str(count) + s[i]
        count = 1
print(answer_s + str(count) + s[len(s)-1])