from datetime import datetime

while True:
    user_input = input().split(" ")
    
    user_day= int(user_input[0])
    user_month = int(user_input[1])
    user_year = int(user_input[2])
    if user_day==0 and user_month==0 and user_year==0:
        break
    time1 = datetime(user_year, user_month, user_day, 0, 0, 0)
    time2 = datetime(user_year, 1, 1, 0, 0, 0)
    
    print((time1-time2).days+1) 
    
  
