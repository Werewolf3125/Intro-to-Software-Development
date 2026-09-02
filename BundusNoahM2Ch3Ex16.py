decider = str.lower(input("Are you having trouble with your wifi connection? y/n "))
if decider == "y":
    print("Reboot the computer and try to connect.")
    decider = str.lower(input("Did that fix the problem? y/n "))
    if decider == "n":
        print("Reboot the router and try to connect.")
        decider = str.lower(input("Did that fix the problem? y/n "))
        if decider == "n":
            print("Make sure the cables between the router and modem are plugged in firmly.")
            decider = str.lower(input("Did that fix the problem? y/n "))
            if decider == "n":
                print("Move the router to a new location and try to connect.")
                decider = str.lower(input("Did that fix the problem? y/n "))
                if decider == "n":
                    print("Get a new router.")