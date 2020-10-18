# Write a Python program to count the number of even and odd numbers from a series of
# numbers.
number=[9,8,97,4,3,535,35,35,33,4]
odd=0
even=0
for i in range(len(number)):
    k=number[i]
    if k%2 == 0:even=even+1
    if k%2 != 0:odd=odd+1
print('Number of odd numbers is',odd)
print('Number of even numbers is',even)