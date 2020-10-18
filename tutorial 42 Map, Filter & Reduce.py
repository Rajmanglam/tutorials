numbers=['54','55','65','54']
# numbers[1]=numbers[1]+665
# here this will give error as we can'tt add a number to a string
# so here we will first convert them to integers
for i in range(len(numbers)):
    numbers[i]=int(numbers[i])
numbers[1]=numbers[1]+665
print(numbers[1])

# here using for for each time converting in very clumpsy so we use maps like this
numbers=list(map(int,numbers))
numbers[2]=numbers[2]+665
print(numbers[2])
# this will also do the same work

def sq(a):
    return a*a
num=[2,3,4,5,6,7,8,9,10]
kall=list(map(sq,num))
print(kall)

# we can even do it using lambda like this
num2=[2,3,4,5,6,7,8,9,10]
kallt=list(map(lambda x:x*x,num))
print(kallt)

def sq(a):
    return a*a

def cube(a):
    return a*a*a

func=[sq,cube]
for i in range(5):
    kal=list(map(lambda x:x(i),func))
    print(kal)

# NOW LET'S LEARN ABOUT FILTER
# we will simply filter using FILTER
ko=[5,3,4,2,4,8,7,8,90]
k=lambda x:x>5
ko2=list(filter(k,ko))
print(ko2)

# ok  so let's learn about reduce
from functools import reduce
lsf=[44,5,4,334,44]
# suppose we have to add them to a variable named num so we will do this
num=0
for i in lsf:
    num=num+i
print(num)
# this is a very lenthy way of doing this and another way of doing it is
numm=reduce(lambda x,y:x+y,lsf)
print(numm)
