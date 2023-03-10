import time


def shedule(f, n: int):
    time.sleep(n / 1000)
    f()


def hello():
    print("hello")


shedule(hello, 1000)
