
# USING LIST COMPREHENSION
l = [i*i for i in range(1,10) ]
print("output list using for loop :", l)

sqr = []
for i in range(1,10):
    sqr.append(i**2)
print("output list using for loop :",sqr)

# USING DICTONARY COMPREHENSION

dic = { key:key**3 for key in range(1,8) if key%2 != 0}
print(dic)

state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']
dict = {state:capital for (state,capital) in zip(state,capital)}
print("using comprehension in dict:",dict)
print(type(dict))
#USING SET COPREHENSION
# set use curly brackets { }

input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
set = {i for i in input_list if i%2==0}
print("these all are even no and not repeated:",set)
print(type(set))

#USING GENERATOR COMPREHENSION
input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
gen = (i for i in input_list if i%2!=0)
#this is generator so we run this with for loop
for iten in gen:
    print(iten)
    print(type(gen))


















#HARRY BHAI👇👇




n = int(input("please tell us how many person's data want to add : "))
ip = 1
l = []


while ip <= n:
    ipn = input(f"enter no.{ip}  person detail : ")
    append = l.append(ipn)
    ip += 1
typ = int(
    input("which type of comprehensions you want \n press 1 for 'list comprehension'  press 2 for 'dictonary comprehension'  press 3 for 'set comprehension   and press 4 for generator comprehension \n :"))

if typ == 1:
    l = [i for i in l]


    print(l)

elif typ == 2:

    dict = {f"details persons  {i}": i  for i in l}
    print( dict)

elif typ == 3:

    n = {i for i in l}
    print(type(n))
    print(n)
elif typ == 4:
    n = (i for i in l)
for j in n:
    print(j)









