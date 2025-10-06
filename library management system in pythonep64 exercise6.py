class library:
    no_of_books=4
    books=["100 ways to think","a to z","one million digits of pi","where is waldo"]

a=int(input('press 0 to print list of books: \npress 1 to add a book in library: \npress 2 to delete a book in library: \npress 3 to exit library:'))

def addingbooks(self,a):
    newbook=list(input("enter the name of book you want to add:"))
    books.append(newbook)
    no_of_books=no_of_books+1
    print("no of books is:",no_of_books)
    print("new list of books available is:",books)



def removingbooks(self,a):
    newbook=list(input("enter the name of book you want to remove:"))
    books.append(newbook)
    no_of_books=no_of_books-1
    print("no of books is:",no_of_books)
    print("new list of books available is:",books)

def printinglistofbooks(self,a):
    print("list of available books is:",books)
    print("no of books is:",no_of_books)

if(a==0):
    printinglistofbooks(a)
elif(a==1):
    addingbooks(a)
elif(a==2):
    removingbooks(a)
elif(a==3):
    print("thanks for accessing the library")
else:
    print("invalid input")
              
