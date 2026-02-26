#! /usr/bin/env python3


class SecurePlant:
    name: str
    height: int
    p_age: int

    def __init__(self, name: str, height: int, age: int) -> None:
        self.__name = name
        self.__height = height
        self.__age = age

    def get_info(self) -> None:
        print(f"{self.__name} ({self.__height}cm, {self.__age} days)")

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

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


if __name__ == "__main__":
    plant: SecurePlant = SecurePlant("Rose", 20, 25)

    print("=== Garden Security System ===")
    print(f"Plant created: {plant.get_name()}")
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)

    print("\nCurrent plant: ", end="")
    plant.get_info()
