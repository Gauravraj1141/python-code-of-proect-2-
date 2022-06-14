# now we learn f string

# m = "gaurav"
# f = 12
# str = "this is %s %s"%(m,f) # ham ase krke bhi kisi bhi str me variable ki value add kra skte h
# print(str)
#
#
# import math
# l = math.lcm(int(input("enter number ")),int(input("enter number ")),int(input("enter number ")))
# str = "this is {},{}, it is lcm = {}"
# b = str.format(m,f,l) # format keyword ka use krke bhi ham variable add kra skte
# # h or hmne ye math module import krke lcm bhi add kra dia h
# print(b)

#by using fstring
g = "gaurav"
l = 12
import random
r = random.randint(0,6)

a = f"it is a {g},{l}, random number in range (0,6)= {r}" # ye hoti h fstring isme kitne bhi variable add kr
# skte h asani se
print(a)

