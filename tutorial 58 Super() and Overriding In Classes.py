class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1="I an inside instance variable of class A"
        self.special='I am inn special'


class B(A):

    classvar1 = "I am in class B"

    # here we have overridden classvar1
    #now let us override the whole constructer
    def __init__(self):

        # here we have overridden the constructer of class A
        # but suposse there is a variable special in class A constructer which we want to run
        # keeping constructer of class B in action then we will do like this using super
        super().__init__()
        # here we have kept super(B, self).__init__()above the variable of class B constructer
        # so if we do like this
        # print(b.classvar1)
        # it will print "I an inside instance variable of class B"
        # but if we put it below the variables then it will print
        # I am inside instance variable of class A

        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "I an inside instance variable of class B"

# suppose we do something like this
# print(b.classvar1)
# here the compiler will first check
#1> an instance variable in class B
#2> an instance variable in class A
#3> an normal variable in class B
#4> an normal variable in class A
a=A()
b=B()
print(a.classvar1)
print(b.special+'  '+ b.classvar1)