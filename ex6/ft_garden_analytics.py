#! /usr/bin/env python3


class Plant:
    __name: str
    __height: int
    growth: int = 0

    def __init__(self, name: str, height: int) -> None:
        self.__name = name
        self.__height = height if Plant.is_valid(height) else 0

    def get_name(self) -> int:
        return self.__name

    def get_height(self) -> int:
        return self.__height

    def get_info(self) -> None:
        print(f"- {self.__name}: {self.__height}cm")

    def grow(self) -> None:
        self.__height += 1
        self.growth += 1
        print(f"{self.__name} grew 1cm")

    @staticmethod
    def is_valid(val: int) -> bool:
        return val < 0


class FloweringPlant(Plant):
    color: str
    is_blooming: bool = False

    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color

    def get_info(self):
        print(
            f"- {self.get_name()}: {self.get_height()}cm, {self.color}"
            + f" flowers{' (blooming)' if self.is_blooming else ''}"
        )

    def grow(self) -> None:
        super().grow()
        self.is_blooming = True

    @classmethod
    def bloom(plant: object):
        plant.set_bloom()


class PrizeFlower(FloweringPlant):
    prize_points: int

    def __init__(self, name: str, height: int, color: str, prize_points: int)\
            -> None:
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_info(self) -> None:
        print(
            f"- {self.get_name()}: {self.get_height()}cm, {self.color} flowers{
                ' (blooming)' if self.is_blooming else ''
            }, Prize points: {self.prize_points}"
        )


class Garden:
    owner: str
    plants: list

    def __init__(self, owner: str) -> str:
        self.owner = owner
        self.plants = []

    def add_plant(self, plant: Plant) -> None:
        self.plants += [plant]
        print(f"Added {plant.get_name()} to {self.owner}'s garden'")

    def grow_plants(self) -> None:
        print(f"{self.owner} is helping all plants grow")
        for plant in self.plants:
            plant.grow()

    def report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        for plant in self.plants:
            plant.get_info()


class GardenManager:
    gardens: list

    def __init__(self) -> None:
        self.gardens = []

    @classmethod
    def create_garden_network(cls, garden: Garden) -> object:
        gm = GardenManager()
        gm.add_garden(garden)
        return gm

    def add_garden(self, garden: Garden) -> None:
        if garden not in self.gardens:
            self.gardens += [garden]

    def get_garden_by_owner(self, name: str) -> Garden:
        for garden in self.gardens:
            if garden.owner == name:
                return garden

    class GardenStats:
        is_height_valid: bool = True
        garden_count: int
        points: dict
        total_growth: int
        regular_plant_count: int
        flower_plant_count: int
        prize_plant_count: int

        def __init__(self, manager: "GardenManager") -> None:
            self.manager = manager

        def compute_stats(self) -> None:
            self.garden_count: int = 0
            self.points: dict = {}
            self.is_height_valid: bool = True
            self.total_growth = 0
            self.regular_plant_count: int = 0
            self.flower_plant_count: int = 0
            self.prize_plant_count: int = 0
            for garden in self.manager.gardens:
                self.garden_count += 1
                self.points[garden.owner] = 0
                for plant in garden.plants:
                    self.total_growth += plant.growth
                    if plant.get_height() < 0:
                        self.is_height_valid = False
                    if plant.__class__ == PrizeFlower:
                        self.points[garden.owner] += plant.prize_points
                        self.prize_plant_count += 1
                    elif plant.__class__ == FloweringPlant:
                        self.flower_plant_count += 1
                    else:
                        self.regular_plant_count += 1

        def print_plant_stats(self) -> None:
            self.compute_stats()
            print(
                f"Plants added: {
                    self.regular_plant_count
                    + self.flower_plant_count
                    + self.prize_plant_count
                }, "
                + f"Total growth: {self.total_growth}cm"
            )
            print(
                f"Plant types: {self.regular_plant_count}"
                + f" regular, {self.flower_plant_count}"
                f" flowering, {self.prize_plant_count} prize flowers"
            )

        def print_height_validation(self) -> None:
            self.compute_stats()
            print(f"Height validation test: {self.is_height_valid}")

        def print_score(self) -> None:
            self.compute_stats()
            print(f"Garden scores - {self.points}")

        def print_garden_count(self) -> None:
            self.compute_stats()
            print(f"Total gardens managed: {self.garden_count}")


def stats_demo() -> None:
    print(" === Garden Management System Demo ===")

    gm = GardenManager.create_garden_network(Garden("Alice"))
    gm.add_garden(Garden("Bob"))

    garden_alice = gm.get_garden_by_owner("Alice")

    print()
    garden_alice.add_plant(Plant("Oak Tree", 100))
    garden_alice.add_plant(FloweringPlant("Rose", 25, "red"))
    garden_alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    print()
    garden_alice.grow_plants()

    print()
    garden_alice.report()

    print()
    gm.GardenStats(gm).print_plant_stats()
    gm.GardenStats(gm).print_plant_stats()

    print()
    gm.GardenStats(gm).print_height_validation()
    gm.GardenStats(gm).print_score()
    gm.GardenStats(gm).print_garden_count()


if __name__ == "__main__":
    stats_demo()
