# Write a Python program that prints each item and its corresponding
# type from the following list.
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1),
# [5, 12], {"class":'V', "section":'A'}]
list1=[534,34.4,'ginr',(99,'ottomon'),['hello','man',0],99]
for i in range(len(list1)):
    print('type of',list1[i],'is',type(list1[i]))