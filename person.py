class Person:
    def __init__(self, name: str, address: str, telephone_number: int):
        self.name: str = name
        self.address: str = address
        self.telephone_number: int = telephone_number

class Customer(Person):
    def __init__(self, name: str, address: str, telephone_number: int, mailing_list: bool):
        super().__init__(name, address, telephone_number)
        self.mailing_list: bool = mailing_list

    def get_customer_info(self):
            return self.name, self.address, self.telephone_number, self.mailing_list

