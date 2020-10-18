#first create a text file manglam

f=open("manglam.txt","rt")# here we used the open function to open our file manglam.txt
# and then stored it in a variable(file pointer) 'f'

content=f.read()# we can't open and read it directly so we stored it in a variable
# named content and put f there and used the read function that read it

print(content)# now we printed it using print statement

f.close()# once we opened a file we have to close it using close function
# to free the resources used to open  the file

# syntax to open a file- open("filename" ,"mode") for example
# open("myfile.txt")
# we stored the returned output by the function-
# f = open("myfile.txt," "w")
# we can read it without even using .read function like this-
# f = open("myfile.txt", "r")
# f.read(2); #Here, you will get the first two characters of the file.


#but if we want to iterate it and print each alphabet/line in single line
f=open("manglam.txt","rt")
for line in f :
    print(line)#this will print each line of  the file in seperate line


f=open("manglam.txt","rt")
print(f.readline())# this will print one line from our file
print(f.readline())# this will print next line from statement


for line in content :
    print(line)#this will print each alphabet of  the file in seperate line


#NOTE: everytime we do printing using for loop or readline statement we need to open
# it and store it in a pointer that we are going to use a open statement
