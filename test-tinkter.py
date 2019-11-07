from  tkinter  import  *

class  Mas_1(object):
    def __init__(self,size,title):
        self.size = size
        self.title = title
    def  mars_1_1(self):  #开启GUI设置窗口的大小和主题
         root = Tk()
         root.geometry(self.size)
         root.title(self.title)
         return root
    def  mars_1_2(self):#文本框
         for i in ["python","li"]:
             lab = Label(self.mars_1_1(),text=i,bg="#eeeeee")
         lab.pack()
         self.mars_1_1().mainloop()
    def  mar_1_3(self):#列表框
         theLB =Listbox(self.mars_1_1())
         item = ["192.168.0.1","192.168.0.110"]
         for i in item:
             theLB.insert(0,i)
         theLB.pack()
         self.mars_1_1().mainloop()
    def  mar_1_4(self):
         b1 = Button(self.mars_1_1(),text = 'hide',width = 15,height = 5,command= 'hello')
         b1.pack()



a = Mas_1('500x300','window')
a.mar_1_3()