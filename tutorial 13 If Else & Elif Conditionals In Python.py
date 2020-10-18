var1 = 3829
var2 = 3283
print('enter a number')
var3 = int(input())
if (var3>var1):
    print("var3 is greater than var1")
if (var3==var1):print("both are same")
else: print("var3 is greater than var1")
# here we have used to make a decision using if-else statement it's syntax is:
# if(condition): do this
# else : do this

#just another way of doing it is else if which in python is elif
#same program as above using elif

var4 = 3829
var5 = 3283
print('enter a number')
var6 = int(input())
if (var6>var4):
    print("var3 is greater than var1")
elif(var6==var4):print("both var4 an 6 are same")
elif(var6>var5):print('var6 is greater than var5')
elif(var6==var5):print('var6 an var5 are equal')
else: print("var6 is smaller than both var5 and var4")

list=[48,49,58,290]
print(55 in list)
if (55 in list) :print("55 is in list ")# the in function is used to cheak
# involvement of a item in list we have to first put it in a print statement


list1=[48,49,58,290]
print(55 not in list)
if (55 not in list) :print("55 is not in list ")# the not in function is used
# to whether a function is not in list

#quiz- to cheak if a person is eligible to drive
print('enter your age')
age=int(input())
if(age>18 and age<100 and age>7):print('you can drive')
elif(age==18):print('you have to come and meet us' )
elif(age<18 and age>7and age>100):print('you cannot drive')
