#! /usr/bin/env python3


class Plant:
    __name: str
    __height: int
    growth: int

    def __init__(self, name: str, height: int) -> None:
        self.__name = name
        self.growth = 0
        self.__height = height if Plant.is_valid(height) else 0

    def get_name(self) -> int:
        return self.__name

    def get_height(self) -> int:
        return self.__height

    def get_info(self) -> None:
        print(f"- {self.__name}: {self.__height}cm")

    def grow(self) -> None:
        self.__height += 1
        print(f"{self.__name} grew 1cm")

    @staticmethod
    def is_valid(val: int) -> bool:
        return val >= 0


class FloweringPlant(Plant):
    color: str
    is_blooming: bool

    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color
        self.is_blooming = False

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
    plant_count: int
    score: int
    total_growth: int
    is_height_valid: bool
    types_dict: dict

    def __init__(self, owner: str) -> str:
        self.owner = owner
        self.plants = []
        self.plant_count = 0
        self.score = 0
        self.total_growth = 0
        self.is_height_valid = True
        self.types_dict = {'regular': 0, 'flowering': 0, 'prize flowers': 0}

    def add_plant(self, plant: Plant) -> None:
        self.plants += [plant]
        self.total_growth += plant.growth
        if plant.get_height() < 0:
            self.is_height_valid = False
        if plant.__class__ == PrizeFlower:
            self.score += plant.prize_points
            self.types_dict['prize flowers'] += 1
        elif plant.__class__ == FloweringPlant:
            self.types_dict['flowering'] += 1
        else:
            self.types_dict['regular'] += 1
        print(f"Added {plant.get_name()} to {self.owner}'s garden'")

    def grow_plants(self) -> None:
        print(f"{self.owner} is helping all plants grow")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        for plant in self.plants:
            plant.get_info()


class GardenManager:
    gardens: list = []

    @classmethod
    def create_garden_network(cls, owner: str) -> None:
        cls.gardens += [Garden(owner)]

    @classmethod
    def garden(cls, name: str) -> Garden:
        for garden in cls.gardens:
            if garden.owner == name:
                return garden

    class GardenStats:
        def print_plant_stats() -> None:
            types_dict = {'regular': 0, 'flowering': 0, 'prize flowers': 0}
            total_growth = 0
            plant_count = 0
            for garden in GardenManager.gardens:
                total_growth += garden.total_growth
                for type in garden.types_dict:
                    types_dict[type] += garden.types_dict[type]
                    plant_count += garden.types_dict[type]
            print(f"Plants added: {plant_count}, "
                  + f"Total growth: {total_growth}cm")
            print(f"Plant types: {types_dict}")

        def print_height_validation() -> None:
            validation = [g.is_height_valid for g in GardenManager.gardens]
            print(f"Height validation test: {False not in validation}")

        def print_score() -> None:
            score = {}
            for garden in GardenManager.gardens:
                score[garden.owner] = garden.score
            print(f"Garden scores - {score}")

        def print_garden_count() -> None:
            garden_count = 0
            for garden in GardenManager.gardens:
                garden_count += 1
            print(f"Total gardens managed: {garden_count}")


def stats_demo() -> None:
    print(" === Garden Management System Demo ===")

    GardenManager.create_garden_network("Alice")
    GardenManager.create_garden_network("Bob")

    print()
    GardenManager.garden("Alice").add_plant(Plant("Oak Tree", 100))
    GardenManager.garden("Alice").add_plant(FloweringPlant("Rose", 25, "red"))
    GardenManager.garden("Alice").\
        add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    print()
    GardenManager.garden("Alice").grow_plants()

    print()
    GardenManager.garden("Alice").report()

    print()
    GardenManager.GardenStats.print_plant_stats()

    print()
    GardenManager.GardenStats.print_height_validation()
    GardenManager.GardenStats.print_score()
    GardenManager.GardenStats.print_garden_count()


if __name__ == "__main__":
    stats_demo()
