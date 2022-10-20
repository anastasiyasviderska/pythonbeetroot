class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open ('logs.txt', 'a') as file_object:
            file_object.write(msg)
            file_object.close()

raise CustomException('Error 1')

