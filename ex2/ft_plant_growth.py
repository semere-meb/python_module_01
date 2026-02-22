#! /usr/bin/env python3


class Plant:
    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.p_age} days old")

    def age(self, days: int):
        self.p_age += 1

    def grow(self, days: int):
        self.height += self.growth_factor * days


if __name__ == "__main__":
    plant = Plant()
    plant.name = "Monsera"
    plant.height = 70
    plant.p_age = 120
    plant.growth_factor = 1.5

    start_height = plant.height

    for day in range(1, 7 + 1):
        print(f"== Day {day} ==")
        plant.age(1)
        plant.grow(1)
        plant.get_info()

    end_height = plant.height

    print(f"Growth this week: +{end_height - start_height}cm")
