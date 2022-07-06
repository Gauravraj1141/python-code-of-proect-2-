class A:
    def met(self):
        print("it is the instance variable of class a")
class B(A):
    def met(self):
        print("it is the instance variable of class b")
class C(A):
    def met(self):
        print("it is the instance variable of class c")
class D(B,C):
    def met(self):
        print("it is the instance variable of class d")
a = A()
b = B()
c = C()
d = D()
d.met() # to isme ye d ka print krega python ke andr diamond problem nhi aati h multiple inheritence me or languange me ajati h isliye multiple inheritence ko or language me avoid krte h multilevel or single inheritence ko use krte h sabhi language me
