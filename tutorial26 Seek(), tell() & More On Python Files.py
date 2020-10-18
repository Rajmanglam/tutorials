h=open('manglam.txt')
print(h.readline())# this will print the first line
print(h.readline())# this will print the second line

#Now suppose that we have a lot of lines and we need to know where our file pointer is exactly
# then we use '.tell' function let's see how
print(h.tell())

# Now suppose that we want to print the first line again but if we use the readline function
# again it print the next line so in such cases we use  'seek' function like this
h.seek((30))# now our file pointer will go to 29th character and will print that line if we use readline function
print(h.tell())
print(h.readline())
print(h.tell())
h.close()