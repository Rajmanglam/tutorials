# build a dictionary which gives meaning of word entered by user
oxford = {'mutable' : 'can be changed','immutable':'can\'t be changed',
          'light':'A form of energy'}
print("enter the word whose meaning you want")
word = input()
print(oxford[word])