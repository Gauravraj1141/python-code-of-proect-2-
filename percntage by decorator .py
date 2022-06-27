def func1(ram):
    def func2():
        print("please enter your board marks  ".upper())
        ram()

        print("it is the result of you board")
    return func2()
@func1

def func3():
    a = int(input("enter your obtained marks =  "))
    b = int(input("enter the maximum marks = "))
    c = a/b*100
    print("it is your percentage  = ".upper(),c ,"%")