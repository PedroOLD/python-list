class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def show(self) -> None:
        print(f"""=== Garden Plant Registry ===
{self.name}: {self.height}cm, {self.age} days old
""")


if __name__ == "__main__":
    p = Plant("Rose", 20, 20)
    p.show()
