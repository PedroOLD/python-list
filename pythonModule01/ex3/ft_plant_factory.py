class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.agedays: int = age
        self.taxGrow: float = 0.8

    def show(self) -> None:
        print(f"""=== Plant Factory Output ===
{self.name}: {self.height:.1f}cm, {self.agedays} days old
""")

    def grow(self) -> None:
        self.height += self.taxGrow

    def age(self) -> None:
        self.agedays += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oka", 200, 365)
    cactus = Plant("Cactus", 5, 45)
    rose.show()
    oak.show()
    cactus.show()
