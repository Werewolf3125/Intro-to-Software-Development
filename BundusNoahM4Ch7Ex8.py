filename: str = "GirlNames.txt"
names: list = []
with open(filename, 'r') as file:
    for line in file:
        name: str = str(line.strip())
        names.append(name)

filename: str = "BoyNames.txt"
with open(filename, 'r') as file:
    for line in file:
        name: str = str(line.strip())
        names.append(name)

get_input: str = input("Which name would you like to check? ").lower()
get_input = get_input.capitalize()
while str(get_input) != "":
    if get_input in names:
        print(f"{get_input} is a popular name.")
    else:
        print(f"{get_input} is not a popular name.")
    get_input = input("Which name would you like to check? Input nothing to end. ").lower()
    get_input = get_input.capitalize()