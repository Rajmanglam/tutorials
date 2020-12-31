# In this tutorial, we are going to learn about the pickle module in python. Pickle means to
# preserve, and in Python, we use it for the same purpose. Pickle comes handy while saving
# complicated data. They are easy to use, lighter, and does not require several lines of code.
# The pickled file generated is not easily readable and thus provide some level of security.
import pickle
#PICKLING
cars=['Audi','Maruti Suzuki','BMW','Honda City','Hyundai']
file='mycar.pkl'
fileobj=open(file,'wb')
pickle.dump(cars,fileobj)
fileobj.close()

#DEPICKLING
file='mycar.pkl'
fileobj2=open(file,'rb')
mycar=pickle.load(fileobj2)
print(mycar)