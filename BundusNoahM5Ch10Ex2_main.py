from BundusNoahM5Ch10Ex2_car import Car

year_model = input("Enter the year model of your car: ")
make = input("Enter the make of your car: ")

car = Car(year_model, make, 0)

for _ in range(5):
    car.accelerate()
    print(f"Your {year_model} {make} is now traveling at {car.get_speed()[2]} mph")

for _ in range(5):
    car.brake()
    print(f"Your {year_model} {make} is now traveling at {car.get_speed()[2]} mph")