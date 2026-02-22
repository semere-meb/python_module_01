#! /usr/bin/env python3

class Plant:
    def __init__(self, name:str, height:int, age:int, growth_factor:int):
        self.name = name
        self.height = height
        self.p_age = age
        self.growth_factor = growth_factor

    def get_info(self):
        print(f'{self.name} ({self.height}cm, {self.p_age} days)')

    def age(self, days:int):
        self.p_age += 1

    def grow(self, days:int):
        self.height += self.growth_factor * days

if __name__ == '__main__':
    plants:list(Plant) = [
        Plant('Rose', 25, 30),
        Plant('Monstera', 70, 120),
        Plant('Cactus', 25, 30)
    ]
    count = 0

    print("=== Plant Factory Output ==")

    for plant in plants:
        print('Created: ', end='')
        plant.get_info()
        count += 1

    print(f'\nTotal plants created: {count}')

