def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    if (unit == "packets"):
        unit = "available"
        print(f"{seed_type} seeds: {quantity} packets {unit}\n")
    elif (unit == "grams"):
        unit = "grams total"
        print(f"{seed_type} seeds: {quantity} {unit}\n")
    elif (unit == "area"):
        unit = "square meters"
        print(f"{seed_type} seeds: covers {quantity} {unit}\n")
    else:
        print("Unit undifined")
