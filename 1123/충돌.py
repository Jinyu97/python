import threading, time

lock=threading.Lock() #줄바꿈 제대로 나오게 함. 없으면 동시에 여러 개가 한 줄에 나오고 줄바꿈도 한번에 몰아서 나옴

def test(id):
    for i in range(1,10):
        lock.acquire()
        print('# %d %d'%(id,i))
        lock.release()

tlist=[threading.Thread(target=test, args=(1,)) for i in range(5)]

for temp in tlist:
    temp.start()

print('main die')

for temp in tlist:
    temp.join()