lis=['john','cena','randy','orton','khali','jinder mahal']
for item in lis:
    print(f'{item} and', end=' ')
print('these are some wwe superstar')

# this is one way of  printing items of a list but their is an another method to do this
# using join function
a='  and  '.join(lis)+'  these are some wwe superstar'
print(a)