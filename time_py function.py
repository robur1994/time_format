def time_py(x):
    sec = 1
    min = 60
    hour = 3600
    day = 86400
    if x < hour  and x > min:
        time_min =  x // min  
        rim_res = time_min * min
        time_sec = x - rim_res 
        return (time_min, "minutes", time_sec, "secund")
    elif x >= hour and x < day:
        time_hour = x // hour
        rim_res = time_hour * hour
        time_min = (x - rim_res) // min
        time_sec = x - rim_res - (time_min * min) 
        return (time_hour, "hour", time_min, "minute", time_sec, " secund")
    elif x >= day:
        time_day = x // day
        rim_res = time_day * day
        time_hour = (x // hour) % 24
        time_min = ((x - rim_res) // min) % 60
        time_sec = (((x - rim_res) - hour)-60) % 60
      
        return (time_day, " :day", time_hour, ": hour",time_min, ": minute", time_sec, ":Secund")
    else:
        return (x, "secund")

print(time_py(int(input())))
