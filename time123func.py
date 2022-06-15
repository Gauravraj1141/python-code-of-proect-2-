import time
l = time.time() # ye time ka function h isse ham time ka pta lga skte h code ko execute hone me kitna time lga
print(l)
for i in range(20):
    print("gaurav is a good boy   ")
    print(time.time()-l)

m = 1
l = time.time()
while m<20:
    m+=1
    print("gaurav is a good boy haha ")
    print(time.time()-l) # for or while loop me lgbhag same time lgta h



localtime = (time.asctime(time.localtime(time.time()))) #iska use ham local time and date k liye krte h
print(localtime)

print(time.gmtime(0)) #The epoch is the point where the time starts and is platform-dependent
# . On Windows and most Unix systems, the epoch is January 1, 1970, 00:00:00 (UTC),
# and leap seconds are not counted towards the time in seconds since the epoch.
To check what the epoch is on a given platform we can use   = time.gmtime(0).

for i in range(20):
    time.sleep(3) # ye is gaurav ko print krne m 3 sec k break lega yhi is sleep function ka use h
    print("gaurav")