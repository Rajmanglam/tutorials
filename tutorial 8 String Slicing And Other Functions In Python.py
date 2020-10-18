myst = "raj is a good boy"
print((myst))

print(myst[0:4])#this [0:4] will print values from only 0 to 3 number
#ie : raj because 4 is excluding value so if we want to print 0 to
#4 we will write[0:5]

print(len(myst))#this will show the size of variable"""

print(myst[0:5:2])#now when we wrote 0:5 it printed values
# from 0 to 4 but the last :2 was used to to set gapping like
#as we have set 2 so the second alphabets are not printed in
#between 0 to 4"""

print(myst[-4:-2])#here it sent the code in backward direction
# and due to it and so it went to -4 values which is just a space as
# you can see and it will go till -2 which is 'o' but it is execluded as
# you learnt above so it will take the -1 value which is 'b'

print(myst[::-1])# in this case the string will printed in
# reverse format

print(myst.isalnum())#here isalnum cheaks that whether the variable
# apha(al) type or numeric(num) type
# alpha means has no space in between
# numeric means having number values

print(myst.isalpha())#here it will cheak that is the variable
# alpha type

print(myst.isnumeric())#here it will cheak that is the
# variable numeric

print(myst.endswith("boy"))#this will show it as true because last
# word is boy but if I do it something like this

print(myst.endswith("body"))#it will show false because it is not ending
# with body

print(myst.count("o"))#it will tell us the count of alphabet 'o' in variable myst
# the aphabet in the (" ") is shown as how many times

print(myst.capitalize())# it will capatalize the first letter of variable

print(myst.find("is"))# it is used to find a specific word in variable
# we are displayed the numeric place of the word

print(myst.upper())# it will convert the whole string in uppercase

print(myst.lower())# it will convert the whole string in lowercase

print(myst.replace("is","are"))# it will replace 'is' with 'are' , in such function
# the frist entred string is replaced with second string

#### END OF PROGRAM ####
