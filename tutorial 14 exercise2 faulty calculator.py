#45*3=555, 56+9=77, 56/6=4
print('Enter the first number')
a=int(input())
print('Enter the second calculator')
b=int(input())
print('Enter the operator')
c=input()
if(c=='*'):
    if(a==45 and b==3):
        print('555')
        k=a*b
    else:
        print(a*b)
elif(c=='+'):
    if(a==56 and b==9):
        print('77')
    else:
        print(a+b)
elif(c=='/'):
    if(a==56 and b==6):print('4')
    else:print(a/b)
l=input('enter anything and press enter to close the terminal')
print(l)