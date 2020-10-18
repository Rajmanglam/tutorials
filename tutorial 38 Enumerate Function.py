l1=['bhindi','aloo','chopsticks','chowmein']
#suppose that we want to print only items at odd number places then we will

# so one thing we can do is
i=1
for item in l1:
    if i%2 != 0:
        print(f"{item}")
    i+=1

# now this process was very time taking and tuff so another way is enumerate function

for index,item in enumerate(l1):
    if index%2==0:
        print(f"{item}")
