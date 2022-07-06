# class alternative me ham jab alg alg attributes ko ek hi string me dal dete h to string split krke use
class Developer:
    pay_scale = 2

    def __init__(self,dname,drole):
           self.name = dname
           self.role = drole

    @classmethod  # hmne ise yha ek altrenative constructor ki trh use kiya h
    def from_dash(cls,str):
        # far = str.split("-")
        # return cls(far[0],far[1])
        return cls(*str.split("-"))
rdx = Developer("Rdx","trader")
gaurav = Developer("Gaurav","developer")
aatif = Developer.from_dash("Aatif-recuriter") # yha ham use function me is data ko denge
print(aatif.name,aatif.role)
print(rdx.name,rdx.role)
print(gaurav.name,gaurav.role)



