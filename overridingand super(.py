class A:
    clsvar1 = "i am in class a "
    def __init__(self):
        self.clsvar1= " it is class a instance  variable "
        self.var2 =  " it is class a variable 2 "
        self.special = "it is special and print this necessary "
class B(A):


    clsvar1 = "it is  classs variable of class b "

    def __init__(self):
        pass
        super().__init__()
        self.clsvar1 = "it is instance variable of cls b "
        super().__init__()

ram = B()
shyam = A()
print(shyam.clsvar1)





# class A:
#     clsvar1 = "i am class variable in class a "
#     def __init__(self):
#         self.var1 = "it is instance variable in class a"
#         # self.clsvar1 =  " it is instance variable and overrideen variable in class a "
# class B(A):
#     clsvar1  = "i am  class variable of class b " # ye override hogya class a ke class variable se
#     pass
# a = A()
# b = B()
# print(b.clsvar1) # jab hmne b.clsvar1 print kiya to phle to  class b
# me instance variable check krega fir iski parent class me instance variable check krega or
# is class a me mil gya to calss a ka instance variable print kr dega ni to fir apni class ka
# class variable check krega or ni mila to uske bad apni parent class ka class variable check krega



