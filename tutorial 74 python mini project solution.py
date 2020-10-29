import datetime
def gettime():
    return datetime.datetime.now()

class library():
    def __init__(self,lob,ln):
        self.list_of_books = lob
        self.library_name = ln
        self.len_books = {}
        b = open(f"{self.library_name}.txt", 'w')
        for index, item in enumerate(self.list_of_books):
                b.write(f"*{item}\n")
        b.close()

    def display(self):
        for index, item in enumerate(self.list_of_books):
            print(f'{index}.>{item} \n')
        j=open(f"{self.list_of_books} logs.txt",'w')
        j.write(f'this file was once displayed at {str([str(gettime())])}')
        return ' '

    def lendbook(self):
        o=input('enter the book you want')
        k = input('enter your name')
        i=0
        if o in self.list_of_books:
            print(f'the book {o} was taken by {k}\n')
            j = open(f"{self.library_name} logs.txt", 'a')
            j.write(f'the book {o} was taken by {k}  at {str([str(gettime())])}\n')
            j.close()
            o1=self.list_of_books
            o1.remove(o)
        else:
            print("sorry we don't have this book")
            j = open(f"{self.library_name} logs.txt", 'a')
            j.write(f'the book {o} was requested by {k}  at {str([str(gettime())])}\n')
            j.close()
        return ' '

    def return_book(self):
        l1=input('enter the book you want to return')
        k=input('enter your name')
        k1=self.list_of_books
        k1.append(l1)
        j = open(f"{self.library_name} logs.txt", 'a')
        j.write(f'the book {l1} was returned by {k}  at {str([str(gettime())])}\n')
        j.close()
        print('thanks for returning the book')
        return '  '

    def addbook(self):
        k=input('enter the book you want to add \n')
        b= open(f"{self.library_name}.txt", 'a')
        i=1
        for index in range(len(self.list_of_books), len(self.list_of_books) + i):
                if k in self.list_of_books:
                    pass
                    return ' '
                else:
                    self.list_of_books.append(k)
                    b.write(f'*{k}\n')
                    j = open(f"{self.library_name} logs.txt", 'a')
                    j.write(f'the book {k} was added in the library  at {str([str(gettime())])}\n')
                    j.close()
                    return ' '
        b.close()
        return ' '



def main():
    k=library(['alice in wonderland','twenty thousand leagues under the sea','raj,'
           'rodger','meluha','laos','hamlet'],'raj')
    print(f'welcome to {k.library_name}')
    print(f'now you have four options you can do in the library')
    k33=False
    while k33 is not True:
        k4=input("enter \n'q' to quit from library\n'a' to add book in library\n"
                 "'l' to lend book from library \n'r'to return a taken book to library\n"
                 "'d' to display the books in library\n")
        if k4=='q':
            print('after you quit from this library your all data will be lost so please save your data')
            l3=input('press any key to exit now')
            if l3=='':
                k33=True
        elif k4=='d':
            k.display()
        elif k4=='a':
            k.addbook()
        elif k4=='l':
            k.lendbook()
        elif k4 == 'r':
            k.return_book()

if __name__=='__main__':
    main()


