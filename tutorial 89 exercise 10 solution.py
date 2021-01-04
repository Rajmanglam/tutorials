import pickle
k=open('C:\BOOKS\iris\iris.data', 'r')
l=k.read()
p=l.splitlines()
# print(p)
print(type(p))
k.close()
# print(p)

#pickling
file="picklediris.pkl"
fileobj=open(file,'wb')
pickle.dump(p,fileobj)
fileobj.close()

#depickling
file='picklediris.pkl'
fileobj2=open(file,'rb')
mycar=pickle.load(fileobj2)
print(mycar)