# f = open("gaurav.txt") #ye file to h to isme koi error nhi ayega
# try:
#     f = open("gaurav.txt")
#     # ye file nhi h to isme error ayega or try except ki vjh se ye age vala print krega
# except Exception as f:
#
#     print(f)
#     # print("it is important")
#     # f2 = open("kdkd.txt")
# else: #ye else tab chlega agr try me jo file open hui vo error na de to yha except na chlkar ye else chlega
#     print("is except is not run so else will be print ")
# finally: # or ye finally isliye h k exception k bad ye jarur run ho ga kuch ho ya na ho ye jarur krna h jo jyada important h use run krna h
#     print("it is very important")
#     f.close()
# #finally ka use ham cleanup ke liye krte h jse bhot sari files khol rkhi h to unhe sbhi ko samet skte h

# def division(a,b):
#     try:
#         c = (f"{a}/{b} is {a/b}")
#         print(c)
#     except ZeroDivisionError as e:
#         print(e)
#     else:
#         print("there is no exception in this code")
# division(10,5)

def numbers(a,b):
    try:
        print (a ** b)
    except ZeroDivisionError:
        print(" in this try have a error")
    except EOFError:
        print("this case is eof error")
    except IOError:
        print("this case is Io error")
    else:
        print("in this no error")
    finally:
        print("it is important link")


numbers(155,54)


