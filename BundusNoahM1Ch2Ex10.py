COOKIES_PER_NORMAL_BATCH = 48
SUGAR = 1.50
BUTTER = 1.00
FLOUR = 2.75

desired_cookies = int(input("Enter the number of cookies you want to bake: "))
sugar_needed = SUGAR * desired_cookies / COOKIES_PER_NORMAL_BATCH
butter_needed = BUTTER * desired_cookies / COOKIES_PER_NORMAL_BATCH
flour_needed = FLOUR * desired_cookies / COOKIES_PER_NORMAL_BATCH

print(f"To make {desired_cookies} cookies, you will need:")
print(f"Sugar: {sugar_needed:.2f} cups")
print(f"Butter: {butter_needed:.2f} cups")
print(f"Flour: {flour_needed:.2f} cups")