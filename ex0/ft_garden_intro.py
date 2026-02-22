#!/usr/bin/env python3


def get_info(name: str, height: int, age: int):
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")


if __name__ == "__main__":
    name = "Monstera"
    height = 67
    age = 120
    print("== Welcome to my garden ==")
    get_info(name, height, age)
    print("== End of program ==")
