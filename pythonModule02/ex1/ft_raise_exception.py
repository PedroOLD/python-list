def input_temperature(temp_str) -> int:
    number: int = int(temp_str)
    if (number < 0):
        raise ValueError(f"{number}°C is too cold for plants (min 0°C)")
    print(f"Temperature is now {number}°C")
    return number


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    print("Input is 50")
    try:
        input_temperature('50')
    except ValueError as e:
        print("Caught input_temperature error: ", e)
    print()
    print("Input is abc")
    try:
        input_temperature('abc')
    except ValueError as e:
        print("Caught input_temperature error: ", e)
    print()
    print("Input is -20")
    try:
        input_temperature('-20')
    except ValueError as e:
        print("Caught input_temperature error: ", e)
