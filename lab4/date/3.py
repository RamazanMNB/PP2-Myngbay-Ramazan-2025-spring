from datetime import datetime, timedelta
def day(date):
    today =date
    print( today.strftime("%x-%X"))
now = datetime.now() 
day(now)