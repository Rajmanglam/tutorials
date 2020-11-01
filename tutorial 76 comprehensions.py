# so let us print a table of 3 using loops
les=[]
for i  in range(100):
    if i%3==0:
        les.append(i)
print(les)
# now let us understand to do it in one line using comprehensions
lk=[i for i in range (100) if i%3==0]
print(lk)
# this was called list coomprehensions


# now we will learn about dictionary comprehensions
# suppose we have to create a dictionary which gives something like this
# {0:'item0'}
# suppose we have to do this till hundred then it  will take very time so one way to do this will a lot of time
# so we will use dictionary comprehensions
dict1={i:f"item{i}" for i in range (100)}
print(dict1)

# and we can even use it  to print table of 3 like this in this format
dict2={i:f"item{i}" for i in range (100) if i%3==0}
print(dict2)

# we can even change the value of dictionaries like this
dict3={i:f"item{i}" for i in range (5)}
print(dict3)
# this will print {0: 'item0', 1: 'item1', 2: 'item2', 3: 'item3', 4: 'item4'}
dict3={key:value for value,key in dict3.items()}
# this will change the value and print it like this
# {'item0': 0, 'item1': 1, 'item2': 2, 'item3': 3, 'item4': 4}
print(dict3)


# now let's learn about set comprehensions
dresses={dress for dress in ['dress1','dress2','dress3'
                            ,'dress4','dress5','dress6']}
print(dresses)


# now let's learn about about generators comprehension
evens=(i for i in range (100) if i%3==0)
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
