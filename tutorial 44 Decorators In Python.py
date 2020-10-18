def func1():
    print('subscribe now')

func2=func1 # here we have assigned values of func1 to func2
# and if we delete it like this
del func1
# then also func2 will print values of func1 becase it already had got the values and
# stored it
func2()

def funret(num):
    if num==0:
        return print
    elif num==1:
        return print

a=funret(0)
print(a)
#in this case it will also run

def executer(func):
    func('my name is raj')
executer(print)

# so we can give functions as an argument in a function or return it in a function

def dec1(func1):
    def exec():
        print('executing now')
        func1()
        print('executed')
    return exec

def whoisraj():
    print('raj is a good boy')
whoisraj=dec1(whoisraj)
whoisraj()
# this is called a decorator
# we can even use a decorator like this
@dec1
def whoisraj2():
    print('raj is a good boy')
whoisraj2()