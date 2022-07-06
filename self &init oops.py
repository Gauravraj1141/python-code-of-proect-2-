class Employee:
    no_of_leaves = 8

    # yha par ye self khud likh k aya isliye yani jab m ise kisi bhi object ke sath
    # use krunga to uska name isme khud ajayega yani ye jiske sath use hoga use apne andr lelega
#     def printdetail(self):
#         return  f"the  name is  {self.name} . and his/her  salary is {self.salary},and company is {self.company},and it is {self.role}"
#
# gaurav = Employee()
# rdx = Employee()
#
# gaurav.name = "Gaurav"
# gaurav.salary = 5654656556
# gaurav.company = "google"
# gaurav.pf = 9888
# gaurav.role = "software engineer"
#
# rdx.name = "RDX"
# rdx.salary = 5645648484
# rdx.company = "microsoft"
# rdx.pf = 665445
# rdx.role  = "trador"
#
# print(gaurav.printdetail()) # yha par is function ke andr as an argument gaurav chala jayega jisee gaurav ki detail print hogi upper self me jake or uske bad vo vha se lelenge
# print(rdx.printdetail()) # iski help se ham kitne bhi object ko asani se le skte h

class Employee:
    no_of_leaves = 8

    # ye self is gaurav nam ke object ko lelega or iske andr ke data ko kram se inme dal dega
    def __init__(self,aname,asalary,acompany,arole):
        self.name = aname # ye a isliye lgaya jisse confusion na ho
        self.salary = asalary
        self.company = acompany
        self.role = arole



gaurav = Employee("rdx",59545646,"microsoft","trador")
print(gaurav.role)
print(gaurav.no_of_leaves)