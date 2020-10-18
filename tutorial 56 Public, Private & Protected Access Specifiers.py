# public --- anyone and everyone can see or get access
# protected --- only specified people can see or get access
# public --- no one except you can see or get access
class employee2():
    no__of__leaves=10
    # if we want to keep name public then we will simply put the variable name like here
    # no__of__leaves
    '''but if we want ot make it protected then we will do like this'''
    _matches=99
    # we will put a _ behind it but it can still be accessed by this program
    '''if we want to create private variable then we will do like this'''
    __heros=90
    # we put __ behind private variable but it can't be directly accesed we have to do like this
    # print(variable._employee__heros)
    def __init__(self,aname,arole,asalary):
        self.name=aname
        self.role=arole
        self.salary=asalary
    def info(self):
        return f'the name is {self.name}. salary is {self.salary} and role is {self.role}'\
    @classmethod
    def changeleaves(cls,no):
        cls.no__of__leaves=no
    @classmethod
    def mystr(cls,string):
     return cls(*string.split('-'))
    @staticmethod
    def printgood(string):
        print('this  is good'+string)
