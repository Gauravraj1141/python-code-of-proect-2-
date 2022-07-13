# list comprehensions

# ls = []
# for i in range(100):
#     if i%2 == 0:
#         (ls.append(i))
# print(ls,end=" ")
#list comprehension ke help se ham in lines ko ek line me add kr skte h
ip = int(input("enter number that you want table of that number : "))
ls = [i+ip for i in range(ip*10) if i%ip == 0 ]
print(ls)