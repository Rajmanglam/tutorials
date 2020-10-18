list1 = [ ["Harry", 1], ["Larry", 2],#here we have created a list because for loop
           ["Carry", 6], ["Marie", 250]]
dict1 = dict(list1)# here we have created a dictionary and put the value of list in it
for item in dict1:# while printing the items we use the item keyword
    print(item)


list1 = [ ["Harry", 1], ["Larry", 2],
           ["Carry", 6], ["Marie", 250]]
for item, lollypop in dict1.items():# here lolltpop is used to store the numbers
     print(item, "and lolly is ", lollypop)

# write program which from a list will print only numeric value greater than 6
items = [int, float, "HaERRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]
for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)

