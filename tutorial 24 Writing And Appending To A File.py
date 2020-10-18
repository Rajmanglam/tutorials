f=open("manglam.txt",'w')#here we chose a file>opened
# it>defined that we have to write something in it using 'w'
f.write("manglam bhai bhut achha hai")# this will clear our data in manglam.txt
# and enter our entered data in it
f.close()

# In the above program it will add entered data in our existing file but if the file
# do not exsist it will create a new one like this

h=open("manglam2.txt",'w')# here manglam2.txt named file did not exsist but we created
# it and you can create it like this or just enter manglam3 in place of manglam2
# and it will create a new file named manglam3 and enter the data in it
h.write("this is file two")# entered data in it you can create any other file
# like this
h.close()

b=open("manglam3.txt",'a')# here we have added our data to previos file using append
b.write("manglam bhai bhut achha hai")
a = b.write("manglam bhai bhut achha hai")#this will tell us the number of characters we have entered
print(a)
b.close()

# Handle read and write both
j = open("manglam2.txt", "r+")
print(j.read())
j.write("thank you")
j.close()
