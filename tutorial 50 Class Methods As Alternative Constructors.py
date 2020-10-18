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

    @classmethod#we had to set 3 parameters for harry1 and rohan1 but we can do it even like this
    def mystr(cls,string):
    #     k=string.split('-')
    #     return cls(k[0],k[1],k[2])
    # you can uncomment the above code and try it also but first let's see a one liner
     return cls(*string.split('-'))

# we know that all functions in a class takes self as default but
# if we want it to be something different then we use class methods
harry1=employee2('harry','instructer','45000')
rohan1=employee2('rohan','worker','30000')
karan=employee2.mystr("karan-instructer-salary=45000")
print(f'The name is {rohan1.name}.He  is a {rohan1.role} and his '
      f'salary is {rohan1.salary}')
harry1.changeleaves(49)
print(harry1.no__of__leaves)
print(karan.name)