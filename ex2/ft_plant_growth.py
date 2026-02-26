#! /usr/bin/env python3


class Plant:
    name: str
    height: int
    original_height: int
    p_age: int

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.p_age} days old")

    def age(self) -> None:
        self.p_age += 1

    def grow(self) -> None:
        self.height += 1


if __name__ == "__main__":
    plant = Plant()
    plant.name = "Rose"
    plant.height = 25
    plant.p_age = 30
    plant.original_height = 25

    print("== Day 1 ==")
    plant.get_info()

    for days in range(6):
        plant.age()
        plant.grow()

    print("== Day 7 ==")
    plant.get_info()

    print(f"Growth this week: +{plant.height - plant.original_height}cm")
