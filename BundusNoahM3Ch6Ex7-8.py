import random

MIN_NUMBER = 1
MAX_NUMBER = 500

def get_input() -> int:
    """Get a valid integer input from the user."""
    while True:
        try:
            count: int = int(input("Enter the number of random numbers to generate: "))
            if count <= 0:
                print("Please enter a positive integer.")
                continue
            return count
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def write_random_numbers_to_file(filename: str, count: int) -> None:
    """Generate random numbers and write them to a file."""
    with open(filename, 'w') as file:
        for _ in range(count):
            random_number: int = random.randint(MIN_NUMBER, MAX_NUMBER)
            file.write(f"{random_number}\n")

def read_numbers_from_file(filename: str) -> list:
    """Read numbers from a file and return them as a list of integers."""
    numbers: list = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                number: int = int(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Invalid number found in file: {line.strip()}")
    return numbers

def display_numbers_and_stats(numbers: list) -> None:
    """Display the numbers and their statistics."""
    total: int = sum(numbers)
    count: int = len(numbers)

    print("Random Numbers:")
    for number in numbers:
        print(number)

    print(f"Total of numbers in file: {total}")
    print(f"Number of numbers in file: {count}")

def main() -> None:
    """Main function to execute the program."""
    filename: str = "random_numbers.txt"
    count: int = get_input()
    write_random_numbers_to_file(filename, count)
    numbers: list = read_numbers_from_file(filename)
    display_numbers_and_stats(numbers)

if __name__ == "__main__":
    main()