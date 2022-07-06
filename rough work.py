# class Engineers:
#     pay_scale = 12
#     pf = 66
#     rd = 63
#     def dl(self):
#         return f"name is and ctc {self.pay_scale}/year , and gender is {self.gender},life status {self.status},and all pf is  {self.pf},and it is road load {self.rd}"
#     @classmethod
#     def change_pscale(cls , npscale,nwpf, nrd):
#     @classmethod
#     def str(cls,strings):
#         return cls(*strings.split("-"))
#         cls.pay_scale = npscale
#         cls.pf = nwpf
#         cls.rd = nrd
#     def __init__(self,epname,epgender,epstatus,eprole,pay_scale):
#         self.name = epname
#         self.gender = epgender
#         self.status = epstatus
#         self.role = eprole
#         self.pay_scale = pay_scale
#     @classmethod
#     def chgne(cls):
#
#
#
#
#     # @classmethod
#     # def change_attribte(cls):
#     #     return cls()
# rajput = Engineers("gaurav","male","unmarried","developer",252)
# print(rajput.name)
# print(rajput.pay_scale)
# print(Engineers.pay_scale)
# # rdx = Engineers()
# # aatif = Engineers()
# # rajput.change_pscale(663,89,5)
# # rajput.name = "gaurav"
# # rajput.gender = "male"
# # rajput.status = "unmarried"
#
# #
# # rdx.name  = "sachin"
# # rdx.gender  = "male"
# #
# # rdx.status= "unmarried"
# # aatif.name= "Aatif"
# # aatif.status= "unmarried"
# # aatif.gender= "male"
# # print(rajput.dl())
# # print(rdx.dl())
# # print(aatif.dl())




















class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


class Programmer(Employee):
    no_of_holiday = 56
    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages


    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"



harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Programmer("Shubham", 555, "Programmer", ["python"])
karan = Programmer("Karan", 777, "Programmer", ["python", "Cpp"])
print(karan.no_of_holiday)
print(harry.printdetails())
print(shubham.printprog())

