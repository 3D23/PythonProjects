class SpaceObject():
    def __init__(self, size):
        self.size = size

class Star(SpaceObject):
    def __init__(self, brightness, size):
        super().__init__(size)
        self.brightness = brightness

    def shine(self):
        print('Звезда светит с яркостью: ', self.brightness)

class Planet(SpaceObject):
    def __init__(self, population, growth, size):
        super().__init__(size)
        self.population = population
        self.growth = growth

    def print(self, year):
        print('Через ' + str(year) + ' лет население будет: ' + str(year * self.growth + self.population))

star = Star(40, 10)
star.shine()

planet = Planet(300, 20, 943)
planet.print(30)

