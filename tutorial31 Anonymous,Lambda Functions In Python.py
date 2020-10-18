# In Python programming, an anonymous function or lambda expression
# is a function definition that is not bound to an identifier (def).
#
# The anonymous function is an inline function.
# The anonymous functions are created using a lambda operator and cannot
# contain multiple expressions.

#suppose we want to write a function to print differance of two number then it can be written by two
# ways

#first way
def minus(x,y):
    return x-y
print(minus(9,5))#this will print 4

#second way
minus2= lambda x,y:x-y#this will work same as previous function
print(minus2(7,5))