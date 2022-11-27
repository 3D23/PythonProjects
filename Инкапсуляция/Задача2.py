from random import randint
from time import *

class Hero():

    def __init__(self, name, health, armor, power, weapon, hit_percentage, chance_for_a_critical_hit, critical_hit, rank):

        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon
        self.hit_percentage = hit_percentage
        self.chance_for_a_critical_hit = chance_for_a_critical_hit
        self.critical_hit = critical_hit
        self.count_heal_big = 1
        self.count_heal_middle = 1
        self.count_heal_small = 1
        self.max_heal = health
        self.__rank = rank

    def create_hero(self, enemy):

        self.name = 'лллл'
        self.health = randint(enemy.health - 15, enemy.health + 15)
        self.armor = randint(enemy.armor - 10, enemy.armor + 10)
        self.power = randint(enemy.power - 10, enemy.power + 10)
        self.weapon = 'дддлдд'
        self.hit_percentage = randint(1, 100)
        self.chance_for_a_critical_hit = randint(1, 100)
        self.critical_hit = randint(1, 300)
        self.count_heal_big = 1
        self.count_heal_middle = 1
        self.count_heal_small = 1
        self.max_heal = health
        self.__rank = ''

    def getrank(self):
        return self.__rank

    def setrank(self):
        self.__rank = 'Победитель арены'

    def delrank(self):
        del self.__rank

    def print_info(self):

        print(self.name)
        print('Уровень здоровья: ', self.health)
        print('Класс брони:', self.armor)
        print('Сила удара:', self.power)
        print('Оружие:', self.weapon)
        print('Шанс промаха:',self.hit_percentage)
        print('Шанс Крит.удара:',self.chance_for_a_critical_hit)
        print('Крит.Урон:',self.critical_hit)
        print('Количество больших зелий здоровья:',self.count_heal_big)
        print('Количество средних зелий здоровья:',self.count_heal_middle)
        print('Количество малых зелий здоровья:', self.count_heal_small)

    def info_heroes(self, enemy):

        print('Ваш персонаж: ')
        print('Имя', self.name)
        print('Уровень здоровья героя:', self.health)
        print('Класс брони:', self.armor)
        print('Сила удара:', self.power)
        print('Оружие:', self.weapon)
        print('Шанс промаха:', self.hit_percentage)
        print('Шанс Крит.удара:', self.chance_for_a_critical_hit)
        print('Крит.Урон:', self.critical_hit)
        print()
        print('Противник: ')
        print('Имя', enemy.name)
        print('Уровень здоровья героя:', enemy.health)
        print('Класс брони:', enemy.armor)
        print('Сила удара:', enemy.power)
        print('Оружие:', enemy.weapon)
        print('Шанс промаха:', enemy.hit_percentage)
        print('Шанс Крит.удара:', enemy.chance_for_a_critical_hit)
        print('Крит.Урон:', enemy.critical_hit)

    def step_print_info_attack(self):  # После каждой атаки должно выводится

        print(self.name)
        print('Уровень здоровья героя:', self.health)
        print('Класс брони:', self.armor)
        print('Сила удара:', self.power)
        print()

    def step_print_info_defence(self):   # После каждой защиты должна выводится

        print(self.name)
        print('Уровень здоровья героя:', self.health)
        print('Класс брони:', self.armor)
        print()

    def strike(self, enemy):    # Атака

        strike = self.power
        crit_chance = randint(1,100)
        percentage_chance = randint(1,100)
        if percentage_chance <= self.hit_percentage:
            print('Промах!!')
            return

        if crit_chance <= self.chance_for_a_critical_hit:
            strike += strike * (self.critical_hit / 100)

        if (strike > self.power):
            print('Удар ->')
            print('Критический удар!!!! Нанесено урона:', strike)
        else:
            print('Удар ->')
            print('Нанесено урона:', strike)

        if enemy.armor > 0:
            enemy.armor -= strike

            if (enemy.armor < 0):
                enemy.health -= abs(enemy.armor)
                enemy.armor = 0

        elif enemy.armor == 0:
            enemy.health -= strike

        enemy.step_print_info_defence()

    def info_commands(self):                                    # Информация о всех существующих командах

        print('/attack - атаковать противника')
        print('/big_heal - вылечится большим зельем здоровья')
        print('/middle_heal - вылечится средним зельем здоровья')
        print('/small_heal - вылечится малым зельем здоровья')
        print('/inventory - посмотреть инвентарь')

    def info_inventory(self, enemy):   # Информация об инвентаре

        print('Ваш инвентарь')
        print('Оружие:',self.weapon)
        print('Количество малых зелий:',self.count_heal_small)
        print('Количество средних зелий:',self.count_heal_middle)
        print('Количество больших зелий:',self.count_heal_big)
        print()
        print('Инвентарь противника: ')
        print('Оружие:', enemy.weapon)
        print('Количество малых зелий:', enemy.count_heal_small)
        print('Количество средних зелий:', enemy.count_heal_middle)
        print('Количество больших зелий:', enemy.count_heal_big)

    def command_use(self, command, enemy):

        if command == '/small_heal' or command == '/middle_heal' or command == '/big_heal':
            self.healing(command)
        elif command == '/attack':
            self.strike(enemy)

    def healing(self, command):
        if (self.health > 0):
           if command == '/small_heal':
                if self.count_heal_small > 0:
                    self.health += self.max_heal * 0.1
                    if self.health > self.max_heal:
                        self.health = self.max_heal
                    print('Лечение')
                    sleep(2)
                    print('Восстановлено',self.max_heal * 0.1,'очков здоровья')
                    print('Ваше здоровье: ',self.health)
                    self.count_heal_small -= 1
                else:
                    print('Не хватает зелий лечения')
           elif (command == '/middle_heal'):
                if self.count_heal_middle > 0:
                    self.health += self.max_heal * 0.2
                    if self.health > self.max_heal:
                        self.health = self.max_heal
                    print('Лечение')
                    sleep(2)
                    print('Восстановлено',self.max_heal * 0.2,'очков здоровья')
                    print('Ваше здоровье: ', self.health)
                    self.count_heal_middle -= 1
                else:
                    print('Не хватает зелий лечения')

           elif (command == '/big_heal'):
              if self.count_heal_big > 0:
                 self.health += self.max_heal * 0.3
                 if self.health > self.max_heal:
                    self.health = self.max_heal
                 print('Лечение')
                 sleep(2)
                 print('Восстановлено',self.max_heal * 0.3,'очков здоровья')
                 print('Ваше здоровье: ', self.health)
                 self.count_heal_big -= 1
              else:
                 print('Не хватает зелий лечения')

    def step_enemy(self, enemy):

        if self.power >= enemy.health:
            self.strike(enemy)
        elif self.health <= self.max_heal * 0.1 and self.count_heal_big > 0:
            command = '/big_heal'
            self.healing(command)
        elif self.health <= self.max_heal * 0.2 and self.count_heal_middle > 0:
            command = '/middle_heal'
            self.healing(command)
        elif self.health <= self.max_heal * 0.3 and self.count_heal_small > 0:
            command = '/small_heal'
            self.healing(command)
        else:
            self.strike(enemy)

