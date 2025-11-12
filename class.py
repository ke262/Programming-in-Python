class Employee:
    company = "HP"

    def get_salary(self): # self is important here because self is a way to refrence the object of the class which is being created
        print(self)
        return 34000
    
e1 = Employee() # Am object of class Employee is created here
print(e1.get_salary()) #Employee e's get salary method is called

e2 = Employee()
print(e2.get_salary())
print(e2.company)