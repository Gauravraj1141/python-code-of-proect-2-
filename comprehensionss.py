# list comprehensions

ls = []
for i in range(100):
    if i%2 == 0:
        (ls.append(i))
print(ls,end=" ")
#list comprehension ke help se ham in lines ko ek line me add kr skte h
ip = int(input("enter number that you want table of that number : "))
ls = [i for i in range(1,ip*11) if i%ip == 0 ] #to ase krke ham list comprehension or alg alg data type k sath kr skte h
print(ls)

# ase hi ham dictonary ke sath bhi kr skte h
dict = { i:f"Item{i} "for i in range(1,9) }
dict2 = {value:key for key,value in dict.items()} # ase krke ham key or value ko change kr skte h dict ko ulta kr dia hmne
print(dict,"\n" ,dict2)
print(dict.__sizeof__())
print(dict2.__sizeof__())

# set compreshensions
dresses = {dress for dress in ["dress 1","dress2","dress2","dress2"]} #ye set h jisme repetetion nhi hota h
dres = [dress for dress in ["dress 1","dress2","dress2","dress2"]] # ye ek list h jisme sb kuch print ho rha h
print(f"size of ]set,{dresses.__sizeof__()},{type(dresses)}") # ye hmne inke size or type dekhe h
print(f"size of list,{dres.__sizeof__()},{type(dres)}")
print(dresses,dres)

# generator comprehensions
gn = (i for i in range(100) if i%2 == 0) # or ase krke ham isme condition de skte h
print(type(gn))
print(gn.__next__())
print(gn.__next__())
print(gn.__next__())
# or yha par ise for loop se iterate bhi kr skte h or ise ham ek bar hi iterate kr skte h
for i in gn:
    print(i)

