#
# def srq(x):
#     return x*x
# def cube(x):
#     return x*x*x
#
# fun = [srq,cube]
# for l in range(5):
#     a = list(map(lambda x: x(l), fun))
#     print(a)
#


# ye even no k liye
list1 = [1,5,4,7,8,9,5,6,3,4,77]
def even_no(num):
    return num%2==0

gr_5  = list(filter(even_no,list1)) # ye h filter function iska isme phle function dete h fir iterable
print(gr_5)

# from functools import reduce
#
# list = [1,2,3,4,5]
# add = reduce(lambda  x,y:x*y, list) # ye hmne functools se import kiya h or ye hamari list ke numbers ko ek ke bad ek add krta chalajayega or end me result dedega
# # or isse ham recursion bhi kr skte h
# print(add)