class Employee:
    def __init__(self, employee_name: str, employee_number: int):
        self.employee_name: str = employee_name
        self.employee_number: int = employee_number

class ProductionWorker(Employee):
    def __init__(self, employee_name: str, employee_number: int, shift: int, hourly_pay_rate: float):
        super().__init__(employee_name, employee_number)
        self.shift: int = shift
        self.hourly_pay_rate: float = hourly_pay_rate

    def get_production_worker_info(self):
            return self.employee_name, self.employee_number, self.shift, self.hourly_pay_rate

