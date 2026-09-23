Sales: float = 0.00
Day: int = 0
filename: str = "sales.txt"
TotalSales: float = 0.00

with open(filename, 'w') as file:
    for Day in range(7):
        Sales = float(input(f"Enter the total sales for Day {Day + 1}: $"))
        file.write(f"{Sales}\n")

numbers: list = []
with open(filename, 'r') as file:
    for line in file:
        try:
            number: float = float(line.strip())
            numbers.append(number)
        except ValueError:
            print(f"Invalid number found in file: {line.strip()}")

for number in numbers:
    TotalSales += number

print(f"Total sales for the week: ${TotalSales:.2f}")