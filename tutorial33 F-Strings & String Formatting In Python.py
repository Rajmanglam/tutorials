# String formatting is used to design the string using formatting techniques provided
# by the particular programming language. From the % formatting to the format()
# method, to format string literals, there is no limit as to the potential of string crafting.
# There are four significant ways to do string formatting in Python.

# method 1- using'%'operator
v='raj'
k='my name is %s'%v#this way we can add value of variable  v in k but if we will have to add
# a lot of variables then it would be very tuff to debug it
print(k)

# method 2- using .format
l='my name is {} {}'
m=l.format('raj','manglam')
# this is another method of formatting but it is also very clumpsy
print(m)

# method 3- using f string
o='raj'
w='manglam'
l1=f"this is {o}{w}"
#this is f string
# in f strings are indicated by an "f" before the first quotation mark of a string.
# Put the expression inside { } to evaluate the result. Here is a simple example
#
# declaring variables
#
#  str1="Python”
#
#  str2="Programming”
#
# print(f"Welcome to our {str1}{str2} tutorial
import math #here we have imported a module named math
m=int(input('enter the angle'))
k2=math.cos(m)
p=(f'cos of {m} is {k2}')
print(p)