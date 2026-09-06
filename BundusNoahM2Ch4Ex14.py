space_count: int = 0

for space_count in range(6):
    print("#", end="")
    for spaces in range(space_count):
        print(end=" ")
    space_count += space_count
    print("#")