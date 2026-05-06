class Plant():
    def __init__(self, name: str, height: int, age: int):
        error: bool = False
        if  (height < 0): 
            raise ValueError("Error, height can't be negative")
        if (age < 0):
            raise ValueError("Error, age cant be negative")
        if not error:
            self.name: str = name
            self._height: int = height
            self._agedays: int = age
            self._taxGrow: float = 0.8

    def show(self) -> None:
        print(f"""=== Garden Security Sestem ===
{self.name}: {self._height:.1f}cm, {self._agedays} days old
""")

    def _grow(self) -> None:
        self._height += self.taxGrow

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
    
    def get_agr(self) -> int:
        return self._agedays
    
if __name__ == "__main__":
    rose = Plant("Rose", 166, 26)
    rose.show()
    rose.set_age(-2)
    rose.show()