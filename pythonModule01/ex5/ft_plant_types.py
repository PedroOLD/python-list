class Plant():
    def __init__(self, name: str, height: int, age: int):
        error: bool = False
        if (height < 0):
            raise ValueError("Error, height can't be negative")
        if (age < 0):
            raise ValueError("Error, age cant be negative")
        if not error:
            self.name: str = name
            self._height: int = height
            self._agedays: int = age
            self._taxGrow: float = 2.1
            self._valueBloom: str = "false"

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._agedays} days old")

    def _grow(self) -> None:
        self._height += self._taxGrow
        self._age()

    def _age(self) -> None:
        self._agedays += 1

    def set_height(self, new_height) -> None:
        if new_height < 0:
            raise ValueError("Error, age cant be negative")
        else:
            self._height = new_height

    def get_height(self) -> int:
        return self._height

    def set_age(self, new_age) -> None:
        if new_age < 0:
            raise ValueError("Error, agr can't be negative")
        else:
            self._agedays = new_age

    def get_age(self) -> int:
        return self._agedays


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self._color: str = color

    def bloom(self, value: str) -> None:
        self._valueBloom = value

    def show(self):
        super().show()
        print(f" Color: {self._color}")
        if self._valueBloom in ("true", "yes", "1"):
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name}  has not bloomed yet")


class Tree(Plant):
    def __init__(self,
                 name: str,
                 height: int,
                 age: int,
                 trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self, activate: str) -> None:
        if activate in ("true", "1", "yes", "y"):
            print(f"Tree {self.name} now produces a shade of"
                  f"{self._height}cm long and {self.trunk_diameter}cm wide")
        elif activate in ("false", "0", "no", "n"):
            print("Without shade")
        else:
            print("response not valid")


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 height: int,
                 age: int,
                 harvest_season: str,
                 nutricional_value: int):
        super().__init__(name, height, age)
        self._harvest_season: str = harvest_season
        self._nutricional_value: int = nutricional_value

    def show(self):
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutricional_value}")

    def grow(self, days: int):
        for day in range(days):
            self._nutricional_value += 1
            super()._grow()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower = Flower("Rose", 15, 10, "red")
    flower.show()
    print("[asking the rose to bloom]")
    flower.bloom("true")
    flower.show()
    print()
    print("=== Tree")
    tree = Tree("Oak", 200, 365, 0.5)
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade("true")
    print()
    print("=== Vegetable")
    tree = Vegetable("Tomate", 5, 10, "april", 0)
    tree.show()
    print("[make tomato grow and age for 20 days]")
    tree.grow(20)
    tree.show()
    print()
