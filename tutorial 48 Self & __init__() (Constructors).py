class employee():
    no__of__leaves=10
    def info(self):
        return f'the name is {self.name}. salary is {self.salary}'
# in the above program it has taken self by default which is used as
# a storing variable for variable rohan and harry
harry=employee()
rohan=employee()
harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"
print(rohan.info())

# here we had to give so many of these lines like this
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"
# to get information about our names now  let's look at another easier
# way of doing this

class employee2():
    no__of__leaves=10
    def __init__(self,aname,arole,asalary):
        self.name=aname
        self.role=arole
        self.salary=asalary
    def info(self):
        return f'the name is {self.name}. salary is {self.salary}'

harry1=employee2('harry','instructer','45000')
rohan1=employee2('rohan','worker','30000')
print(f'The name is {rohan1.name}.He  is a {rohan1.role} and his '
      f'salary is {rohan1.salary}')