packages_purchased: int = int(input("Enter the number of packages purchased: "))
discount: float = 0.0
price_per_package: float = 99.00

if packages_purchased < 10:
    discount = 0.0
elif packages_purchased < 20:
    discount = 0.1
elif packages_purchased < 50:
    discount = 0.2
elif packages_purchased < 100:
    discount = 0.3
else:
    discount = 0.4

base_cost : float = packages_purchased * price_per_package
print(f"Packages purchased: {packages_purchased}")
print(f"Money saved: ${(money_saved := base_cost * discount):.2f}")
print(f"Total cost: ${base_cost - money_saved:.2f}")