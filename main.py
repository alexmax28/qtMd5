import tkinter as tk
import hashlib

window = tk.Tk() # GUI的核心
window.title('GUI') # 程式上方的文字
window.geometry('500x300') #  長寬設定
window.resizable(False, False) # 定義可不可以被使用者放大縮小視窗
# window.iconbitmap('icon.ico') # 設定程式的圖示，可在括弧中放入檔案路徑

# key1 = tk.StringVar()
# value1 = tk.StringVar()
i = 1
arr=[]
strList = []
strDict = {}
ans =''
turn_md5= ''


frame = tk.Frame(window)

frame.pack(side='top')


frame1 = tk.Frame(window,height=200,background='#EE82EE',width=200)
frame1.pack()

def add_input():  
    global i 
    global arr
    if i <= 10:
        key1label = tk.Label(frame, text='Key:')
        key1label.grid(row=i, column=0)

        key1entry = tk.Entry(frame)
        key1entry.grid(row=i, column=1)
        # arr.append(key1entry)

        v1label = tk.Label(frame, text='Value:')
        v1label.grid(row=i, column=2)

        v1entry = tk.Entry(frame)
        v1entry.grid(row=i, column=3)

        # arr.append(v1entry)
        arr.append([key1entry,v1entry])
        # np.append(arr, [key1entry,v1entry], axis=None)
        print(arr)
        i=i+1
    else:
        return
    
def getarr():
    global arr 
    global strList
    global strDict
    global ans
    global turn_md5

    # 清空text_table
    T.delete("1.0","end")

    # 取arr裡input值放入dict
    for i in range(len(arr)):
        strDict[arr[i][0].get()] = arr[i][1].get()

    # 將dict排序
    result = sorted(strDict.items())
    # print(result)
    # strList.append('?')
    # 將dict值取出組字串加入list裡
    for item in result:
        strList.append(item[0])
        strList.append('=')
        strList.append(item[1])
        strList.append('&')
    print(strList)

    # 把list轉成字串 [:-1]移除字串最後一個字元
    ans = ''.join(strList).replace(' ','')[:-1]

    # 加入mainkey
    finalAns = f'{ans}&key={mainKey.get()}'
    print(finalAns)
    
    # 將字串轉成MD5
    turn_md5 = hashlib.md5(finalAns.encode('utf-8')).hexdigest().upper() 
    print(turn_md5)

    # insert 入textTable
    T.insert(tk.END, turn_md5)

    # 清空 list & dict
    strList.clear()
    strDict.clear()
    
    # print("key：", arr[i][0].get(), " ,vlaue:", arr[i][1].get())


# --------------------------------------------------------元件
v6label = tk.Label(frame, text='主Key:')
v6label.grid(row=0, column=0)
mainKey = tk.Entry(frame)
mainKey.grid(row=0, column=1)
# mainKey.insert(1,'aaa')

# --------------------------------------------------------btn

# group = tk.LabelFrame(window, text='按鈕')
# group.pack(side='bottom')

mybutton = tk.Button(frame1, text='增加資料', command=lambda: add_input())
mybutton.grid(row=0, column=1)

# shhowarrbutton = tk.Button(frame1, text='轉換', command=getarr)
# shhowarrbutton.grid(row=0, column=3)

# --------------------------------------------------------text
group = tk.LabelFrame(window, text='sign')
group.pack(side='bottom')
T = tk.Text(group,height = 1, width = 50)
T.grid(row=0, column=1)

shhowarrbutton = tk.Button(group, text='轉換', command=getarr)
shhowarrbutton.grid(row=0, column=2)

# --------------------------------------------------------
window.mainloop() # 會使程式常駐執行，記得要打在程式的最後一行




