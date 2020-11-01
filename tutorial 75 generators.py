"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -
"""
# Generators concept is also very similar as it is used to make an iterator.
# The only difference comes in the return statement. The generator does not use a
# return statement. Instead, it uses a yield keyword. Yield functionality is very
# similar to return as it returns a value to the caller, but the difference is that
# it also saves the state of the iterator. Meaning that when we use the function again,
# the yield will resume it is the value from the place it left off.

def gen(n):
    for i in range (n) :
        yield i #here we have yielded so it will act as a return function and this function
        # will no longer execute
        # the difference between yield and print is that it print will print values
        # whereas yield will create on the fly value
# now if we will do something like this
l=gen(9230)
#this will not print 1 to 9230 instead it will print
# <generator object gen at 0x01531990>
# it actually has the capacity to print 1 to 9230
print(l)
print(l.__next__())#this will print 0
print(l.__next__())#this will print 1
print(l.__next__())#this will print 2
print(l.__next__())#this will print 3
print(l.__next__())#this will print 4

#generator to print fibonicci numbers
def fibo(n):
    for i in range (n):
        yield i+(i+1)
l0=fibo(5)
print(l0.__next__())
print(l0.__next__())
print(l0.__next__())
print(l0.__next__())

def factorial(n):
    fac=1
    for i in range(n):
        fac = fac * (i + 1)
        yield fac

n = int(input("Input a number to compute the factiorial : "))
l00=factorial(5)
print(l00.__next__())
print(l00.__next__())
print(l00.__next__())
print(l00.__next__())
print(l00.__next__())
