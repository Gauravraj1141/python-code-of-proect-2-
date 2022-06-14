print("Welcome to this game \n \t\t\t\t\tYou have only 10 turns ")
v = 0
my_points = 0
your_points = 0
while v<=9:
    v = v+1
    import random
    p = ("s","w","g")
    l = random.choice(p)
    print("\n\nthis is = ",v,"turn")
    ip = input("select only one of these  ( s , w , g) = ")

    if l == "s" and ip == "w":
        print(f" cpu = {l} and user = {ip}  snake drinks water ,  cpu wins {v} turn")

        your_points = your_points +1
        print("your points",your_points)
    elif l == "w" and ip == "g":
        print(f"cpu = {l} and user = {ip}  gun is drown in water so cpu wins in {v} turn ")

        your_points = your_points + 1
        print("your points", your_points)
    elif l == "g" and ip == "s":
        print(f"cpu = {l} and user = {ip}  gun will killed snake so cpu wins in {v} turn ")

        your_points = your_points + 1
        print("your points", your_points)
    elif l == "s" and ip == "g":
        print(f"cpu = {l} and user = {ip}  gun will shot the snake so gaurav wins in {v} turn ")
        my_points = my_points +1

        print("my  points = ",my_points)
    elif l== "g" and ip =="w":
        print(f"cpu = {l} and user = {ip}  gun will drown in water so gaurav wins in {v} turn")
        my_points = my_points + 1

        print("my points = ", my_points)
    elif l== "w" and ip == "s":
        print(f"cpu = {l} and user = {ip}  snake drink water so gaurav wins in {v} turn")
        my_points = my_points + 1

        print("my points = ", my_points)
    else:
        print(f"cpu = {l} and user = {ip} both are same so it is draw")




    print("\nyour total  points  = ", your_points)
    print("my total  points = ", my_points)

    continue




