def printname(a,b,c,d):
    print(a,b,c,d)
printname('raj','manglam','rohan','raju')
# this above function will print name of four people 'raj','manglam','rohan','raju'

#now suppose we want to add a name named shivam so we can do this
def printname2(a,b,c,d,e):
    print(a,b,c,d,e)
printname2('raj','manglam','rohan','raju','shivam')
# now this will print 5 names but suppose we are working with billions
# of users so this will be very clumpsy

# now we will use args for it
def funargs(*args):
    print(args)
k=['raj','manglam','rohan','raju','shivam','sumit','salman']
funargs(*k)
#in this way we have printed name of the people and we can change the names by just changing
# the list and by the way they are stored in as a tupple

# and we can even print a single name like this
def funargs2(*args):
    print(type(args))
    print(args[0])
funargs2(*k)

# NOTE: it is not necesarry for the name to be args it can be any variable in this format:
# def function name(* variable name)

# And we can even print using a loops

def funargs3(*args):
    print(type(args))
    for i in args:# we use this type of loops for tupples or alphabet type
        print(i)
funargs3(*k)

# and we can even do this

def funargs3(rohan,*args):
    print(rohan)
    for i in args:  # we use this type of loops for tupples or alphabet type
        print(i)
rohan='Name of our some students are'
funargs3(rohan,*k)

# but we can't do like this'
#
# def funargs3(*args,rohan):
#     print(rohan)
#     for i in args:  # we use this type of loops for tupples or alphabet type
#         print(i)
# rohan='Name of our some students are'
# funargs3(rohan,*k)

# SO WE CANNOT PUT A VARIABLE NAME AFTER ARGS IN A FUNCTION


# Now let's learn about kwargs

def funargs4(**kwargs):
    for key, value in kwargs.items():
        print(key,'::',value)
        #(for key, value in kwargs.items():)
        # we use such types of loops while printing a key and value type data type such
        # as dictionary
print('and some of our heros are')
kw={'raj':'coordinator','rohan':'monitor','shivam':'fitness trainer'}
funargs4(**kw)

# so basically kwargs help us to print a key:value type of values such as  dictionaries


# NOTE: it is not necesarry for the name to be kargs it can be any variable in this format:
# def function name(**variable name)