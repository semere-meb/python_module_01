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
        print(f"({self.name}: {self.height}cm, {self.p_age} days)")

    def age(self) -> None:
        self.p_age += 1

    def grow(self) -> None:
        self.height += 1


if __name__ == "__main__":
    plants: list(Plant) = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]
    print("=== Plant Factory Output ==")
    count = 0
    for plant in plants:
        print("Created: ", end="")
        plant.get_info()
        count += 1
    print(f"\nTotal plants created: {count}")
