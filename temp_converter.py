def to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def main() -> None:
    while True:
        raw_temp = input("Enter temperature (or 'exit' to quit): ").strip()
        if raw_temp.lower() == "exit":
            break

        raw_unit = input("Enter unit (C/F) (or 'exit' to quit): ").strip()
        if raw_unit.lower() == "exit":
            break

        try:
            value = float(raw_temp.replace(",", "."))
        except ValueError:
            print("Error: temperature must be a number.")
            continue

        unit = raw_unit.strip().upper()
        if unit == "C":
            converted = to_fahrenheit(value)
            print(f"{converted:.2f} F")
        elif unit == "F":
            converted = to_celsius(value)
            print(f"{converted:.2f} C")
        else:
            print("Error: unit must be 'C' or 'F'.")


if __name__ == "__main__":
    main()
