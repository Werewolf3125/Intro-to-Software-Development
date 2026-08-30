stockbroker_tax = .03
shares = 2000
purchase_price = 40.00
sell_price = 42.75

purchase_cost = shares * purchase_price
purchase_commission = purchase_cost * stockbroker_tax
sell_cost = shares * sell_price
sell_commission = sell_cost * stockbroker_tax
total_commission = purchase_commission + sell_commission
profit = sell_cost - purchase_cost - total_commission

print(f"Buying price: ${purchase_cost}")
print(f"Buying commission: ${purchase_commission}")
print(f"Selling price: ${sell_cost}")
print(f"Selling commission: ${sell_commission}")
print(f"Total commission: ${total_commission}")
print(f"Profit: ${profit}")