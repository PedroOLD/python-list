class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.agedays: int = age
        self.taxGrow: float = 0.8

    def show(self) -> None:
        print(f"""=== Garden Plant Registry ===
{self.name}: {self.height:.1f}cm, {self.agedays} days old
""")

    def grow(self) -> None:
        self.height += self.taxGrow

    def age(self) -> None:
        self.agedays += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    i = 0
    while (i < 7):
        rose.age()
        rose.grow()
        rose.show()
        i += 1
