def searcher():
    import time
    book = "rajputo ka itihas nhi yug tha and usme rdx,gaurav,atif samil the "

    time.sleep(3)
    #ye only yha ek hi bar 3 second lega yni hmne 3 second isliye li jse koi bda data lenge to use read krne me kuch time lagega isliye hmne uske badle me ye 3 second ka time dia or uske bad ye funciton dobara run nhi hoga fir ham is book me kitna bhi search kr skte h

    while True:
        text = (yield ) #is yield me hmne jo send kiya niche vo ajayega search.send me jo send kiya h vo is yield me ayega
        if text in book:
            print(f"your name {text} is in this book")
        else:
            print(f"your name {text} is not in this book")
search = searcher()
next(search) # ye next ise upper yield me bhejne me help krta h
print("it is start to search")
search.send("sachin")
search.send("gaurav")
search.send("aatif")
search.send("kp")




#excercise by me


def search_book():
    import time
    with open("gaurav.txt", "r+") as f:
        book = f.read()

    time.sleep(2)
    while True:
        value = (yield )
        if value in book:
            print(f" \t\t\t\t\t\t\t'{value}'   is in this book")
        else :
            print(f"sorry this value :  '{ value}'  is not in this book ")
ip = search_book()
print("please wait your book is reading now......".upper())
next(ip)
print("\t\t\t\t\t\t\tyour book reading sucessfully, now you can search anything in this .".upper())
while True:

    v = int(input(" Press : 1   Continue to search keyword in this book  \n Press : 2 for exit this  program \n : "))
    if v == 1 :
        ip.send(input("Enter value that you want to search in this boook : "))
    elif v == 2 :
        ip.close()
        print(" \t\t\t\t\t\t\tcoroutine is closed sucessfully ".upper())
        break
    else:
        print("plase enter the valid input \n")




#revision

def search():
    import time
    with open("gaurav.txt","r+") as f:
        a = f.read()
        time.sleep(2)
    while True:
        value = (yield )
        if value in a:
            print(f"this '{value }' is in this book")
        else:
            print(f"this '{value}' is not in this book")
ip = search()
next(ip)
ip.send("earth")
