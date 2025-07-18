from converter import km_to_miles, celsius_to_fahrenheit, kg_to_pounds

def main():
    print("Welcome to the Unit Converter!")

    print("""
    Select conversion:
    1. Kilometers to Miles
    2. Celsius to Fahrenheit
    3. Kilograms to Pounds
    """)

    try:
        choice = int(input("Enter your choice (1, 2, or 3): "))
        value = float(input("Enter the value to convert: "))

        if choice == 1:
            result = km_to_miles(value)
        elif choice == 2:
            result = celsius_to_fahrenheit(value)
        elif choice == 3:
            result = kg_to_pounds(value)
        else:
            print("Invalid choice")
            return

        print("Converted value is:", result)

    except ValueError:
        print("Please enter valid numeric input.")

if __name__ == "__main__":
    main()
