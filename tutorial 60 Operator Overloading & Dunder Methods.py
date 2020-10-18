class Employee:
    no_of_leaves = 8

    # these __init__ methods are called a dunder method
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod

    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other): #this is a dunder method that overwrites operators
        # and is used for adding operations of a class variables
        return self.salary+other.salary

    def __truediv__(self, other):
        # return 756
        # here we have given retuen of 756 in truediv function that is why if we divide any two
        # variables of class Employee then it will give 756 no matter what number it is
        return self.salary/other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

emp1=Employee('Harry',50000,'programmer')
emp2=Employee('Garry',5000,'Cleaner')
print(emp1+emp2)
print(emp1/emp2)
print(emp1)#here in it it will give <__main__.Employee object at 0x01DEF658> but suppose we don't
# want it to prnt it's printdetails functions then we will use repr function which we have used
# in class Employee you can see it above. for same such things we use str functions but python
# takes str first in preferance over repr
'''but we can call repr like this'''
print(repr(emp1))
'''and if there is not a str function then it will print
Employee('Harry', 50000, 'programmer')
'''
# we can get more overloading methods by searcing
# Mapping Operators to Functions


# QUIZ-- Create a class with any three methods

class tec():
    def __init__(self, aname,asalary):
        self.salary = asalary
        self.name = aname

    def __mod__(self,other):
        return self.salary%other.salary
    def __mul__(self, other):
        return self.salary*other.salary
    def __sub__(self, other):
        return self.salary-other.salary

