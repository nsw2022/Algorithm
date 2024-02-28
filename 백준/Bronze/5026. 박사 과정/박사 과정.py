user = input()    
for i in range(int(user)):
    user_i = input()
    if user_i == "P=NP":
        print("skipped")
        continue
    a=user_i.split("+")    
    print(int(a[0])+int(a[1]))
    