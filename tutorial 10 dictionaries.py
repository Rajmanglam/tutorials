# dictionaries are key value pairs

d1 ={}# for creating a dictionary we have to put all the sata in curly brackets
print(type(d1))#it will show type of d1 variable

d2 = {"ram":"fish" , "sohan":"roti" , "shyam":"burger"}#what is the syntax pof writing a dictionary?
# variablename = {"word":"meaning" , .....}
print(d2)

print(d2["sohan"])#this will print liking(meaning) of sohan only

#we can also create a dictionary in a dictionary like this
d3 = {"ram":"fish" , "sohan":"roti" , "shyam":"burger" ,
      "maddy":{"lunch":"rice","breakfast":"bread jam","dinner":"chicken"}}# "maddy":{"lunch":"rice","breakfast":"bread jam",
                                                                          # "dinner":"chicken"} is the dictionary
# we created for maddy
print(d3)

print(d3["maddy"]["lunch"])#here it will print the value of lunch in maddy in d3

d3["ankit"] = "chinese food"#now this will add a name ankit with liking chinese food
print(d3)

del (d3["ankit"])#it will delete ankit from dictionary
print(d3)

print(d3.copy())#this will make a copy of d3 dictionary

print(d3.get("sohan"))#this will give us the value of sohan

d3.update({"harshit":"bats"})#this will add a value harshit in the dictionary
print(d3)

print(d3.keys())#it will print all keys of d3

print(d3.items())#to get all the items of the dictionary
