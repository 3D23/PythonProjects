class Human():

    def quack(self):
        print('Имитирует кряканье')

    def wear_clothes(self):
        print('Носит одежду')
class Duck():

    def quack(self):
        print('Крякает')

human_one = Human()
duck_one = Duck()
human_one.wear_clothes()
for i in [human_one, duck_one]:
    i.quack()


