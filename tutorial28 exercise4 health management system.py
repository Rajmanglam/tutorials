# The task is to create a "Health Management System."
# Suppose you are a fitness trainer and nutritionist.
# You have to deal with three clients, i.e., (Harry, Rohan, Hammad).
# For each client, you have to design their exercise and diet plan.
# Instructions:
# Create a food log file for each client
# Create an exercise log file for each client.
# Ask the user whether they want to log or retrieve client data.
# Write a function that takes the user input of the client's name.
# After the client's name is entered,
# A message should display "What you want to log. Diet or Exercise"
# Use function
import datetime
def gettime():
    return datetime.datetime.now()


def harry():
    print('do you want to retrive data or log data \nL for loging and \n R for retriving')
    g = input()


    if g=='L':

        print('you want to do your work with exercise or food chart \nf for food \ne for exercise')
        a1 = input()


        if a1=='f':

            f1 = open('harryfoodlooging.txt', 'a')
            print('enter the food you ate')
            n2=input()
            f1.write(f"{n2} was ate at{str([str(gettime())])}\n")#here we have used + to add data
            print('your data has been stored thank you')


        elif a1=='e':

            f1 = open('harryexerciselooging.txt', 'a')
            print('enter the exercise you did\n')
            e1=input()
            f1.write(f"{e1} was ate at{str([str(gettime())])}\n")
            print('your exercise details have been stored thank you')


    elif g=='R':

        print('you want to retrive food data or exercise data')
        j1=input('enter 1 for food data \nenter 2 for exercise data\n')


        if j1=='1':

            l1=open('harryfoodlooging.txt')
            print(l1.readlines())


        elif j1=='2':

            l2=open('harryexerciselooging.txt')
            print(l2.readlines())
    return (' ')


def rohan():

    print('do you want to retrive data or log data \nL for loging and \n R for retriving')
    g = input()


    if g=='L':

        print('you want to do your work with exercise or food chart \nf for food \ne for exercise')
        a1 = input()


        if a1=='f':

            f1 = open('rohanfoodlooging.txt', 'a')
            print('enter the food you ate')
            n2=input()
            f1.write(f"{n2} was ate at{str([str(gettime())])}\n")#here we have used + to add data
            print('your data has been stored thank you')


        elif a1=='e':

            f1 = open('rohanexerciselooging.txt', 'a')
            print('enter the exercise you did')
            e1=input()
            f1.write(f"{e1} was ate at{str([str(gettime())])}\n")
            print('your exercise details have been stored thank you')


    elif g=='R':

        print('you want to retrive food data or exercise data')
        j1=input('enter 1 for food data \n enter 2 for exercise data')


        if j1=='1':

            l1=open('rohanfoodlooging.txt')
            print(l1.readlines())


        elif j1=='2':

            l2=open('rohanexerciselooging.txt')
            print(l2.readlines())
    return ('')

def hamid():

    print('do you want to retrive data or log data \nL for loging and \n R for retriving')
    g = input()


    if g=='L':

        print('you want to do your work with exercise or food chart \nf for food \ne for exercise')
        a1 = input()


        if a1=='f':

            f1 = open('hamidfoodlooging.txt', 'a')
            print('enter the food you ate')
            n2=input()
            f1.write(f"{n2} was ate at{str([str(gettime())])}\n")#here we have used + to add data
            print('your data has been stored thank you')


        elif a1=='e':

            f1 = open('hamidexerciselooging.txt', 'a')
            print('enter the exercise you did')
            e1=input()
            f1.write(f"{e1} was ate at{str([str(gettime())])}\n")
            print('your exercise details have been stored thank you')


    elif g=='R':

        print('you want to retrive food data or exercise data')
        j1=input('enter 1 for food data \n enter 2 for exercise data')


        if j1=='1':

            l1=open('hamidfoodlooging.txt')
            print(l1.readlines())


        elif j1=='2':

            l2=open('hamidexerciselooging.txt')
            print(l2.readlines())
    return (' ')

def nutrition():

    print('enter your name')
    k2=input()

    if k2=='harry':
        print(harry())

    elif k2=='rohan':
        print(rohan())

    elif k2=='hamid':
        print()
    return (' ')

print(nutrition())