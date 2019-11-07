import threading
import time

event=threading.Event()
def test_wr():
    with open('D:\\test\\test.txt','a') as f:
          a=time.time()
          f.write('hello'+str(a)+'\n')
    event.set()

def delfile():
     #event.wait()
     #time.sleep(5)
     print('hellolloy')
     with open('D:\\test\\test.txt','w') as f1:
          f1.write(" ")

def main():
    treed = []
    print('>>>>>>>>','hello')
    for i in range(3):
        i = threading.Thread(target=test_wr)
        treed.append(i)
    s = threading.Thread(target=delfile)
    treed.append(s)
    for k in treed:
        k.start()
    for j in treed:
        j.join()

if  __name__ == '__main__':
    main()
