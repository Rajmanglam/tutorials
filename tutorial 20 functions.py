# there are to types of fuctions
# predefined functions = already defined by user
# and user defined functions = we create them
a=4
b=4
print(sum((a,b)))# the syntax of sum function is sum((numbers))

#LET'S LEARN TO CREATE A FUNCTION
def func1():
    print("hello you are in function")
# HERE WE CREATED A FUNCTION THE FORMAT OF CREATING A FUNCTION IS
# def 'function name()':'code of the function'
print(func1())# here if we print the function it will along with the
# function also return a void value named NONE to avoid
#but if we do not do the print function likr this
func1()#it will not give any return as none


i=0
def func2():
    print("hello you are in function",i)
    return" "
print(func2())# here it will not give any return value because we have put blan space in return
while(i<91):
    print(func2())
    i=i+9
# here we printed the table of 9 using function and putting i and increasing in by 9 every time
def func3(l,m):
    print("hello you are in function",l+m)
    return" "
func3(9,4)# here we setup two variables l and m and put 9 and 4 in them

#now let's learn to  print average of two numbers like this
def func4():
    print('enter the first number')
    n1=int(input())
    print('enter the second number')
    n2=int(input())
    average=(n1+n2)/2
    print(average)
    return" "
print(func4())

def func5():
    print('enter the first number')
    n4 = int(input())
    print('enter the second number')
    n5 = int(input())
    average = (n4 + n5) / 2
    print(average)
    return "average "
mm=func5()#we can even print store it in a variable like this

# now let's learn about doc string
def func7():
    """this function is used to calculate average"""
    print('enter the first number')
    n10=int(input())
    print('enter the second number')
    n11=int(input())
    average=(n10+n11)/2
    print(average)
    return" "
#in the above function the first line of this function is called doc string
print('\n',func7.__doc__)#now this will give us the doc of func7
