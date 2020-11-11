# In this tutorial we will get to learn the functionality and usage of OS module
import os
# print(dir(os))
print(os.getcwdb())# here the cwd stands for (current working directory) and it gives us
# the current working directory
# now let's learn how to change the current working directory
# os.chdir('C://')
#now physically the program is 'C:\\Users\\rajma\\PycharmProjects\\tuts' but in reality it's
#location has changed to 'c:\\'
print(os.getcwdb())
print(os.listdir())#this function will give us all the files of the directory we are
#working in
print(os.listdir('c://'))#this function will give us all the files of the directory C:\\
# we are working in
"""os.mkdir('this')#this will create a folder named this"""
# os.mkdir('this/that') this will give a error because as this does not exist
#to avoid this we will do
"""os.makedirs('this/that')#this will create a folder this and a subfolder that inside it"""
"""os.renames("log.txt", "logs.txt")"""#this will change names of files
"""print(os.environ.get('Path'))"""#this will give us the environment variable
"""print(os.path.join("C:/", "/harry.txt"))"""#this will add two paths
print(os.path.exists("C://"))# this tells us weather a certain file exists
print(os.path.isfile("C://Program Files"))# this will tell us weather it is a file
