i=0
while(True):#while True is a while loop that will run forever
    print(i+1, end="\n")
    if(i==44):break#stop the loop
    i=i+1
#loop day break hone ke baad yaha aa jaye ga

j=0
while(True):#while True is a while loop that will run forever
    if(j+1<5):
        j = j + 1
        continue# ye continue statement ise phir say loop ke starting pe pahucha dega
    print(j+1, end=" ")
    if(j==44):break#stop the loop
    j=j+1
#loop day break hone ke baad yaha aa jaye ga


#QUIZ- when user enters a number if it is greater than 100 stop the program and
# if it is smaller than 100 print try again
while(True):
 print("\n enter a number ")
 n=int(input())
 if(n>=100):
     print("congo you entered a number greater than 100")
     break
 else:print("try again")
 continue