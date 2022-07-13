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

gr = Employee("gaurav ","rajput")
gr.fname = "bhatti"
print(gr.email)
gr.email = "name.doon@gmail.com"
del gr.email # to is del function ko jab ham chalate h to ye upper ek deleter dhudhta h jo hmne bnaya h usi k according ye chlta h
print(gr.email)
gr.email = "rajput.doon@gmail.com"
print(gr.email)