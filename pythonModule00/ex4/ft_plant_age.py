def ft_plnat_age() -> None:
    agePlant: int = int(input("Enter plant age in days: "))
    if (agePlant > 60):
        print("Plant is ready to havest")
    else:
        print("Plant need more time to grow")
