import random
#here we have imported a module named random which will allow us to use all pre-defined functions
# of the module RANDOM
n=1
y=100
random_number=random.randint(n,y)#here this randit function will print any random number between
# n and y
print(random_number)

rand=random.random()#this will print any one random number between 0 and 1
ran=random.random()*100#this will print any one random number between 0 and 100
print(ran,rand)

lst=['aaj tak','dhruv rathee','code with harry','dd1','set max']
# here we have created a lst having channel names
k=random.choice(lst)# this will print any random channel from the list 'lst'
print(k)

#some modules are pre installed but we need to install some modules using pip functions
# using "pip install 'module name'"
