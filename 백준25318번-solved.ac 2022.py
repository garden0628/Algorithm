from datetime import datetime

dt_object= []
level = []
n = int(input())
if n==0: print(0)
else:
    for i in range(n):
        str = input()
        list = str.split()
        dtime = list[0] + " " + list[1]
    
        dt_object.append(datetime.strptime(dtime, "%Y/%m/%d %H:%M:%S"))
        level.append(int(list[2]))

    denominator = 0
    numerator = 0
    for i in range(n):
        date_diff = dt_object[len(dt_object)-1] - dt_object[i]
        total_days = date_diff.days + (date_diff.seconds/(3600*24))
        #value = round(total_days/365, 3)
        value = total_days/365
        if(0.5**value>=0.9**(len(dt_object)-1-i)):
            denominator += 0.5**value
            numerator += (0.5**value)*level[i]
        else:
            denominator += 0.9**(len(dt_object)-1-i)
            numerator += (0.9**(len(dt_object)-1-i))*level[i]

    result = numerator/denominator
    print(round(result))
