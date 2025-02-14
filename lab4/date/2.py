from datetime import datetime, timedelta
def day(date):
    
    yesterday = date - timedelta(days=1)
    tomorrow= date + timedelta(days=1)
    today =date
    print("вчера", yesterday.strftime("%d-%B-%Y"))
    print("завтра", tomorrow.strftime("%d-%B-%Y"))
    print("сегодня", today.strftime("%d-%B-%Y"))
now = datetime.now() 
day(now)
