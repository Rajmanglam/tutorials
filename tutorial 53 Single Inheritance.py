class employee2():
    no__of__leaves=10

    def __init__(self,aname,arole,asalary):
        self.name=aname
        self.role=arole
        self.salary=asalary

    def info(self):
        return f'the name is {self.name}. salary is {self.salary}'

    # we know that all functions in a class takes self as default but
    # if we want it to be something different then we use class methods
    @classmethod#these types of functions are used for instance variables
    def changeleaves(cls,no):
        cls.no__of__leaves=no

    @classmethod#we had to set 3 parameters for harry1 and rohan1 but we can do it even like this

    def mystr(cls,string):
    #     k=string.split('-')
    #     return cls(k[0],k[1],k[2])
    # you can uncomment the above code and try it also but first let's see a one liner
     return cls(*string.split('-'))

    @staticmethod
    def printgood(string):
        print('this  is good'+string)

"""Inheritance is the ability to define a new class(child class)
 that is a modified version of an existing class(parent class)
 HER WE WILL ONLY LEARN ABOUT SINGLE INHERITENCE"""

'''let's understand it with a example 
we know that harry and rohan are two people whom we have defined using employee 
 class but we also want to create a class that has all features of employee and also tell which
 programming language does it know then we will use class inheritence like this'''

class programmer(employee2):#with this method it will get all code of employee2
    def __init__(self, aname, arole, asalary, alang):
        self.name = aname
        self.role = arole
        self.salary = asalary
        self.language = alang
        # we do this to add a programmer before the name
        # now we will write to add language of programmer
    def prog(self):
        print(f'the programmer name is {self.name}. salary is {self.salary} and he knows the languages'
              f'{self.language}')




subham=programmer('subham','programmer','55000',['python','java','c++','nodeJS'])
ritesh=programmer('Ritesh','programmer','60000',['python','java','react JS'])
print(subham.prog())


harry1=employee2('harry','instructer','45000')
rohan1=employee2('rohan','worker','30000')