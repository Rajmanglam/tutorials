class employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def explain(self):
        return f"This employee's name is {self.fname} and his last name is {self.lname}"
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return ('email is not set')
        return f"The employee's email is {self.fname}.{self.lname}@gmail.com"
    @email.setter
    def email(self,string):
        names=string.split('@')[0]
        self.fname=names.split('.')[0]
        self.lname=names.split('.')[1]
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None

skillf=employee('skill','f')
# object introspection means getting information about a object like this
print(type(skillf))
print(id(skillf))#this will give id of object
o=skillf
print(dir(o))#this will give us a list of all the things we can do with object given

import inspect
print(inspect.getmembers(skillf))# this will give us all members of the object given