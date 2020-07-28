##Atomic Operations

from threading import Thread
import time
import random

counter = 0

def increment_counter():
    global counter
    time.sleep(random.random())
    counter += 1
    time.sleep(random.random())
    print(f'New counter value: {counter}')
    time.sleep(random.random())
    print('-------')

if __name__ == "__main__":
    for x in range(10):
        t = Thread(increment_counter())
        time.sleep(random.random())
        t.start()

