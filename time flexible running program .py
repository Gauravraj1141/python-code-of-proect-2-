import time
a = time.time()
v = int(input("enter time in minute while you want to run this function"))*60
def function(x):
    while True:
        g = v
        print(x)
        if time.time()-a>g:
         break
function("when we input minutes so program run till the end of minutes")
print(time.time()-a)



