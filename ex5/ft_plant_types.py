#! /usr/bin/env python3

class Plant:
    def __init__(self, name:str, height:int, age:int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f'{self.name} ({self.height}cm, {self.age} days)')

class Flower(Plant):
    def __init__(self, name:str, height:int, age:int, color:str):
        super().__init__(name, height, age)
        self.color = color

    def get_info(self):
        print(f'{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color')

    def bloom(self):
        print(f'{self.name} is blooming beautifuly')

class Tree(Plant):
    def __init__(self, name:str, height:int, age:int, trunk_diameter:int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_info(self):
        print(f'{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter')

    def produce_shade(self):
        print(f'{self.name} provides {self.trunk_diameter} square meters of shade')

class Vegetable(Plant):
    def __init__(self, name:str, height:int, age:int, harvest_season:str, nutritional_value:str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        print(f'{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest')

    def get_nutritional_facts(self):
        print(f'{self.name} is rich in {self.nutritional_value}')

if __name__ == '__main__':
    flowers:list(Flower) = [
        Flower('Rose', 25, 60, 'red'),
        Flower('Lavender', 34, 67, 'purple')
    ]
    trees:list(Tree) = [
        Tree('Oak', 500, 1825, 50),
        Tree('Bamboo', 350, 67, 10)
    ]
    vegetables:list(Vegetable) = [
        Vegetable('Carrot', 15, 102, 'Autumn', 'vitamin A'),
        Vegetable('tomato', 56, 68, 'Spring', 'vitamin C')
    ]

    print('== Garden Plant Types ==')

    for flower in flowers:
        flower.get_info()
        flower.bloom()

    for tree in trees:
        tree.get_info()
        tree.produce_shade()

    for vegetable in vegetables:
        vegetable.get_info()
        vegetable.get_nutritional_facts()
