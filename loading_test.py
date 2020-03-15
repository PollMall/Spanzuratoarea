import time,os


def loading():
    prtg=0
    for i in range(11):
        print(str(prtg)+"%")
        time.sleep(0.5)
        prtg += 10


if __name__ == '__main__':
    loading()
