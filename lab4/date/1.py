from datetime import datetime, timedelta
def dayminus5(date):
    
    future = date - timedelta(days=5)
    print("5 дней назад:", future)
now = datetime.now() 
dayminus5(now)



