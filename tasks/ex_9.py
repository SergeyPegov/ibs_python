import threading
import time

def thread_1():
    print('Potok_1 start')

    for i in range(10, 0, -1):
        print(f'Potok_1:{i}')
        time.sleep(1)

    print('Potok_1 finish')


def thread_2():
    print('Potok_2 start')

    for i in range(10, 0, -1):
        print(f'Potok_2:{i}')
        time.sleep(1)

    print('Potok_2 finish')

thr_1 = threading.Thread(target=thread_1)
thr_2 = threading.Thread(target=thread_2)


thr_1.start()
thr_2.start()