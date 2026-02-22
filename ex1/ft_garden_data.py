#!/usr/bin/env python3

class Plant:
    name:str = ''
    height:int = 0
    age:int = 0

    def get_info(self):
        print(f'{self.name}: {self.height}cm, {self.age} days old')

if __name__ == '__main__':
    rose = Plant()
    rose.name = 'Rose'
    rose.height = 25
    rose.age = 30

    monstera = Plant()
    monstera.name = 'Monstera'
    monstera.height = 70
    monstera.age = 120

    cactus = Plant()
    cactus.name = 'cactus'
    cactus.height = 15
    cactus.age = 78

    plants = [rose, monstera, cactus]

    print("=== Garden Plant Registry ==")
    for plant in plants:
        plant.get_info()
