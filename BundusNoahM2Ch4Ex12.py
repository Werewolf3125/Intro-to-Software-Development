organism_input: str = input("Starting number of organisms: ")
while int(organism_input) < 1:
    organism_input = input("Please enter a positive integer for the starting number of organisms: ")

start_num_organism: int = int(organism_input)

daily_increase_input: str = input("Average daily increase (as a decimal representing a percentage): ")
while float(daily_increase_input) <= 0:
    daily_increase_input = input("Please enter a positive number for the average daily increase: ")

avg_daily_increase: float = 1 + float(daily_increase_input) #the average daily increase is added to 1 to represent the total growth factor

num_days_input: str = input("Enter the number of days (less than 1000) to display the population for: ")
while int(num_days_input) < 1 or int(num_days_input) >= 1000:
    num_days_input = input("Please enter a positive integer for the number of days: ")

num_days: int = int(num_days_input)

print("Day Approximate Population")

for day_num in range(num_days):
    print(f"{day_num + 1} {start_num_organism:.2f}")
    start_num_organism = start_num_organism * avg_daily_increase

