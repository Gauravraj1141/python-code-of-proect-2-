# it is built in module in python
import os

print(dir(os)) # is module me jo kuch bhi isse ek list me ajata h
print(os.getcwd()) # isse cwd yani current working directory ajati h
os.chdir("c://") # chdir we can change the directory
print("now current working direcotry",os.getcwd()) # now we in c:// directory
f = open("gaurav.txt") # to jab hamari directory change ho gyi hmne jab ye file open ki to error agya kuki ab jis directory me hm h vha par gaurav.txt nhi h isliye ise comment kiya to fir se directory vhi hogyi

os.mkdir("rama") # To create a new directory or folder. The name is sent as a parameter inside the parenthesis.
os.makedirs("parent/child/grandchild") # ye ek se jyada directory or subdirectory bhi bna deta h
os.rename("oops.py","oopsbhat.py") #To rename an already existing directory, we use this. We send the current name and new name of our directory as parameters.
os.rmdir("thisname") # It deletes an empty directory.
os.removedirs("rama") #We can remove all directories within a directory by using removedirs()
print(os.environ.get('path')) # ye hamara environment variable set h path nam ka to isme pura path agya hamara
print(os.name) # hamare os ka name nt h
print(os.path.join("c://","//gaurav.txt")) # to ye isliye krte h ab ye joint  hogye ise hame slash lgane nhi pdte ye khud lga lega
print(os.path.exists("c://")) # ye true or false me batata h ki ye path exist bhi krta h ya nhi to ye exist krta h isliye true aya
print(os.path.isfile("C://user")) #It returns true if the path is an existing regular file.
print(os.path.isdir("c://")) # agr is dir me h to true hoga