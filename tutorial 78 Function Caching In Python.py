import time
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    # some_work(3)
    # some_work(3)
    # print("called again")


#suppose we want to run this function 10 times so we have to wait 30 secs
    # but suppose we run it only once and store the value somewhere then it will take only
    # 3 seconds
    # we do this using function chaching
    #let's do a fresh start

from functools import lru_cache
@lru_cache(3)#this is a decorator and we have specified 3 so
# that it stores last three executions
def some_work2(n):
    #Some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work2(3)
    print("called again")
    some_work2(3)
    print("called again")
    some_work2(3)
    print("called again")
#here the first execution will take 3 seconds but the next all calls will run without
# taking any time
