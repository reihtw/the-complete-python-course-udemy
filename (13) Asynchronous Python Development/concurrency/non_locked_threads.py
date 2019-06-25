import time
import random

from threading import Thread

counter = 0

def increment_counter():
    time.sleep(random.random())
    global counter
    time.sleep(random.random())
    counter += 1
    time.sleep(random.random())
    print(f'New counter value: {counter}')
    time.sleep(random.random())
    print('-------------------------')
    time.sleep(random.random())

for x in range(10):
    time.sleep(random.random())
    t = Thread(target=increment_counter)
    time.sleep(random.random())
    t.start()
