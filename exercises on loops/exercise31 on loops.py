# Write a Python program to calculate a dog's age in dog's years. Go to the editor
# Note: For the first two years, a dog year is equal to 10.5 human years.
# After that, each dog year equals 4 human years.
# Expected Output:
#
# Input a dog's age in human years: 15
# The dog's age in dog's years is 73
d=int(input('enter the age of dog \n'))
a=0
if d <= 0:
    print('enter a positive number computer hoon gadha nhi')
    exit()
for i in range (d):
    if i==0 or i==1:
        a=a+10.5
    else:a=a+4
print(a)