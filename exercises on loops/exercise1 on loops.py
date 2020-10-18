# 1. Write a Python program to find those numbers which are
# divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
i=1501
while(i>1500 and i<2700):
        if(i%7==0 and i%5==0):
            print(i ,end=" ")
        i=i+1