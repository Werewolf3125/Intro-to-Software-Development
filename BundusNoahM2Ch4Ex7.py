day_count: int = input("Number of days to calculate: ")
while int(day_count) < 1:
    day_count = input("Please enter a positive integer for the number of days: ")

daily_income: float = 0.01
total_income: float = 0.00

num_days = int(day_count)

print("Day Total Income")

for day_num in range(num_days):
    total_income += daily_income
    daily_income = daily_income * 2
    print(f"{day_num + 1} {total_income:.2f}")

