from datetime import datetime, timedelta

current_time = datetime.now()

timer = current_time + timedelta(seconds=10)

for x in range (10):
    while timer > datetime.now():
        pass
    print("It's time!")
    timer = datetime.now() + timedelta(seconds=10)







