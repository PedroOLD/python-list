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

    @staticmethod
    def older_then_year(age: int) -> bool:
        return age > 365
    
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