#! /usr/bin/env python3


class Plant:
    __name = ""
    __height = 0
    __age = 0
    __growth_factor = 0

    def __init__(self, name: str, height: int, age: int, growth_factor: int):
        self.__name = name
        self.__height = height
        self.__age = age
        self.__growth_factor = growth_factor

    def get_info(self):
        print(f"{self.__name} ({self.__height}cm, {self.__age} days)")

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def grow(self, days: int):
        self.height += self.growth_factor * days
        print(f"{self.__name} grew {self.__growth_factor}cm")

    @staticmethod
    def is_valid(val: int) -> bool:
        if val < 0:
            return False
        return True

    def set_height(self, height: int):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {age}cm [OK]")


class FloweringPlant(Plant):
    __color = ""
    __is_blooming = False

    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.__color = color

    def get_info(self):
        print(
            f"{self.get_name()}: {self.get_height()}cm, {self.__color} \
            flowers{' (blooming)' if self.__is_blooming else ''}"
        )

    def bloom(self):
        print(f"{self.get_name()} is blooming beautifuly")
        self.__is_blooming = True

    def get_color(self) -> str:
        return self.__color


class PrizeFlower(FloweringPlant):
    def __init__(
        self, name: str, height: int, age: int, color: str, prize_points: int
    ) -> None:
        super().__init__(name, height, age)
        self.prize_points = prize_points

    def get_info(self):
        print(
            f"{self.name}: {self.height}cm, {self.color} flowers{
                ' (blooming)' if self.is_blooming else ''
            }, Prize points: {self.prize_points}"
        )


class Garden:
    name = ""
    owner = ""
    plants = []
    plant_count = 0

    def __init__(self, name: str, owner: str) -> str:
        self.name = name
        self.owner = owner

    def add_plant(self, plant: Plant):
        self.plants[:0] = plant
        self.plant_count += 1


class GardenManager:
    manager_name = ""
    gardens = []

    def __init__(self, name: str, gardens: list(Garden)) -> None:
        self.manager_name = name
        self.gardens = gardens

    @classmethod
    def create_garden_network(cls, name: str, gardens: list(Garden)) -> object:
        if name == "":
            return None
        return GardenManager(name, gardens)

    def add_garden(self, garden: Garden):
        self.gardens + [garden]

    class GardenStats:
        def get_total_points(self):
            count = 0
            for garden in self.gardens:  # TODO: self.gardens available?
                for plant in garden:
                    if plant.__class__ == "PrizePlant":
                        count += 0
            return count


if __name__ == "__main__":
    pass
