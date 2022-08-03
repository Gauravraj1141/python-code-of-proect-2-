import os
def soldier(path ,file , format):
    os.chdir(path)
    ls = os.listdir(path)
    v = 1
    with open(file) as f:
        filelist = f.read().split("\n")
    for list in ls:
        if list not in filelist:
            os.rename(list,list.upper())


        os.rename(list,list.upper())
        if list.endswith(format):
            os.rename(list, f"{v}.{list.lower()}")
            v+=1


if __name__ == '__main__':
    path = input("enter path : ")
    file = input("enter file name: ")
    format = input("enter format")
    soldier(path,file,format)