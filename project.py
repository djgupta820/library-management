# Library Management Software
import sys
import os

class lib:
    is_name = ""
    bk_name = ""
    bk_code = ""
    is_date = ""
    re_date = ""
    op = 0

    def options(self):
        print("1.\tIssue New Book")
        print("2.\tReturn Book")
        print("3.\tAdd New Book")
        print("4.\tDelete Book")
        print("5.\tList All Books")
        print("6.\tExit")
        op = int(input("Enter your option here : "))
        return op

    def issueBook(self):
        print("\n Issue a New Book")
        is_name = input("Enter Name of Issuer : ")
        bk_name = input("Enter Book Name : ")
        bk_code = input("Enter Book Code : ")
        is_date = input("Enter Issue Date (DD\MM\YYYY) : ")
        re_date = input("Enter Return Date (DD\MM\YYYY) : ")

        info ="\n" + is_name + "," + bk_name + "," + str(bk_code) + "," + is_date + "," + re_date 
    
        try:
            f = open("issueBook.csv", "a")
        except:
            print("Error while opening database")

        f.write(info)
        f.close()
        print("Done")
        print("You need to return the book on ", re_date)

    def returnBook(self):
        print("\n Return Book")
        is_name = input("Enter Name of Issuer : ")
        bk_name = input("Enter Book Name : ")
        bk_code = input("Enter Book Code : ")
        is_date = input("Enter Issue Date (DD\MM\YYYY) : ")
        re_date = input("Enter Return Date (DD\MM\YYYY) : ")

        info = is_name + "," + bk_name + "," + str(bk_code) + "," + is_date + "," + re_date 
    
        try:
            f = open("issueBook.csv", "r")
            lines = f.readlines()
        except:
            print("error")
        f.close()

        with open("issueBook.csv", "w") as f:
            for line in lines:
                if line.strip("\n") != info:
                    f.write(line)
        print(lines)                  

    def addBook(self):
        print("\nAdd a New Book")
        bname = input("Enter Book Name : ")
        bcode = input("Enter Book Code : ")
        auth = input("Enter Author : ")
        pub = input("Enter Publisher : ")
        pyear = input("Enter Publish Year : ")
        info = "\n" + bname + "," + bcode + "," + auth + "," + pub + "," + pyear
        
        try:
            f = open("books.csv","a")
        except:
            print("Error")
        f.write(info)
        f.close()
        print("Book added successfully")

    def removeBook(self):
        print("\nRemove Book")
        bname = input("Enter Book Name : ")
        bcode = input("Enter Book Code : ")
        auth = input("Enter Author : ")
        pub = input("Enter Publisher : ")
        pyear = input("Enter Publish Year : ")
        info = bname + "," + bcode + "," + auth + "," + pub + "," + pyear
        
        try:
            f = open("books.csv", "r")
            lines = f.readlines()
        except:
            print("error")
        f.close()

        with open("books.csv", "w") as fl:
            for line in lines:
                if line.strip("\n") != info:
                    fl.write(line)
        fl.close()
        print("Book Removed Successfully")
        
    def allBooks(Self):
        print("\nAll Books in Library")
        with open("books.csv", "r") as f:
            data = f.readlines()
            print(data)
        f.close()

    def main(self):
        op = lib().options()
        if op == 1:
            lib().issueBook()
        elif op == 2:
            lib().returnBook()
        elif op == 3:
            lib().addBook()
        elif op == 4:
            lib().removeBook()
        elif op == 5:
            lib().allBooks()
        elif op == 6:
            sys.exit(0)
        else:
            print("Wrong Input")

obj = lib()
while True:
    obj.main()
