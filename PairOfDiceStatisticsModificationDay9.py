import random


def get_input() -> int:
    """Get a valid integer input from the user."""
    while True:
        try:
            rolls: int = int(input("Input the number of times you'd like to simulate rolling a pair of dice: "))
            if rolls <= 0:
                print("Please enter a positive integer.")
                continue
            return rolls
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def write_random_numbers_to_file(filename: str, rolls: int) -> None:
    """Generate random numbers and write them to a file."""
    with open(filename, 'w') as file:
        for _ in range(rolls):
            die1 = Die()
            die2 = Die()
            die1.roll()
            die2.roll()
            total = die1.get_roll() + die2.get_roll()
            file.write(f"{total}\n")

class Die: # Return uniform distribution of integers 1 through 6
    def __init__(self):
        self.value = 0 # initialize roll integer type
    def roll(self):
        self.value= random.randint(1,6)
    def get_roll(self):
        return self.value

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

def calculate_totals(numbers: list) -> None:
    """Calculate the number of times each number in the file was rolled."""
    frequency: dict = calculate_frequency(numbers)
    percentage: dict = calculate_percentage(numbers, len(numbers))
    print("\nNumber of times each number was rolled:")
    for number, count in frequency.items():
        print(f"{number}: {count}")
    print("\nPercentage of times each number was rolled:")
    for number, percent in percentage.items():
        print(f"{number}: {percent:.2f}%")

def calculate_frequency(numbers: list) -> dict:
    """Calculate the frequency of each number in the list."""
    frequency: dict = {}
    for number in range(2, 13):
        frequency[number] = 0
    for number in numbers:
        frequency[number] += 1
    return frequency

def calculate_percentage(numbers: list, rolls: int) -> dict:
    """Calculate the percentage of each number in the list."""
    percentage: dict = {number: (count / rolls) * 100 for number, count in calculate_frequency(numbers).items()}
    return percentage

def main() -> None:
    """Main function to execute the program."""
    filename: str = "random_numbers.txt"
    rolls: int = get_input()
    write_random_numbers_to_file(filename, rolls)
    numbers: list = read_numbers_from_file(filename)
    calculate_totals(numbers)

main()