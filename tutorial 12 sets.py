s = set()# making a set
print(type(s))

making_set_from_list = set([12,48,239,478])# putting values in sets using lists
print(making_set_from_list)

s.add(22)# adding values in set 's' NOTE: more than one value cannot be entered in set
s.add(22)# it will not add 22 again because sets take one value only once
s.add(232)# but this 232 will be added
print(s)

s1=s.union({33,54,21,34})# in this way using s.union we can add multiple values directly in a set
# and as we have used the union function it will put the values of set 's' also in it
s1.remove(33)# this will remove 33 from set s1
print(s, s1)

