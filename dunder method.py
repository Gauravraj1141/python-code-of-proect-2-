class A:
    def __init__(self,salary,breakfast):
        self.salary = salary
        self.breakfast = breakfast

#     def __add__(self, other):
#         return self.salary + other.salary
#     def __gt__(self, other): #for greater than
#         return self.breakfast>other.breakfast
#     def __eq__(self, other): #for equal to
#         return self.salary == other.salary
#     def __truediv__(self, other):#ye divide krne k liye hota h
#         return self.salary/other.salary
# aman = A(2400,3000)
# gaurav = A(1200,6000)
# if aman.breakfast>gaurav.breakfast:
#     print("aman's spend more than gaurav")
# elif gaurav.breakfast>aman.breakfast:
#     print("Gaurav spend more than aman")
# else:
#     print("both are equal")
#
# print( aman.salary+gaurav.salary)
#
# if aman.salary==gaurav.salary:
#     print("both are earn equal")
# else:
#     print("both are not equal")
# print(aman.salary/gaurav.salary)



class A:
    def __init__(self,salary,cost):
        self.salary = salary
        self.cost = cost

    def printdetails(self):
        return f"name is {self.salary} and  his kharcha is {self.cost}"
    def __repr__(self):
        return f"employe{self.salary},{self.cost}"
    def __str__(self):
        return f"it is str's attributes {self.salary},{self.cost}"
emp = A(4555,5558)
print(repr(emp)) # jab bhi ham yha object ko print krenge to repr jo return krega vo print hoga or agr uski jgh str hua to str jo return krega vo print hoga
# agr str nhi hoga to repr me jo hoga vo print hoga ase krke