STATE_TAX_RATE: float = .05
COUNTY_TAX_RATE: float = .025
purchase_amount: float = .00

def get_input() -> float:
    purchase_amount = float(input("Enter the purchase amount: "))
    return float(purchase_amount)

def calculate_taxes(purchase_amount: float) -> tuple:
    state_sales_tax = purchase_amount * STATE_TAX_RATE
    county_sales_tax = purchase_amount * COUNTY_TAX_RATE
    total_sales_tax = state_sales_tax + county_sales_tax
    total_sale = purchase_amount + total_sales_tax
    return state_sales_tax, county_sales_tax, total_sales_tax, total_sale

def print_receipt(purchase_amount: float, state_sales_tax: float, county_sales_tax: float, total_sales_tax: float, total_sale: float) -> None:
    print(f"Purchase Amount: ${purchase_amount:.2f}")
    print(f"State Sales Tax: ${state_sales_tax:.2f}")
    print(f"County Sales Tax: ${county_sales_tax:.2f}")
    print(f"Total Sales Tax: ${total_sales_tax:.2f}")
    print(f"Total Sale: ${total_sale:.2f}")

def main() -> None:
    purchase_amount = get_input()
    state_sales_tax, county_sales_tax, total_sales_tax, total_sale = calculate_taxes(purchase_amount)
    print_receipt(purchase_amount, state_sales_tax, county_sales_tax, total_sales_tax, total_sale)

main()