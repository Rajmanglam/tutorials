# Write a Python program that accepts a string and calculate the number
# of digits and letters.
n=input('enter anything you want \n')
k=len(n)
l=0
p=0
for i in n:
    if i.isdigit():
     p=p+1
    elif i.isalpha():
     l=l+1
    else:continue
print('number of alphabet is',l)
print('number of numbers is',p)


