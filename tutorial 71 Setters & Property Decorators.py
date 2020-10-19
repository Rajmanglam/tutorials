class employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
#suppose we want to add email also then
        # self.email=f'{fname}.{lname}@gmail.com'
    def explain(self):
        return f"This employee's name is {self.fname} and his last name is {self.lname}"

    @property#by using this we will not have to call printemail as a function we can only call
    # it as .printemail
    def email(self):
        if self.fname==None or self.lname==None:
            return ('email is not set')
        return f"The employee's email is {self.fname}.{self.lname}@gmail.com"


    # now suppose we want that our program takes email as input and changes the fname and lname
    # then we will do something like this
    @email.setter#this can be used as decorator for any attribute of class after using this
    # setter we can set our attributes outside the class
    def email(self,string):
        names=string.split('@')[0]
        self.fname=names.split('.')[0]
        self.lname=names.split('.')[1]

    # we will have to create a deleter to delete the email entered by us in case required
    # like this using decorator deleter
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
        # this will give us None.None@gmail.com to avoid this we will do changes in email constructer
        # you can see that above
a=employee('rohan','raj')
b=employee('shivam','raj')
print(a.explain())
a.lname='hater'
print(a.email)
a.email='raj.manglam@gmail.com'
print(a.fname)
print(a.email)
del a.email
print(a.email)
