#first we will learn about lists
grocerry = ["bhindi","vim","potato","sunflower oil",839389,928.929]
print(grocerry) #as we saw here we created a list here and we can also add numbers and floats also in it

#now we will learn to access any specific item from list like shown in next line
print(grocerry[1])#here by adding [1] we asked it to print 1th number item in list

#we can even make a number object like this
numbers = [77,23,42,244]
print(numbers)
print(numbers[2])#and we can access a specific number in same way

#now we will see how to sort a number
numbers.sort()#this function will sort our number list and we will now be able to print it in sorted form
print(numbers)

numbers.reverse()#this will print our sorted numbers in reversed form
print(numbers)

print(numbers[0:3])#now this will print or list from item 0 to 3 and will print 0th,1th and 2th items
print(numbers[:3])#it anyways take 0 by default like this
print(numbers[1:])#in this case the 0th value would be ommited

print(numbers[::2])#in this function parameter 1 and two are taken as default of 0 and 3 respectively
# but the third parameter defines the skip in list like in this list all the second pllaces
# will be ommited
print(numbers[::-1])#here if we put -1 in 3rd parameter and do not put any value in the first and second
# parameter and let them be default value the list will be reversed but if we put any value in
# them or put any other negative value the list we become blank
print(type(numbers))#it will show it's class. like this there are many functions that you use
# try them- len,max,min,sets with syntax  --- print(function name(list))

numbers.append(88)#this will add the number in brackets to end of list as append function
# adds items to end of list. NOTE:it takes only one value at once
print(numbers)
#with append we were able to add numbers to end but if we want to add numbers to a specific nth point
# at list we will do this
numbers.insert(3,88)#this insert function will add 88 in the 3rd index
# here the first parameter is the point of list and 88 is the value we want to add
print(numbers)
numbers.remove(244)#this will remove 244 from list
print(numbers)
numbers.pop()#this function will remove the last item from list
print(numbers)

numbers[2] = 77#in this way we can change the value of list at a specific point
print(numbers)

#now we will learn a new thing called topple but first we must learn two new terms
# MUTABLE AND IMMUTABLE
# MUTABLE = which can be changed (lists are mutable)
# IMMUTABLE = which cnanot be changed (toppels are immutable)

raj = ("good","handsome","genius")#here this is topple and the only thing it has different
# from list is that we have to put paranthesis instead of square brackets
print(raj)
#raj [2] = "bad" # here this will show error because it is a topple and can't be changed you can
# cheak it by uncommenting it


 #now we will see how to interchange value of two variables using normal method and python method

 #normal method
a = 22
b = 32
print(a,b)
#now let's change them
c =a
a=b
b=c
print(a,b)

#another more easy way that is a profit of using python
a=22
b=32
print(a,b)
a,b=b,a
print(a,b)

