from  tkinter  import *

from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename

root = Tk()
root.geometry('700x100')
root.title('alyasis')

def select_dir_path():
    path = askdirectory()
    dir_path.set(path)
dir_path = StringVar()
#第一个标签，选择文件夹路径
Label(root,text = "目标路径:").grid(row = 0, column = 0)
Entry(root, textvariable = dir_path, width = 80).grid(row = 0, column = 1)
Button(root, text = "路径选择", command = select_dir_path).grid(row = 0, column = 2)

def select_file_path():
    path = askopenfilename()
    filePath.set(path)

filePath = StringVar()

#第二个标签，选择文件路径
Label(root, text = " 文件路径：").grid(row = 1 , column = 0)
Entry(root, textvariable = filePath, width = 80).grid(row = 1, column= 1)
Button(root, text = "文件选择", command=select_file_path).grid(row = 1, column = 2)

def execute():
    pass
#button
exe_button = Button(root, text = "execute", command=execute)
exe_button.grid(row = 2, column = 1)
root.mainloop()