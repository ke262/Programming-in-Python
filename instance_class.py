class Employee:
    company = "Asus"
    
    def __init__(self,salary,name,bond, company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company
    
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond}.")
    
e1 =  Employee(3400, "John", 3, "Tesla")
print(e1.company)
print(Employee.company) # This will always print the class attribute

# Object introspection
print(dir(e1))