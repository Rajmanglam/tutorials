# TYPES OF OPERATORS IN PYTHON
""""
1.Arithmatic operator
2.Assignment operator
3.comparison operator
4.logical operator
5.identity operator
6.membership operator
7.bitwise operator
"""

#1.Arithmatic operator are used to mathmatical operations
print("5+6 is",5+6)
print("5-6 is",5-6)
print("5/6 is",5/6)
print("5**6 is",5**6)
print("5%6 is",5%6)
print("5//6 is",5//6)#this // will give us intiger value
#these types of operators are called arithmatic operator

#2.Assignment operator are used to assign values to a variable
x=8 # here = is a assignment operator which assigned 8 to variable x
print("assignment operator")
print(x)
x+=7# this += will add 7 to previous value of x which is 15
print(x)
x-=4# this -= will remove 4 from previous value of x which was 15 and will give 11
print(x)
x*=88# this will multiply x with 88
print(x)
x/=22# this will give qotient on dividing x by 22
print(x)
x*=22
x%=9#this will give remainder when dividing 968 with 9
print(x)
x**=7# this will raise x to it's 7th power
print(x)

#comparison operator are used to do comparison of values
print("comparison operators")
x=7
print(x==10)# this will cheak if x is equal to 10
print(x>=10)# this will cheak if x is greater than 10
print(x<=10)# this will cheak if x is smaller than 10
print(x!=10)# this will cheak if x is not equal to 10

#logical operators
print("LOGICAL OPERATORS")
a=True
b=False
print(a and a)#here a and a are true which will give true value in return
print(a and b)#here a and b are not true which will not give true value in return

#ientity oprators
print("IDENTITY OPERATOR")
k=99
print(k is 77)# this will cheak if k is equal to 77
print(k is not 8391)# this will cheak if k is not equal to 8391

# membership operator
print('MEMBERSHIP OPERATOR')
list=[99,44,23,31,323,1]
print( 32 in list)# this in function is used to cheak if 32 is in any list topple
# or dictionary as 32 is not in list so it will return FALSE as result
print(99 in list)# this in function is used to cheak if 99 is in any list topple
# or dictionary as 99 is not in list so it will return TRUE as result
print(88 not in list)# this in function is used to cheak if 88 is not in any
# list topple or dictionary as 88 is not in list so it will return TRUE as result

#bitwise operator are used in binary works
#0=00
# 1=01
# 2=10
# 3=11
