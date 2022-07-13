class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def log(self):
        return f"this is employee {self.fname},{self.lname}"
    @property
    def email(self):
        if self.fname == None  or self.lname == None:
            return "it is no any emailid please use setter to manage this again "

        return f"{self.fname}{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        print("setting now.....")
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf = Employee("garuav","rajput")
print(type(skillf)) # this type <class '__main__.Employee'> it is class
print(id(skillf)) # it is id and we can know all attributes and values id .
a = "it is not a ball"
print(id(a)) #so all attributes id will be different
print(dir(skillf)) # it is dir we can know by this all the function's features that what we can do this class fuction and what is in this class all details about the function we know by this "dir"

import  inspect

print(inspect.getmembers(skillf)) #it shows the class and its type. It is used to inspect live classes.
print(inspect.isclass(Employee))#The isclass() method returns True if that object is a class or false otherwise so we run Employee , and it is class so it