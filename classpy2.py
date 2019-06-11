class Employee:
    numep = 0
    tot_sal = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

        self.__class__.numep += 1
        self.__class__.tot_sal += self.salary

    def avg_sal(self):
        avg = Employee.tot_sal / Employee.numep
        return avg


class FulltimeEmployee(Employee):

    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)


e1 = Employee('jack', 'A', 1000, 'CSE')
Employee('rose', 'B', 5000, 'ECE')
Employee('john', 'C', 8000, 'EEE')
Employee('mary', 'D', 6000, 'EEE')

print("Total Number of Employees: " + str(Employee.numep))
print("Final Average Salary of Employees: " + str(e1.avg_sal()))
