#! /usr/bin/env python3

class SecurePlant:
    def __init__(self, name:str, height:int, age:int, growth_factor:int):
        self.__name = name
        self.__height = height
        self.__age = age
        self.__growth_factor = growth_factor

    def get_info(self):
        print(f'{self.__name} ({self.__height}cm, {self.__age} days)')

    def get_name(self)->str:
        return self.__name

    def get_height(self)->int:
        return self.__height

    def get_age(self)->int:
        return self.__age

    def set_height(self, height:int):
        if height < 0:
            print(f'Invalid operation attempted: height {height}cm [REJECTED]')
            print('Security: Negative height rejected')
        else:
            self.__height = height
            print(f'Height updated: {height}cm [OK]')

    def set_age(self, age:int):
        if age< 0:
            print(f'Invalid operation attempted: age {age} days [REJECTED]')
            print('Security: Negative age rejected')
        else:
            self.__age = age
            print(f'Age updated: {age}cm [OK]')

if __name__ == '__main__':
    plant = SecurePlant('Monstera', 22, 120, 1.5)
    print('=== Garden Security System ===')
    print(f'Plant created: {plant.get_name()}')
    plant.set_age(220)
    plant.set_height(34)
    plant.set_height(-22)
    print('Current plant: ', end='')
    plant.get_info()
