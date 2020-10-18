i=1
j=1
n=int(input('print the number 1 or 0 \n'))
m=bool(n)
e = int(input('enter the number of rows \n'))
if m==True:
    for i in range(1, e + 1):
        for j in range(1, i + 1):
            if j <= i:
                print('*', end='')
            else:
                print(' ')
        print(' ')

elif m==False:
    for i in range(e,0,-1):
        for j in range(0,i):
            if j <= i:
                print('*', end='')
            else:
                print(' ')
        print(' ')