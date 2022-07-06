# Python program to demonstrate working
# of map.

# Return double of n using map function
def addition(n):
	return n + n
#
# # We double all numbers using map()
numbers = (1, 2, 3, 4,5,6,8,52,)
result = list(map(addition, numbers))
print((result))
numbers1= (1, 2, 3, 4,4,5,6,4,7,7)
numbers2 = (2,3,5,4,7,8,4,5,7,4)
#
l = map(lambda x,y: x + y, numbers1,numbers2 )
print(list(l))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)
