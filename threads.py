import threading, time

def multiply(multiplicand, multiplier):
    count=1
    while count <= 10:
        time.sleep(.5)
        multiplicand=multiplier*multiplicand
        print(multiplicand)
        count=count+1

try:
    x = threading.Thread(target=multiply, args=(3,3))
    x.start()
    y = threading.Thread(target=multiply, args=(10,2))
    y.start()
except Exception as e: print(e)