# *args and **kwargs function

def funargs(normal,*args,**kwargs): # ham yha par normal argument bhi de skte h par use ham args or
    # kwargs se phle hi de skte h inke bad ham koi arguments nhi de skte h args and kwargs optional hote h inme value do ya mat do ye error nhi dete
    print(normal)
    for item in args:
        print(item)
    print("we can add in kwargs function only dictonary value ")
    for key ,value in kwargs.items():
        print(f"{key} bnega {value}")

var2 = ["gaurav","ram","rohan","priti","bharat","pyush","ram"]
var= {"rdx":"programmer ","gaurav":"developer","aatif ":"recruiter"}
norm = "it is a normal argument we can only give it before the args and kwargs "
funargs(norm, *var,**var2) #isme var ki value store hoke uper function me chali gyi or vo usme ek tuple me print hoti h hamesha or
# yha bhi hame star lgana pdega

def fun(**kwargsgr): # yw kwargs fun h isme only dictionary hi le skte h or inka name bhi change kr skte h
    for key , value in kwargsgr.items():
        print(f"{key} it is a value{value}")
v = {"ram":"ksks","ksk":"fksks"}
fun(**v)