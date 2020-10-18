class employee2():
    no__of__leaves=10

    def __init__(self,aname,arole,asalary):
        self.name=aname
        self.role=arole
        self.salary=asalary

    def info(self):
        return f'the name is {self.name}. salary is {self.salary} and role is {self.role}'

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
 HER WE WILL ONLY LEARN ABOUT MULTIPLLE INHERITENCE"""
class player():
    no_of_games=4
    def __init__(self,aname,agame):
        name=aname
        game=agame

    def details(self):
        return f'the name is {self.name}. the game is {self.game}'

subham=player('subham','cricket')
#so we created a class player and a class employee2
#now suppose we want a class having features pof both player and employee2 then we will use mutiple
# inheritence like this
class coolprogrs(employee2,player):
    language='c++'
    def lang1(self):
        print(self.language)
#so  you must be having doubt that both employee2 and  player have name so whose name would it take
#then your answer is that IT WILL TAKE NAME FROM THE FIRST CLASS GIVEN LIKE THIS
# class coolprogrs(employee2,player)  HERE EMPLOYEE2 WAS GIVEN FIRST SO IT TOOK NAME FROM EMPLOYEE2
# and to summerise it
# ANY TWO SAME VARIABLE IN TWO CLASSES INHERITED IN A SINGLE CLASS WILL TAKE VALUE FROM CLASS
# FIRST CALLED OR  INHERITED
raj=coolprogrs('Raj','coolprogrammer','80000')
det=raj.info()
print(det)

harry1=employee2('harry','instructer','45000')
rohan1=employee2('rohan','worker','30000')