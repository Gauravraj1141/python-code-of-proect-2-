# public - all can seen and access this mean all class can be access this
# protected  -  (ye h only hamare home memeber hi dekh skte h )ise only parent class se drived class hi access kr skti h koi other class ni kr skti yani apna khoon jisme hoga voi access kr skta h
# private = (ye only ham hi dekh skte h ) hamare child class bhi nhi access kr skte h ise
class manager :
    public =  1
    _protected= 4 # protected variable ko single underscore k sath likhte h or ise child class me use kr skte h
    __private = 7 # private variable ko double underscore k sath likhte h ise only base class me hi use kr skte h

    def __init__(self,ename,ework):
        self.name= ename
        self.__work = ework
    def printdetail(self):
        return f"it is name{self.name} and it is work{self.__work}"

class employeee(manager):
    pass

dinesh = manager("suresh","hr")
mayank = employeee("mayank","emply")
print(mayank._manager__private)# python name mangling kr deta h isliye hame iska name ye dena pda ye islie krta h jisse ham ise assani se call na kr ske
print(mayank._manager__work) # hame private vairable ko call krne k liye mangling name ko use krna pdega tabhi ham use call kr skte h

