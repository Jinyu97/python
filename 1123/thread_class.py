import threading, time

lock=threading.Lock() #줄바꿈 제대로 나오게 함. 없으면 동시에 여러 개가 한 줄에 나오고 줄바꿈도 한번에 몰아서 나옴

class cc1(threading.Thread):
    def run(self):
        for i in range (1,10):
            lock.acquire()
            print('$$$$$')
            lock.release()

tlist=[cc1() for _ in range(5)] #thread 5개 생성

for temp in tlist:
    temp.start()

print('main die')

for temp in tlist:
    temp.join() #main이 sub가 끝나기 전까지 안끝남