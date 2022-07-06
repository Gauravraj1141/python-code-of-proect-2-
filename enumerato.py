l = ["bhindi","aalu ","saljam","tori"]
# i = 0
# for item in l:
#     if i%2==0: # yani iska use hmne isliye kiya hame ek chorkar print krna tha
#         print(item)
#     i +=1
#to isi chij ko short me krne k liye enumerate function ka use krte h

for i ,item in enumerate(l): #to is function me ham i (index) and item dono ko ek sath lekr enumerate fun ka use kr skte h
    if i%2==0:
        print(f"javesh please buy {item}")