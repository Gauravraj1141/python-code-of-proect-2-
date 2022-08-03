import time
from functools import lru_cache
#lru_cache ek decorator h hmne ise import kiya ye hamari calls ko save krega jisse ki jab ham call kre to time kam lge
ip = int(input("please tell how many calls store this"))
@lru_cache(maxsize=ip)# to yha ham jo input dete h utni hi calls ko vo cache kr payega

def some_work(n):
    time.sleep(n)
    return n
if __name__ == '__main__':
    some_work(3) # ye bs is suru  vali call me time lega 3 second or fir agli call diff call me time lega baki ki call same h to ve turant print hongi kuki ye jis call ko ek bar leleta h usme fir dobara se time nhi lega iska mtlb ye hota h
    print("this is first time")

    some_work(2)
    print("execution is done ")
    some_work(3)
    print("execution is done ")
    some_work(2)
    print("this is second type of func")
    some_work(2)
    print("it is chekcing")
    some_work(2)
    print("executed")





# @cache
#
# def fibo(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
#
#
# print(fibo(110))
# # print(fibo(int(input("enter number that you want to fibonacci number print: "))))
# print("execution time is :",time()-a,"seconds")
#
#






# from time import time
# from functools import cache
# a = time()
# print("starting time:" ,time()-a)
# # @lru_cache(maxsize=33)