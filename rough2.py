class worker:
    leave_of_year = 9
    pay_scale = 63

    # @classmethod
    # def changel(cls,new_leaves,changeps):
    #     cls.leave_of_year = new_leaves
    #     cls.pay_scale = changeps

    def __init__(self,wname,wpost,whome):
        self.name = wname
        self.post = wpost
        self.home = whome

    @classmethod
    def changeinstance(cls,string):
        # rt = string.split("-")
        # return cls(rt[0],rt[1],rt[2])
        return cls(*string.split("-"))


gaurav = worker("rajput ji ","manager","kalyanpur")
vipin = worker.changeinstance("suar-hod-bijnor")

print(gaurav.name)
print(vipin.name)


