print("Welcome to the Library")
class Library:
    def __init__(self,book,library_name):
        self.list_of_books = book
        self.library_name = library_name
        self.lend_records = {}
        self.return_records = {}

    def display_books(self):
        print(self.list_of_books)
    def lend_books(self):
        p_name = input("enter your name =  ")
        b_name = input("enter book name = ")
        if b_name in self.list_of_books:
            self.list_of_books.remove(b_name)
            self.lend_records[p_name] = b_name
            print("you book has been sucessfully lended ")
            print(self.lend_records)
        elif b_name not in self.list_of_books:
            self.lend_records.get(p_name) #ye hmmne already taken k liye liya h list of lenders
            print(f"this book is already taken by {self.lend_records}")
        else:
            print("this is not a valid input please try again")

    def add_books(self):
        b_name = input("enter book name ")
        self.list_of_books.append(b_name)
        print("Your Book Added Sucessfully  in Library")

    def return_books(self):
        p_name = input("enter your name =  ")
        b_name = input("enter book name = ")

        self.list_of_books.append(b_name)
        self.return_records[p_name] = b_name
        print(self.return_records)
        print("your book has been sucessfully returned")


    def lend_record(self):
        print(self.lend_records)

    def return_record(self):
        print(self.return_records)

book_list = ["rich dad poor dad","stock market","good life","python","c"]

gr = Library(book_list,"Gaurav Rajput")
if __name__ == '__main__':
    def open_library():
        while True:
            ip = input("\n\n put 'd' for Display All books \t put 'l' for Lend books from library \t put 'a' to add books in libraray  \t put 'r' for  return books in libraray \t put 'Q' to exit from libraray \t put 'lr' for lend record \tput 'rr' for return record \n = ")
            if ip == "l" or ip == "L":
                gr.lend_books()
            elif ip == "d" or ip == "D":
                gr.display_books()
            elif ip == "a" or ip == "A":
                gr.add_books()
            elif ip == "r" or ip == "R":
                gr.return_books()
            elif ip == "lr" or ip == "LR":
                gr.lend_record()
            elif ip == "rr" or ip == "RR":
                gr.return_record()

            elif ip == "Q" or ip == "q":

                break
        print("Thanks for using our Library")
    open_library()

