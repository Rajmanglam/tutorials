# Regular expressions are used to perform search-related tasks in Python. In this
# tutorial, our primary focus should be on understanding because we are going to cover
# a concept that has a wide range of uses. To work with
# regular expressions, we have to import a built-in module in python called ‘re’.
import re
mystr= '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''
# The module defines several functions and constants to work with RegEx. The “re” module is composed of five functions known as:
#
# findall: It finds all search for matches and print resultant in the form of a list.
# search: It works the same as a findall, but the resultant is a matched object, if any found.
# split: The split function splits the string from every matched into two new strings.
# sub: The sub-function works exactly like a replace function in notepad or MS Word,
# it replaces the original word, with a word of our choice.
# finditer: The finditer yields an iterator as a resultant with all the objects that match
# the one we sent it) finditer supports more attributes than any other function defined above.
# It also provides more details related to the matched object. So, most of the examples we
# are going to see next will contain a finditer function in them.

patt=re.compile(r'fass')
matches=patt.finditer(mystr)
for match in matches:
    print(match)
    print(mystr[448:452])

# in this way we can find any text in a string
# let's use some meta characters using which we can do a much advanced searcing
patt2=re.compile(r'.')# this will search everything
patt3=re.compile(r'.adm')# this will search words ending with adm
patt4=re.compile(r'^Tata')# here if our file would be starting with tata it would return something but if not it will
# give nothing
patt5=re.compile(r'ii$')#here if the file would be ending with ii it would return else vice-varsa
patt6=re.compile(r'ai*')#here if it will search a with any number of ending i
patt7=re.compile(r'ai+')#here this means a and minimum one i infornt of it
patt8=re.compile(r'ai{2}')#here this means exactly two i infront
patt9=re.compile(r'(ai){2}')#here this means exactly two ai
patt10=re.compile(r'ai{2}|t')# here this means either aii or t

matches=patt10.finditer(mystr)
for match in matches:
    print(match)
    print(mystr[448:452])

#THERE ARE MANY OTHER TYPE OF META CHARACTERS AND SPECIAL SEQUENCES WHICH YOU CAN LEARN FROM DOCUMENTATION
#OR SEE THE VIDEO OF HARRY
