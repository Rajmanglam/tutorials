# 4. Write a Python program to construct the following pattern, using a nested for loop.
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
k=5
i=1
p=1
for i in range(4):
    print('*'*p)
    p=p+1
for i in range(5):
    if k==0:k=k+1
    print('*'*k)
    k=k-1



