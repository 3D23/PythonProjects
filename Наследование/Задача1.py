class Hero():
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor

    def print_info(self):
        print('Уровень здоровья: ', self.health)
        print('Класс брони: ', self.armor)

class Magician(Hero):
    def hello(self):
        super().print_info()

    def attack(self):
        print('Волшебник берёт свою палку и бьёт ей по башне врага')
        print('Большая сила удара (23)')

magician = Magician('kjj',1, 23)
magician.hello()