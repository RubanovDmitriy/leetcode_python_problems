import time

def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

# Создать и запустить поток
from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()