from car import Car

#I couldn't get the import to work with the long file name. It kept saying that the name was "Bundus" instead of "BundusNoahM5Ch10Ex2_car", so I changed the name of the file to "car" and it works now. Maybe you can explain what I was doing wrong?

year_model = input("Enter the year model of your car: ")
make = input("Enter the make of your car: ")

car = Car(year_model, make, 0)

for _ in range(5):
    car.accelerate()
    print(f"Your {car.get_speed()[0]} {car.get_speed()[1]} is now traveling at {car.get_speed()[2]} mph")

for _ in range(5):
    car.brake()
    print(f"Your {car.get_speed()[0]} {car.get_speed()[1]} is now traveling at {car.get_speed()[2]} mph")