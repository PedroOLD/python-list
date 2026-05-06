def recursive_days(days: int) -> None:
    if (days > 1):
        recursive_days(days - 1)
        print(f"Day {days}")
    else:
        print(f"Day {days}")


def ft_count_harvest_recusive() -> None:
    days: int = int(input("Days until harvest: "))
    recursive_days(days)
