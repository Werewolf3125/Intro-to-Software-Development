Joes_Gourmet_Burgers = 1
Main_Street_Pizza_Company = 1
Corner_Cafe = 1
Mamas_Fine_Italian = 1
The_Chefs_Kitchen = 1

vegetarian: str = str.lower(input("Is anyone in your party a vegetarian? (y/n): "))
vegan: str = str.lower(input("Is anyone in your party a vegan? (y/n): "))
gluten_free: str = str.lower(input("Is anyone in your party gluten-free? (y/n): "))

if vegetarian == "y":
    Joes_Gourmet_Burgers = 0
if vegan == "y":
    Joes_Gourmet_Burgers = 0
    Mamas_Fine_Italian = 0
    Main_Street_Pizza_Company = 0
if gluten_free == "y":
    Joes_Gourmet_Burgers = 0
    Mamas_Fine_Italian = 0

print("Here are your restaurant choices:")
if Joes_Gourmet_Burgers == 1:
    print("Joe's Gourmet Burgers")
if Main_Street_Pizza_Company == 1:
    print("Main Street Pizza Company")
if Corner_Cafe == 1:
    print("Corner Cafe")
if Mamas_Fine_Italian == 1:
    print("Mama's Fine Italian")
if The_Chefs_Kitchen == 1:
    print("The Chef's Kitchen")
