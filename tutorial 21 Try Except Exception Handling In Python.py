print('enter the two numbers whose sum you want')
num1=int(input())
num2=int(input())
print(num1+num2)

print('enter the two numbers whose sum you want')
a=input()
b=input()
try:
    print(int(a)+int(b))
except Exception as A:
    print(A)
print('this is very important code')
#In this above code it will take input in a and b and then it will try
# to run the print statement in try: function but if we put any string
# value and it is not able to add them as integer then it will not run
# the print statement and the error that should be displayed is stored in
# exception A and will print it as a string and then will run the next line