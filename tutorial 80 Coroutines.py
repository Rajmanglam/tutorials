# Coroutines are mostly used in cases of time-consuming programs,
# such as tasks related to machine learning or deep learning algorithms
# or in cases where the program has to read a file containing a large number
# of data. In such situations, we do not want the program to read the file or
# data, again and again, so we use coroutines to make the program more efficient
# and faster. Coroutines run endlessly in a program because they use a while
# loop with a true or 1 condition so it may run until infinite time.
import time
def searcher():
    #some task that will take 4 seconds
    book = "This is a book on harry and code with harry and good"
    time.sleep(4)
    #here this function when once ran it will keep the 4seconds task already set then it will start execution from
    #while True
    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")
    #here this searcher is a is not a function it is instead a coroutine
#we can't run a coroutine in a normal way  we have to to like this
search = searcher()#this will open searcher coroutine
print("search started")
next(search)
print("Next method run")
search.send("harry")#In this search.send we will give the word which we want to search
print("Next method run")
search.send("raj")
print("Next method run")
search.send("harry and")
print("Next method run")
search.send("code")
search.close()#here we will close the coroutine to release our resources


#QUIZ : CREATE A COROUTINE THAT WILL CHECK 15 ALPHABET STRING
def youtubers():
    time.sleep(2)
    book = "ram shyam hera raju kalam amit ajay ashish hero bruce wayne kalos ash misty sadam"
    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")
yt=youtubers()
next(yt)
yt.send(input())
yt.send(input())
yt.send(input())