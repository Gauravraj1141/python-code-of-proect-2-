# class employee:
#     pay_scale = 5
#     def __init__(self,ename,eplace):
#         self.name = ename
#         self.game = eplace
#
#     def skills(self):
#         return f"his name {self.name}  and he  is from {self.game}"
#
# class player:
#     pay_scale = 6
#     def skills(self):
#         return f"his name {self.name}and he know {self.game}"
#     def __init__(self,name,game):
#         self.name = name
#         self.game = game
#
# #ye hamari 2 parent class h in dono se ye child class le skti h attributes ko
#
# class starprogrammer(player,employee): # or agr ham in dono ko aage piche krde to jo phle hoga child class usi ka data phle legi jo parent class phle likhi ye usi ka attributes lega
#     # pay_scale = 9
#     pass
# # gaurav = employee("Gaurav Rajput ","up")
# # print(gaurav.knowledge())
# rdx = player("rdx","badminton")
# ravi = starprogrammer("ravi ","football")
# print(ravi.skills()) # ye uske according attributes ko jse upper class hogi phle player h to player vali k attributes ko lega jo phle hogi usi ke method ko lega
#
# print(ravi.pay_scale)
# # print(gaurav.pay_scale)
# print(rdx.pay_scale)
#
class Base1:
    def func1(self):
        print("this is Base1 class")


class Base2:
    def func2(self):
        print("this is Base2 class")


class Child(Base1, Base2):
    def func3(self):
        print("this is Base3 class")


obj = Child()
obj.func1()
obj.func2()
obj.func3()