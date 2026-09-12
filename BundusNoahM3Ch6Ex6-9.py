filename: str = "numbers.txt"

def data_validator(filename: str) -> None:
    """Validate the data in the file and remove invalid entries."""
    with open(filename, "r") as file:
        lines = file.readlines()

    valid_lines = []
    for line in lines:
        try:
            int(line.strip())
            valid_lines.append(line)
        except ValueError:
            pass

    with open(filename, "w") as file:
        file.writelines(valid_lines)

def calculate_average(filename: str) -> None:
    """Calculate the average of a list of numbers."""
    total: int = 0
    count: int = 0

    with open(filename, "r") as file:
        for line in file:
            number: int = int(line.strip())
            total += number
            count += 1
            
    if count > 0:
        average: float = total / count
        print(f"Average of numbers in file: {average}")
    else:
        print("No valid numbers to calculate average.")

def main() -> None:
    """Main function to execute the program."""
    data_validator(filename)
    calculate_average(filename)

if __name__ == "__main__":
    main()