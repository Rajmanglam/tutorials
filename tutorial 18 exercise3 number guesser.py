#ou have to build a "Number Guessing Game,"# in which a winning number is set to some
# integer value.# The Program should take input from the user, and if the
# entered number is less than the winning number,
# a message should display that the number is smaller and vice versa.
# no. of guesses=9 winning number=18
n=18
attempts=0
while(attempts<=9):
    print('enter a number')
    k=int(input())
    if k==n:
        print("you won the game")
        attempts=attempts+1
        print("the player finished the game in",attempts,"attempts")
        break
    else:
        if k<n:
            print("the number you entered is smaller than winning number")
            attempts = attempts + 1
            if attempts<=9:print("number of attempts left is",9-attempts)
            continue
        else:
            print("the number you entered is greater than winning number")
            attempts = attempts + 1
            if attempts<=9:print("number of attempts left is", 9 - attempts)
            continue
if attempts>9:
    print("you used all your attempts")
    print("game over")