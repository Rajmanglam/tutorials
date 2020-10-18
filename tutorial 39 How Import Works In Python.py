# first we will take the notes because here it's not some type of code


# In this tutorial we aim to understand the working of the import statement,
# so we can have a better grasp of the concept and resolve common importing issues.
# In Python, we give access to a module by using a keyword import.

# HOW DOES IMPORT KEYWORD WORK?
# When we write a certain module name along with the import keyword,
# it will start searching for a file with that name having an extension .py.
# After finding the file, it will import it into our program, which means that it will
# permit our program to use the functions of the certain module we imported.
# We can import a module named “sys” to see the path that our
# import statement takes while searching for a module.

import sys
print( sys.path)
 # this will give list of directories
['C:\\Users\\rajma\\PycharmProjects\\tuts',
 'C:\\Users\\rajma\\PycharmProjects\\tuts',
 'C:\\python 37\\python38.zip',
 'C:\\python 37\\DLLs',
 'C:\\python 37\\lib',
 'C:\\python 37',
 'C:\\python 37\\lib\\site-packages',
 'C:\\python 37\\lib\\site-packages\\win32',
 'C:\\python 37\\lib\\site-packages\\win32\\lib',
 'C:\\python 37\\lib\\site-packages\\Pythonwin']
# they are actually the path from which the python interpreter will bring the module
#chalo ab coding kr low

# their are 2 ways to import a file or module


# 1
import time as time
print(time.localtime())

# we can even do something like this
import tutorial39support
print(tutorial39support.i)
# here we have created a file named tutorial39support and imported it and used the variable i
# which had a value of 9893 and printed it
print(tutorial39support.joke(121))
