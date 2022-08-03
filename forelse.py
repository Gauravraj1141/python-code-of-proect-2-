# today we will talk about how to work else with for loop when we search any item in list and when the item did't find so else print "this item is not in this list " otherwise item is in this list so else will not be print

items = [ "gaurav","rajan ","ram","megha"]
for item in items:
    if item == "gaurav":
        print("this item is in this list")
        break
else:

    print("this item is not in this list ")




# for i in range(1,9,2):
#     print(i)
# else:
#     print("loop is executed sucessfully ")


def even_no(l):
    for i in l:
        if i%2==0:
            print("list contain even number ")
            break
        else:
            print("list does not contain any even number")
print("for list 1")
even_no([1,2])
print("for list 2")
even_no([1,3,5,9])
