#!/usr/bin/env python3


def get_info(name: str, height: int, age: int) -> None:
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")


if __name__ == "__main__":
    name = "Rose"
    height = 25
    age = 30
    print("== Welcome to my garden ==")
    get_info(name, height, age)
    print("\n== End of program ==")
