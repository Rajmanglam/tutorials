# now let us create our first class in python
class student():
    pass

# so above we have created a class student and named it student
# here we have used pass and the function of pass is to help us in situations
# where we do not want to give any code but if we leave them blank then it will show
# error so to avoid taht we use pass

harry=student()
larry=student()

# here we have created two variables harry and larry and specified them to student()
# but this dose not mean that  they will have same values you can cheak it like this

print(harry,larry)

# this will give us memory locations of our variables and if you see them then it
# will show different memory locations

harry.name = "Harry"
harry.std = 12
harry.section = 'I'
print(harry.name,harry.std,harry.section)

# understand only this much for this tutorial and will learn more about classes in
# next tutorials
