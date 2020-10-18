print("hello world ")
#this is one way of doing it let's see how to do it using variables
#and what are variables

#VARIBLES ARE BASICALLY CONYAINERS IN WHICH WE STORE SOMETHING

#let's see how

var1 = "hello world"#it is a string
print(var1)
#we now did the hello world program using variable

var2 = 4 #it is an integer type variable

var3 = 55.67 #it is a floating point variable(float)

print(type(var1)) # it will tell us the type of varible which here is STRING
# and will be shown as <class 'str'>

print(type(var2)) # it will tell us the type of varible which here is STRING
# and will be shown as <class 'int'>

print(type(var3)) # it will tell us the type of varible which here is STRING
# and will be shown as <class 'float'>

print(var2+var3)#this will not show any error and will add values of var2 and var3

#but var2+var1 will show error as var1 has alphabets and the computer
# cannot understand it but something like this will work

var4 = "go to hell"# we are creating a new string variable
print(var1+var4)
#it will not show any error and will show result
#hello worldgo to hell
#here both are string so are added easily
#but now if we will do something like this
var5 ="55" #and add it like
print(var1+var5)
#it will work because 55 is in between "" and such values are srtring

#Now lets understand something else
var6 = "44  "#we create da new string variable var6
var7 = "7849" #we create da new string variable var7
#and if we add them like this
print(var6+var7) #it will show something like this 44  7849 here both are strings so they are not added
#but we can do it by converting then in integers. lets do it
print(int(var6)+int(var7)) #int(variable name) is the method through which we can convert any value to int
#and it will show the result 7893

#now let's consider that we want to print hello world 10 times so one method is
# writing the command 10 times another is
print(10*"hello world")#this will print hello world 10 times like this
#hello worldhello worldhello worldhello worldhello worldhello world helloworldhello worldhello worldhello world
print(10*("hello world\n")) #htis will show the result like this
#hello world
#hello world
#hello world
#hello world
#hello world
#hello world
#hello world
#hello world
#hello world
#hello world
#but if we do something like this
print(100*(var2))#it will multiply the value in the variable with 100 as it is integer


#now let's  see how to take values from user
print("enter a number")
inpnum = input()# here inpnum is a variable name and input() is the function to take the value
#NOTE : value is stored as string so it can't be added with integer values
print("you entered ", inpnum)#this will show the number we entred
#but if we want to add a number to it we will do something like this
print("your number with 100 added in it is",int(inpnum)+100 )
#QUIZ = adding two numbers
print("ENTER THE FIRST NUMBER")
n1= input()
print("ENTER THE second NUMBER")
n2= input()
print("THE SUM OF THE TWO NUMBERS IS=", int(n1)+int(n2))
