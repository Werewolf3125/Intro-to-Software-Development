from employee import ProductionWorker

employee_name = input("Enter your name: ")
employee_number = int(input("Enter your employee number: "))
shift = int(input("Enter your shift (1 for day, 2 for night): "))
hourly_pay_rate = float(input("Enter your hourly pay rate: "))

production_worker = ProductionWorker(employee_name, employee_number, shift, hourly_pay_rate)

print(f"{production_worker.get_production_worker_info()[0]} has employee number {production_worker.get_production_worker_info()[1]} and works shift {production_worker.get_production_worker_info()[2]}. Their hourly pay rate is ${production_worker.get_production_worker_info()[3]:.2f}.")

