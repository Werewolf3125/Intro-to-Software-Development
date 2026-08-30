STATE_TAX_RATE = .05
COUNTY_TAX_RATE = .025

purchase_amount = float(input("Enter the purchase amount: "))
state_sales_tax = purchase_amount * STATE_TAX_RATE
county_sales_tax = purchase_amount * COUNTY_TAX_RATE
total_sales_tax = state_sales_tax + county_sales_tax
total_sale = purchase_amount + total_sales_tax

print(f"Purchase Amount: ${purchase_amount:.2f}")
print(f"State Sales Tax: ${state_sales_tax:.2f}")
print(f"County Sales Tax: ${county_sales_tax:.2f}")
print(f"Total Sales Tax: ${total_sales_tax:.2f}")
print(f"Total Sale: ${total_sale:.2f}")
