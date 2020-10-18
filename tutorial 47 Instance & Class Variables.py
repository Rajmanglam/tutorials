class employee():
    pass

harry=employee()
rohan=employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"
 # here we have given some attributes to rohan and harry
# but suppose we ahve to do this for millions of users then it would be great trouble
# so we will do something like this if we want to apply a common thing to all  variables
# of the class

class employee2():
    number_of_leaves=10
    pass
# here we have given a variable to this class so we do like ths
harry1=employee2()
rohan1=employee2()
print(harry1.number_of_leaves,'\n',rohan1.number_of_leaves)
#here we have taken out number of leaves of both without specifying them so this
# is one of the advantages of using class

# we can change number of leaves of a class like this
employee2.number_of_leaves=60
print(employee2.number_of_leaves)

# here we have changed the value of number_of_leaves like this but we can't change it
# like this
rohan1.number_of_leaves=90
print(rohan1.number_of_leaves)
# this will change the value of number of leaves for rohan1 by
# creating a instance variable
print(employee2.number_of_leaves)
# but the value of employee2.number_of_leaves is not changed here
print(rohan1.__dict__)# this will give us all attributes of rohan