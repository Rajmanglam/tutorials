# Scope refers to the coding area where a particular Python variable is accessible

l=99#here this is global variable and will be used in all functions or any other place in the
# program THIS IS CALLED GLOBAL SCOPE

def function(n):
    l=10# here this is local variable.A local variable is a variable we use in a specific function
    # and that value can only be used in that function we will se it in more depths later
    # and if we print l then it will print 10
    # because the function will search for value of 'l' first in this program and if it gets the
    # value then it prints it else it search for a global variable with the name and prints that value
    m=55# here this 'm' is a local variable and it can only be used in the function suppose
    # if we print the variable outside the fuction then it will show error
    print(n,'I AM GREAT')
    print(l,m)
function('i am hero')


k=99#here this is global variable and will be used in all functions or any other place in the
# program THIS IS CALLED GLOBAL SCOPE
def function1(n):
    b=55
    #now suppose that we want to  change the value of the global variable k so that when
    # used in any function then it shows the value defined in this function for this we use the
    # global keyword
    # k=k+23 here this will show error as we can't change value of a global variable just like that

    global k # now as we have used this global k we can change value of k
    k=k+23
    print(n,'I AM GREAT')
    print(l,b)
function1('i am hero')

# now we will learn something new about nested functions
def raj():
    x=50
    def manglam():
        global x
        x=66
        # now you will think that value of x will be changed as we have used global variable
        # but if you notice x is a local variable in function raj  so it will remain 50 only
    print('before calling manglam',x)
    manglam()
    print('before calling manglam', x)
raj()
print(x)#here it will print 66 because because when we used global x then it went out of the
# function and created a variable x with value 66