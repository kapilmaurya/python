class Library:
    def __init__(self):
        self.lend={}
        self.list_of_books=self.readfile()
        print(type(self.list_of_books))
        print(self.list_of_books)
    
    def displayBooks(self):
        self.list_of_books=self.readfile().split("\n")
        for n in self.list_of_books:
            print(n)
    
    def lendBook(self):
        self.bname=input("enter the book name ")
        if self.bname in self.lend:
            print(f"sorry the {self.bname} book is lend by {self.lend[self.bname]}")
        else:
            self.lname=input("lender's name ")
            self.lend[self.bname]=self.lname

    def returnBook(self):
        self.bname=input("Book name which will you return ")
        self.lend.pop(self.bname)
        print("Thank you for returning the book")

    def addBook(self):
        self.bname=input("Enter the book name which will you add to library_____")
        self.pname=input("Enter your name_____")
        self.list_of_books=f"\n{self.bname}"
        self.addNewBook="\n{}".format({self.bname:self.pname})
        self.myFile()
        print("your book is added in library........")

    def myFile(self):
        with open("lib.txt","a") as fp:
            fp.write(f"{self.list_of_books}")
        with open("bookGiver.txt","a") as f:
            f.write(f"{self.addNewBook}")
    def readfile(self):
        with open("lib.txt","r") as fr:
            return fr.read()


if __name__ == "__main__":
    kapil=Library()
    #kapil.displayBook()
    while True:
        print("press q for quit \npress 1 for lend the book \npress 2 for return book \npress 3 for display the book\npress 4 for add new book")
        opt=input()
        if opt=="q":
            break
        if opt=="1":
            print("welcome")
            kapil.lendBook()
        
        elif opt=="2":
            kapil.returnBook()
        
        elif opt=="3":
            kapil.displayBooks()
        
        elif opt=="4":
            kapil.addBook()

        x=input("press c for continue")


# kapil.addBook()
# kapil.pgive()