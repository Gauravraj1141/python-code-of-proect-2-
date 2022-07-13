"""
Iterable = __iter__()  or __getitem__() jo bhi object iterable hoga yani jis object ko ham loop me asani se chala skte h usme ye hoga phle se hi

Iterator =__next__() isme ye next function hota h, ye jab iterable object ko chalate h to ye uska next  item deta rhega
Iteration =  the method of iterate is called iteration

ase hi generators ek trh ke  iterators hote h jo ki ek bar hi travers kr skte h unhe ham
inka use ham ram bachane k liye krte h kuki generators on the fly value ko generate krte h jse ye range function h
"""

# for i in range(70001154435165465): # kitni hi badi value dedo memory par koi frk nhi pdta
#     print(i) # ye on the fly in values ko generate krta h asa ni h ek sath inhe memory me store kr lega ye run hote time hi generate krta jata h ise chahhe ram se jyada value bhi denge tab bhi run krega kuki on the fly ye values ko generate kr rha h
#

# def gen(n):
#     for i in range(n):
#         yield i # ham is yield ka use krte h generator bnane m
# g = gen(5)
# print(g)
# print(g.__next__())
# print(g.__next__()) # to ham jitni bar bhi ye chalayegne utni hi value deta chala jayega ye 5 value dega agr ye 6 bar next fucniton chalaya to eroor dega
# # or hmne ab yha for loop chalaya to ye age tak print hogya or khud hi ruk bhi gya jha ise value milni bnd hogyi
# # for i in g: #or ye 2 se chlna suru hua kuki 2 tak ki value to is g m thi phle se hi usse agge ise for loop le gya
# #     print(i)
#
# f = "gaurav" # string iterable hoti isliye isme iter function hota h or ye ase kam krtih
#
# g = iter(f)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__()) # to ase next function se ham ise agge tak chala skte h


def fibo(n):
    a,b = 0,1
    while a<=n:
        a,b=b,a+b
        yield a
c = fibo(9)
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())


#5! = 5*4*3*2*1 = 120
def factorial(n):
    v= 1
    for i in range(n,0,-1):

        v = v*i



        yield v

a = factorial(5)

print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())


def factorial(n):
    v = 1
    for i in range(n):
        v = v*(i+1)

    return v
print(factorial(5))
