import threading, time

def test(id): #prcess 정의. id는 의미 없음. 그냥 숫자 주기 위함
    for i in range(1,10):
        time.sleep(0.5)
        print('# %d %d'%(id,i))

#args: id에 값 줌
th1=threading.Thread(target=test, args=(1,))
th1.start()

for i in range(1, 10): #main process
    time.sleep(0.2) #0.7-섞여서 나옴, 0.2=main 끝나도 th1 계속 나옴(join 없을때)
    print("main %d"%i)

th1.join() #main이 sub가 끝날 때까지 안 끝남