try:
    f = open("doesnotexist.txt")
    #here the compiler will try to open a file named doesnotexist.txt in a variable f
    #if this execution can't be done then it will go to except section and print the error
    #and will take it as a variable and print the error as that variable
except Exception as e:
    print(e)
    #now as the file doesnotexist.txt does not exist in the harddisk then it will print the
    #error
    #[Errno 2] No such file or directory: 'does not exist.txt'
    #by storing in a variable e as we have defined above
print("this is important stuff")

#NOW LET US  LEARN TO USE finally AND else IN TRY EXCEPT

#now if we want in the above code suppose we have opened a file as f2 and we want either try will run
#or except  will run the file f2 closes then we will use finally like this
f2=open("log.txt")
try:
    f = open("doesnotexist.txt")
except Exception as e:
    print(e)
finally:
    print('this will run anyway')
    f2.close()
    #here this finally will run no matter whatever try or except will run

#now let's think that we want to do like that if except will not run then a else will run along with
#try let's just see the practical

f2=open("log.txt")
try:
    f = open("doesnotexist.txt")
except Exception as e:
    print(e)
else:
    print("this will run only if except will not run")
finally:
    print('this will run anyway')
    f2.close()

#here except will run so else will not run but suppose something like this
f2=open("log.txt")
try:
    f = open("log.txt")
except Exception as e:
    print(e)
else:
    print("this will run only if except will not run")
    #here this else will run because log file exist
finally:
    print('this will run anyway')
    f.close()
    f2.close()
#NOTE : we can add multiple except statements