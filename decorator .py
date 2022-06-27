# def fun1(ram):
#     return ram
#
# fun2 = fun1  # hmne is fun ki value fun2 me dedi ab agr hmne fun1 ko delete bhi kiya to koi frk nhi pdega fun2 me value phle hi copy ho chuki h
# del fun1
#
# print(fun2("ram ji ki sena chali "))
#
# def function(num):
#         if num == 0:
#             return print  #hm function se built in function ko bhi call kr skte h
#         elif num == 1:
#             return sum
# a = function(0)
# print(a)
#
#
# def executor(func):
#     func("this is a executor's function we can call function inside the function")
# executor(print) #ham function ke andr function ko call kr skte h or usme built in funciton jse print ka use bhi kr skte h


# DECORATOR KA MATLB H FUNCTION KE ANDR FUNCTION KO CALL KRNA
# def dec1(func1):
#     def dec2():
#         print("executing now")
#         func1() #or iske andr  who is gaurav is value store hogyi ye use derha h
#         print("executed")
#     return dec2 # jab ye return kiya tabhi to ye function chala kuki dec2 bhi dec1 ke andr h na to dec1 jab chlega to ise bhi chlna hoga to return se pura function  cla jisse iske andr ke print bhi chala



#
# def who_is_gaurav():
#     print("gaurav is a good boy")
# who_is_gaurav = dec1(who_is_gaurav)
# who_is_gaurav() #or hmne ise execute kr dia or ise dec1 ke andr dal dia ab upper vale function ke bich me ayega


# def gr(dalla):
#     def j():
#         print("hhh")
#         dalla()
#     return j
#
# def d():
#     print("it is real")
# d = gr(d)
#
# d()


# def ff(text):
#     return text.upper()
# def xx(text):
#     return text.lower()
# def gr(func):
#     fx = func("this is a function that contain in another function")
#     print(fx)
# gr(ff)
# gr(xx)
#


# def cp(cap):
#     def gold(gld):
#         return cap+gld
#     return gold
#
# add = cp(10)
# print(add(12))


# #
# def cp(cap):
#     def gold():
#         print("it is a first fun")
#         cap()
#         print("it is second")
#
#     return gold
# @cp # ise hi ham decorator khte h
# def gn():
#
#     print("it is pk")
#
# gn()

# def function1():
#     print("Subscribe now")
#
# func2 = function1
# del function1
# func2()

# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
#
# a = funcret(1)
# print(a)

# def executor(func):
#     func("this")
# #
# #
# # executor(print)
#
# def dec1(func1):
#     def nowexec():
#         print("Executing now")
#         func1()
#         print("Executed")
#
#     return nowexec
#
#
# @dec1
# def who_is_harry():
#     print("Harry is a good boy")
#
#
# # who_is_harry = dec1(who_is_harry) # ase na krne ke bajay ham decorator ka use kr lete h
#
# who_is_harry()


def fun(put):
    def fun2():
        print("it is first value")
        put()
        print("it is second value")
    return fun2

@fun
def let():
    print("gjgjgyugug")
let()

















