class Employee:
    """it is a static or class variable it can not be change by any object or instace variable it is same for all the object's variable"""
    no_of_leaves = 8 #
    pass
gaurav = Employee()
rdx = Employee()

gaurav.salary = 5654656556
gaurav.company = "google"
gaurav.pf = 9888
gaurav.location = "software engineer"

rdx.salary = 5645648484
rdx.company = "microsoft"
rdx.pf = 665445
rdx.location  = "trador"
rdx.no_of_leaves = 9 # ye h instace variable jse hmne class variable ki value bs is rdx k liye hi change ki h or baki sbke liye same h
Employee.no_of_leaves  = 45  # or agr upper class variable ki change krdi to rdx ko chor k sbki change hogi

print(rdx.salary,gaurav.salary,gaurav.no_of_leaves,rdx.no_of_leaves,)
 # dict ki help se ham kisi bhi object ke sare attributes ko dekh skte h
print(rdx.__dict__) # to jab hmne rdx ka leave vala variable change kiya to iski dict me vo alg se add hoke arha h
print(gaurav.__dict__)
print(Employee.__dict__) #isme vo ata h jo sabhi employees k liye same hota h





