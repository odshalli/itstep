class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Ім'я: {self.name}, Посада: {self.position}, Зарплата: {self.salary}"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Співробітника {employee.name} додано до відділу {self.name}.")

    def remove_employee(self, name):
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                print(f"Співробітника {name} видалено з відділу {self.name}.")
                return
        print(f"Співробітника з ім'ям {name} не знайдено у відділі {self.name}.")

    def calculate_total_salary(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Загальна зарплата у відділі {self.name}: {total_salary}")
        return total_salary

    def list_employees(self):
        print(f"Список співробітників відділу {self.name}:")
        for employee in self.employees:
            print(employee)

if __name__ == "__main__":
    # Створення відділу
    it_department = Department("IT Відділ")

    emp1 = Employee("Олександр", "Програміст", 50000)
    emp2 = Employee("Марія", "Аналітик", 45000)

    it_department.add_employee(emp1)
    it_department.add_employee(emp2)

    it_department.list_employees()

    it_department.calculate_total_salary()

    it_department.remove_employee("Марія")

    it_department.list_employees()
