class employee2():
    no__of__leaves=10
    def __init__(self,aname,arole,asalary):
        self.name=aname
        self.role=arole
        self.salary=asalary
    def info(self):
        return f'the name is {self.name}. salary is {self.salary}'
    @classmethod#these types of functions are used for instance variables
    def changeleaves(cls,no):
        cls.no__of__leaves=no
# we know that all functions in a class takes self as default but
# if we want it to be something different then we use class methods
harry1=employee2('harry','instructer','45000')
rohan1=employee2('rohan','worker','30000')
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"
print(f'The name is {rohan1.name}.He  is a {rohan1.role} and his '
      f'salary is {rohan1.salary}')
harry1.changeleaves(49)
print(harry1.no__of__leaves)
