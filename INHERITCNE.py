class father:
    no_of_leave = 12
    def __init__(self,nme,qfcn,work):
        self.name = nme
        self.work = work
        self.qualification = qfcn
    @classmethod
    def changelve(cls,change):
        cls.no_of_leave = change

    def printdetail(self):
        return  f"the  name is  {self.name} and his/her  salary is {self.work},and company is {self.qualification} "
class child(father): # ab is child class me father class ka koi bhi function call kr skte h ham
    no_of_leave = 4

    def printdetail(self):
      return f"child vala name is {self.name} and work {self.work},and padha likha kitna {self.qualification} and {self.background}"

    def __init__(self,pname,pwork,pquali,backgroud):
        self.name = pname
        self.work = pwork
        self.qualification = pquali
        self.background = backgroud

    @classmethod
    def changelve(cls, change):
        cls.no_of_leave = change # jab hmne ye leave yha change kri to child vale me change hui or upper kri to father vale objects k liye change hui


raju = child("rajput","bsc","smr","white")
raju.changelve(777)
print(raju.no_of_leave)
gaurav = father("rajput","bsc","smr")
rdx = father("jaat","bdx","smrr")
gaurav.changelve(55)
print(rdx.no_of_leave,"it is father side")

ravi = child("rajputana ","mca","smamert ","white")
print(ravi.no_of_leave,"ye child ki h ")

print(gaurav.printdetail())
print(ravi.printdetail()) # ye sbse phle apni class me search krta h fir parent class me jata h agr ise child
# class me printdetail nhi mila fir father class ka printdetail me attributes call honge






