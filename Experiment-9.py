'''class Employee:
    def __init__(self, emp_id, emp_name, basic_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.basic_salary = basic_salary

    def calculate_gross_salary(self):
        return self.basic_salary + self.basic_salary * (self.da / 100) + self.basic_salary * (self.hra / 100)

    def calculate_net_salary(self):
        return self.calculate_gross_salary() - self.calculate_tax() - self.epf

    def calculate_tax(self):
        return self.basic_salary * (self.tax / 100)

    def print_pay_details(self):
        print(f'Employee ID: {self.emp_id}\nEmployee Name: {self.emp_name}\nBasic Salary: {self.basic_salary}\nGross Salary: {self.calculate_gross_salary()}\nNet Salary: {self.calculate_net_salary()}')

class Manager(Employee):
    def __init__(self, emp_id, emp_name, basic_salary):
        super().__init__(emp_id, emp_name, basic_salary)
        self.da, self.hra, self.tax, self.epf = 95, 20, 25, 3000

class Engineer(Employee):
    def __init__(self, emp_id, emp_name, basic_salary):
        super().__init__(emp_id, emp_name, basic_salary)
        self.da, self.hra, self.tax, self.epf = 80, 15, 15, 2000

def main():
    print("1. Manager\n2. Engineer")
    choice = int(input("Enter the type of employee: "))
    emp_id, emp_name, basic_salary = input("Enter Employee ID, Name, Basic Salary: ").split()
    basic_salary = float(basic_salary)

    if choice == 1:
        employee = Manager(emp_id, emp_name, basic_salary)
    elif choice == 2:
        employee = Engineer(emp_id, emp_name, basic_salary)
    else:
        print("Invalid choice. Exiting...")
        return

    employee.print_pay_details()

if __name__ == "__main__":
    main()
'''

class Worker:
    def __init__(self, name, salary_rate):
        self.name = name
        self.salary_rate = salary_rate

    def compute_pay(self, hours):
        return self.salary_rate * hours

class DailyWorker(Worker):
    def compute_pay(self, days_worked):
        return self.salary_rate * days_worked

class SalariedWorker(Worker):
    def compute_pay(self, hours_worked):
        return self.salary_rate * 40

# Main program
def main():
    name = input("Enter worker's name: ")
    salary_rate = float(input("Enter worker's hourly wage or weekly salary: "))
    worker_type = input("Enter worker type (daily/salaried): ")

    if worker_type.lower() == 'daily':
        days_worked = int(input("Enter number of days worked: "))
        worker = DailyWorker(name, salary_rate)
        pay = worker.compute_pay(days_worked)
    elif worker_type.lower() == 'salaried':
        hours_worked = int(input("Enter number of hours worked: "))
        worker = SalariedWorker(name, salary_rate)
        pay = worker.compute_pay(hours_worked)
    else:
        print("Invalid worker type. Please enter 'daily' or 'salaried'.")

    print(f"{worker.name} earned Rs.{pay} this week.")

if __name__ == "__main__":
    main()

