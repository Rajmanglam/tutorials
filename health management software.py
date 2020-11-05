import datetime
def gettime():
    return datetime.datetime.now()

def harry():
    k2 = input('enter your name')
    print('do you want to retrive data or log data \nL for loging and \n R for retriving')
    g = input()


    if g=='L':

        print('you want to do your work with exercise or food chart \nf for food \ne for exercise')
        a1 = input()


        if a1=='f':

            f1 = open(f'{k2}food looging.txt', 'a')
            print('enter the food you ate')
            n2=input()
            f1.write(f"{n2} was ate at{str([str(gettime())])}\n")#here we have used + to add data
            print('your data has been stored thank you')


        elif a1=='e':

            f1 = open(f'{k2}exercise looging.txt', 'a')
            print('enter the exercise you did\n')
            e1=input()
            f1.write(f"{e1} was done at{str([str(gettime())])}\n")
            print('your exercise details have been stored thank you')


    elif g=='R':

        print('you want to retrive food data or exercise data')
        j1=input('enter 1 for food data \nenter 2 for exercise data\n')


        if j1=='1':

            l1=open(f'{k2}food looigng.txt')
            print(l1.readlines())


        elif j1=='2':
            l2=open(f'{k2}exercise looging.txt')
            print(l2.readlines())
    l9=input('do want do again')
    if l9=='yes':
        harry()
    return (' ')

print(harry())