import time
#
# k = 0
# while (k < 45):
#     print("This is harry bhai")
#     k += 1
#
# for i in range(45):
#     print("This is harry bhai")
#

#now we have to loops for printing same value 45 times and suppose we want to know which
# loop runs faster we use time modules

initial=time.time()# this will tell time in tik units at this point of program
print(initial)
k = 0
while (k < 10):
    print("This is harry bhai")
    k += 1
print('time took by while loop to run was',time.time()-initial)
initial2=time.time()# this will tell time in tik units at this point of program
for i in range(10):
    print("This is harry bhai")
print('time took by for loop to run was',time.time()-initial2)
# IN THE ABOVE CODES THE EXECUTION TIME WAS TOO SHORT TO BE MENTIONED SO IT WILL SHOW
# 0.0 SECS SO DON'T THINK CODE IS WRONG
# IF WE JUST INCREASE THE LOOP TOO 1000000 TIMES IT WILL SHOW
# 11.188894510269165 SECONDS

k=time.asctime(time.localtime(time.time()))#this will tell us real worldd time
print(k)

#now let's learn sleep function
p=time.time()
k = 0
while (k < 10):
    print("This is harry bhai")
    time.sleep(1)
    k += 1
print('time took by while loop to run was',time.time()-p)
#In the above loop it will go in loop print our argument wait for 1 second then
# will move further and run  again and it go on