a= input("what is your name")
b=input("how much do you earn")
if int(b)==0:
    raise ZeroDivisionError("number is 0 so stopping the program")
if a.isnumeric():
    raise Exception ("Numbers are not allowed")
print(f'hello {a}')
# 1000 lines taking 1 hour

c = input("Enter your name")
try:
    print(a)
except Exception as e:
    if c=="harry":
        raise ValueError("Harry is not allowed ")

    print("Exception handled")