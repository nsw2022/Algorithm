while True:
    user=input().lower()
    if user=='#':
        break
    print(user[0], user.count(user[0],1,len(user)))

