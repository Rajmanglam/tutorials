# Today we are going to discuss a problem or more like a confusion associated with
# multiple inheritance. The problem is commonly known as the “Diamond Shape Problem.”.
# It is about a priority related confusion, which arises when four classes are related
# to each other by an inheritance relationship

class A:
    def met(self):
        print('this is a method from class A')

    pass
class B(A):
    def met(self):
        print('this is a method from class B')
    pass
class C(A):
    def met(self):
        print('this is a method from class C')
    pass
class D(B,C):
    def met(self):
        print('this is a method from class D')
    pass

a=A()
b=B()
c=C()
d=D()
d.met()