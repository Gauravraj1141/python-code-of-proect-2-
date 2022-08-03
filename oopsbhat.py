class Student: # ham jab bhi class bnate h uska nam capital se suru krna chiye 
    pass

gaurav = student()# hmne ye do objects bnaaye h upper vali class
rdx = student()

gaurav.name = "Gaurav"
gaurav.std = 3
gaurav.section = 5
rdx.section = 9
rdx.subject = ["physics","chemistry","bio"]

print(gaurav.name,gaurav.std, rdx.subject)
