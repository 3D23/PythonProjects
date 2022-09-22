food = input()
food = food.lower()
if (food == 'завтрак'):
    print('Каша')
elif (food != 'завтрак'):
    print('Ты хочешь плотно поесть?')
    goodMeal = input()
    goodMeal = goodMeal.lower()
    if (goodMeal == 'да'):
        print('Плов')
    else:
        print('Котлета с пюре')