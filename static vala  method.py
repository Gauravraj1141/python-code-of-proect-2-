class employeee:
    @staticmethod # static decorator h ye
    def statc(str):
        print("it is a static method we can use it withour passed cls and self in "
              "this function we can pass in this which we want it is more efficient for us  " + str)
        return "it is very easy to use"
    def __init__(self,ename,ework):
        self.name= ename
        self.work = ework

gaurav = employeee("gaurav","developer")
ravi = employeee("ravi","devops")

print(gaurav.name,gaurav.work)
gaurav.statc("ram")
#iske sath sath me ham ise bhi use kr skte h