print('Создайте своего персонажа: ')
name = input('Введите имя:')
health = int(input('Введите количество здоровья: '))
armor = int(input('Введите количество брони: '))
power = int(input('Введите силу: '))
weapon = input('Введите оружие: ')
hit_percentage = int(input('Введите шанс промаха: '))
chance_for_a_critical_hit = int(input('Введите Крит.шанс: '))
critical_hit = int(input('Введите Критически урон: '))
knight_one = Hero(name, health, armor, power, weapon, hit_percentage, chance_for_a_critical_hit, critical_hit,"bez ranga")
knight_two = Hero('', 0, 0, 0, '', 0, 0, 0, '')
print('Создание противника...')
knight_two.create_hero(knight_one)
sleep(2)
print('Поприветсвуйте героев:\n ')
knight_one.print_info()
print()
knight_two.print_info()
print('Бой начинается!!!\n')

while knight_one.health > 0 and knight_two.health > 0:

    print('Ваш Ход')
    knight_one.info_commands()
    knight_one.step_print_info_attack()
    command = input('Что вы хотите сделать?')

    while command == '/inventory':
        knight_one.info_inventory(knight_two)
        command = input('Что вы хотите сделать?')
    knight_one.command_use(command, knight_two)
    print()
    print('Ход противника...')
    sleep(5)
    if knight_two.health > 0:
        knight_two.step_enemy(knight_one)

if (knight_one.health <= 0):
    print('Вы проиграли!!!')
    knight_one.delrank()
    knight_two.setrank()
    print(knight_two.getrank())

elif (knight_two.health <= 0):
    print('Вы выиграли!!!')
    knight_one.setrank()
    knight_two.delrank()
    print(knight_one.getrank())

