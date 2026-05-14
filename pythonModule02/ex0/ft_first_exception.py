def input_temperature(temp_str) -> int:
    """
        converte uma string em um number
    """
    number: int = int(temp_str)
    return number


def test_temperature() -> None:
    """
        test as funcoes de input
    """
    print("=== Garden Temperature ===")

    print()
    print('Input data is "25"')
    try:
        current_number = input_temperature("25")
        print(f"Temperature is now {current_number}°C")
    except Exception as e:
        print("Caught input_temperature error", e)

    print()
    print('Input data is "25b"')
    try:
        current_number = input_temperature("25b")
        print(f"Temperature is now {current_number}°C")
    except Exception as e:
        print("Caught input_temperature error", e)

    print()
    print('Input data is "abc"')
    try:
        current_number = input_temperature("abc")
        print(f"Temperature is now {current_number}°C")
    except Exception as e:
        print("Caught input_temperature error", e)


if __name__ == "__main__":
    test_temperature()
