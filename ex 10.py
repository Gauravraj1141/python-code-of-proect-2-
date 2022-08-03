import pickle
import requests

newfiles = []

a = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
getdata = a.content
with open("data.txt","wb") as data:
    data.write(getdata)

file = open("data.txt", "r")
for i in file:
    newfiles.append(i.strip().splitlines())


with open( "datast.pkl" ,"wb") as fileadd:
    pickle.dump(newfiles,fileadd)

with open("datast.pkl","rb") as fileread:
    unpickle = pickle.load(fileread)
    print(unpickle)





