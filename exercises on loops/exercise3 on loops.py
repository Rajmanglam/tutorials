# Write a Python program to construct the following pattern, using a nested for loop.
# *
# **
# ***
# ****
i=1
j=1
e = int(input('enter the number of rows \n'))
for i in range(1, e + 1):
        for j in range(1, i + 1):
            if j <= i:
                print('*', end='')
            else:
                print(' ')
        print(' ')

