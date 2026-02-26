#! /usr/bin/env python3


class Plant:
    name: str
    height: int
    original_height: int
    p_age: int

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.original_height = height
        self.p_age = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.p_age} days old")

    def age(self) -> None:
        self.p_age += 1

    def grow(self) -> None:
        self.height += 1


class Flower(Plant):
    color: str
    is_blooming: bool

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = True

    def get_info(self) -> None:
        print(
            f"\n{self.name} (Flower): {self.height}cm, {self.p_age} days, "
            + f"{self.color} color"
        )

    def bloom(self) -> None:
        self.is_blooming = True
        print(f"{self.name} is blooming beautifuly")


class Tree(Plant):
    trunk_diameter: int

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int)\
            -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_info(self) -> None:
        print(
            f"\n{self.name} (Tree): {self.height}cm, {self.p_age} days, "
            + f"{self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        print(f"{self.name} provides {self.trunk_diameter} square "
              + "meters of shade")


class Vegetable(Plant):
    harvest_season: str
    nutritional_value: str

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        print(
            f"\n{self.name} (Vegetable): {self.height}cm, {self.p_age} days,"
            + f" {self.harvest_season} harvest"
        )

    def get_nutritional_facts(self):
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    plants = [
        Flower("Rose", 25, 30, "red"),
        Flower("Lavender", 34, 67, "purple"),
        Tree("Oak", 500, 1825, 50),
        Tree("Bamboo", 350, 67, 10),
        Vegetable("tomato", 80, 90, "Summer", "vitamin C"),
        Vegetable("Carrot", 15, 102, "Autumn", "vitamin A"),
    ]

    print("== Garden Plant Types ==")
    for plant in plants:
        plant.get_info()
        if plant.__class__ == Flower:
            plant.bloom()
        elif plant.__class__ == Tree:
            plant.produce_shade()
        elif plant.__class__ == Vegetable:
            plant.get_nutritional_facts()
