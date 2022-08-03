import pickle

#pickling a python object
list = ["ram ","shaym",2,56,("radha","gita")]
file = "store.pkl" #we create a file .pkl it store data in bites
fileobj = open(file,"wb") # it is in write bite because we store this list as a bite .
pickle.dump(list,fileobj) # ye dump kiya list ko is fileobj ye isliye fileobj liya jisse ye data is open file me binary file  form m store ho jaye
fileobj.close()

#now unpickle a python object
# file = "store.pkl"
# fileobj = open(file, "rb") #ye rb isliye kuki yha read binary  mode m file ko open kiya jisse ye binary ko read kr le
# # pickdata = pickle.load(fileobj)
# # print(pickdata)
file = "store.pkl"
fileobj = open(file, "rb")
dl = fileobj.read()
data= pickle.loads(dl)
print(data)