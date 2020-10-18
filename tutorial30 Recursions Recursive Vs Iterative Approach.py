def print2(str1):
      # print2(str1) here this is called recursion in which we have called a function inside a same
      # function and it will show error
     print('this is ',str1)
print2('function1')

#we will learn how to use recursion using an example of FACTORIAL
# first let's understand what is factorial
# factorial of any number(n) is- n*n-1*n-2*n-3..... till the value of n becomes 1
# eg:5-----    5*(4)*(3)*(2)*(1)=120
# or if you see it can also be 5*(5-1)!
# therefore factorial of 5 is 120 or 5!=120

def factorial(n):#this was a type of iterative recursion
    #it's function can be written as
    fac=1
    for i in range (n):
         fac=fac*(i+1)
    return fac
number = int(input('enter the number \n'))
print('factorial using iterative is',factorial(number))


def factorial_recursive(n):
    if n==1:
        return 1
    else :
        return n*factorial_recursive(n-1)

# this will work something like this
# 5 * factorial_recursive(4)
    # 5 * 4 * factorial_recursive(3)
    # 5 * 4 * 3 * factorial_recursive(2)
    # 5 * 4 * 3 * 2 * factorial_recursive(1)
    # 5 * 4 * 3 * 2 * 1 = 120

number = int(input('enter the number \n'))
print('factorial using recursive is',factorial_recursive(number))



# quiz= write function to print fibonicci number
# pattern of fibonicci number=
# 0,1,sum of last two number,sum of last two number,sum of last two number,sum of last two number
# 0,1,1,2,3,5,8....
def fibonicci(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fibonicci(n-1)+fibonicci(n-2)
l=int(input('enter the number\n'))#here number is the spot at which number is
print(fibonicci(l))