from datetime import datetime, timedelta

expected_datetime = datetime.now() + timedelta(seconds=10)

while True:
    if datetime.now() > expected_datetime:
        print('test')
        expected_datetime = datetime.now() + timedelta(seconds=10)







