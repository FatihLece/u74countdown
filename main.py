import time


def countdown(t):
    number = 10
    while number > 0:
        print(number)
        time.sleep(1)  # pause comment!
        number -= 1

countdown(10)
