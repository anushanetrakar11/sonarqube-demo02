def calculate_division(number1, number2):
    if number2 == 0:
        raise ValueError("Cannot divide by zero")

    return number1 / number2


def main():
    try:
        result = calculate_division(10, 2)
        print(f"Result: {result}")

    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
