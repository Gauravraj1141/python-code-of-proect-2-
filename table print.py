ip = int(input("enter number that you want table of that number : "))
ls = [i+ip for i in range(ip*10) if i%ip == 0 ]
print(ls)