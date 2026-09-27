from person import Customer

name = input("Enter your name: ")
address = input("Enter your address: ")
telephone_number = int(input("Enter your telephone number: "))
mailing_list: bool = input("Do you want to be on the mailing list? (Yes/No): ").lower() == "yes"

customer = Customer(name, address, telephone_number, mailing_list)

print(f"{customer.get_customer_info()[0]} lives at {customer.get_customer_info()[1]} and can be reached at {customer.get_customer_info()[2]}. They have {'opted in to' if customer.get_customer_info()[3] else 'opted out of'} the mailing list.")

