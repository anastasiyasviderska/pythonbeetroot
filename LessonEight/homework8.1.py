#if the second exception is not implemented then program crashes. 
# To resolve the issue we can use except without parameters.

def oops():
    raise KeyError

def index_error():
    try:
        oops()
    except IndexError:
        print("Some Error")
    except:
        print ("Other Error")

index_error()