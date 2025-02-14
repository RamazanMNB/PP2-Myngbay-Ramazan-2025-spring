from datetime import datetime, timedelta
def dayminus5(date,datetwo):
    
    dif = date - datetwo
    d=dif.days*24*60*60
    if d<0:
        print(str(d*(-1))+" seconds")
    else:
        print(str(d)+" seconds")
    

    1
mone = input("Введите первоначальную дату в формате ДД.ММ.ГГГГ: ") 
now = datetime.strptime(mone, "%d.%m.%Y")
date_str = input("Введите вторую дату в формате ДД.ММ.ГГГГ: ") 
my_date = datetime.strptime(date_str, "%d.%m.%Y")
dayminus5(now,my_date)



