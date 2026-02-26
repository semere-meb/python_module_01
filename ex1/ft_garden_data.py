#!/usr/bin/env python3


class Plant:
    name: str
    height: int
    age: int

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plant_info = [
        ("Rose", 25, 30),
        ("sunflower", 80, 45),
        ("Cactus", 15, 120),
    ]
    plants = []
    for info in plant_info:
        plant = Plant()
        plant.name = info[0]
        plant.height = info[1]
        plant.age = info[2]
        plants += [plant]

    print("=== Garden Plant Registry ==")
    for plant in plants:
        plant.get_info()
