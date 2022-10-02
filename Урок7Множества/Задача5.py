help_dict = {}
count = int(input('Введите сколько всего учеников: '))
answerSet1 = set()
answerSet2 = set()
while (count > 0):
    print('Введите количество учеников: (осталось:',count,')')
    num = int(input())
    count -= num
    if (count < 0):
        print('Превышено число учеников.')
        exit()
    lan = input('Какие языки знают? (Введите "off", для того чтобы прекратить)')
    lan_set = set()
    while (lan != 'off'):
        lan_set.add(lan)
        lan = input('Какие языки знают? (Введите "off", для того чтобы прекратить)')
    frozen_lan_set = frozenset(lan_set)
    help_dict[frozen_lan_set] = num
    answerSet1 = lan_set
    answerSet2 = lan_set
for i in help_dict.keys():
    answerSet1 = answerSet1 | i
for i in help_dict.keys():
    answerSet2 = answerSet2 & i
answer1 = 0
answer2 = 0
for i in help_dict.keys():
    if (answerSet1 == i):
        answer1 = help_dict[i]
    if (answerSet2 == i):
        answer2 = help_dict[i]
print(answer1,'-', list(answerSet1))
print(answer2,'-',list(answerSet2))
