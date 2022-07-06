#isme hm instance variable se hi class variable ki bhi value chnage kr skte h class method ki help se jo ki ek decorator h

class Developer:
    pay_scale = 2
    pf = 67
    day_leave = 99
    def __init__(self,dname,drole):
           self.name = dname
           self.role = drole
    @classmethod  # ye classmethod decorator ka use kiya h
    def change_pay_scale(cls,newpayscale ,new_pf, new_leaves): #ye yha cls khud ajati h isliye puri class ki valiue change hojati h
        cls.pay_scale = newpayscale # or hmne ye class variable ko new instance k equal rkh dia
        cls.pf = new_pf
        cls.day_leave = new_leaves
rdx = Developer("rdx","trader")
gaurav = Developer("Rajput gr","developer")
gaurav.change_pay_scale(55,89,23) # or yha par is function ka use krke instance variable ki help se hi puri class ki value ko change kr dia
print(gaurav.pf)
print(gaurav.pay_scale)
print(rdx.pay_scale)
print(rdx.day_leave)
print(gaurav.day_leave)
