class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showEmployee(self):
        print("Role:", self.role)
        print("Department:", self.dept)
        print("Salary:", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__(role="Engineer", dept="Engineering", salary=60000)

    def showEmployee(self):
        super().showEmployee()
        print("Skill:", self.skill)

eng1 = Engineer("Alice", 30)
eng1.showEmployee()