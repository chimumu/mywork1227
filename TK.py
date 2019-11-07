from  tkinter import *
import  telnet
import threading
from ll import  test_wr,delfile
import time
root = Tk()
root.geometry('500x500')
root.title('telnet')

event=threading.Event()

def get_data(): #获取输入框的内容

    global root
    var = e.get()
    v = StringVar()
    str_li =var.split()
    telnet.main(str_li[0],str_li[1])

    with open('D:\\test\\test.txt', 'r') as f1:
        v.set(f1.read())
        m = Message(root, fg='green', width=200, textvariable=v)
        m.pack()


def get_text():
    global root
    vb = t.get('1.0','end')
    a=vb.splitlines()
    v1 = StringVar()
    thread = []
    for i in range(len(a)):
        b = a[i].split()
        th = threading.Thread(target=telnet.main,args=(b[0],b[1]))
        th.start()
        thread.append(th)
    for jk in thread:
         jk.join()

        #telnet.main(b[0], b[1])
    with open('D:\\test\\test.txt', 'r') as f2:
        v1.set(f2.read())
        m = Message(root, fg='green', width=200, textvariable=v1)
        m.pack()

    time.sleep(10)
    delfile()
l = Label(root, text='端口测试', bg='lavender', font=('Arial',12), width=100, height=2) #label
l.pack()


#e = Entry(root,show = None,font=('Arial',12),width=20, relief=RAISED) #文本框
#e.pack()


#b = Button(root, text='ok',font=('Arial', 12), width=5, height=1,command=get_data,activebackground='cyan',relief=RAISED) #按钮
#b.pack()

t= Text(root,height=4)
t.pack()

tb = Button(root,text='me',font=('Arial', 12), width=5, height=1,command=get_text)
tb.pack()



root.mainloop()
