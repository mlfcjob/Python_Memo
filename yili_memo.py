#coding:utf-8

# @Author: Longfei Ma
# @Date: Aug 2nd 2018
# @Version: 1.0
# @Desc: a memo for yili


#导入图形库
import tkinter
import tkinter.messagebox
import sys
import pickle
from tkinter import ttk
import threading
import time
import datetime
import pyglet
import winsound

memo_todo = []

class MemoItem():
    def __init__(self, todo, todo_year, todo_month, todo_day, todo_hour, todo_min, todo_sec):
        self.todo = todo
        self.todo_year = todo_year
        self.todo_month = todo_month
        self.todo_day = todo_day
        self.todo_hour = todo_hour
        self.todo_min = todo_min
        self.todo_sec = todo_sec

class Memo(tkinter.Tk):
    def __init__(self):
        super().__init__()
        # self.memo_todo = []
        self.cur_row = 0
        self.button_row = 20
        # self.button_list = ["增加备忘", "删除备忘", "修改备忘", "查看已添加任务列表", "保存备忘"]
        # self.button_command = [self.add_memo, self.del_memo, self.modify_memo, self.find_memo, self.save_memo]
        self.button_list = ["增加备忘", "删除备忘", "查看已添加任务列表"]
        self.button_command = [self.add_memo, self.del_memo, self.find_memo]
        print(f'path:{sys.path[0]}')
        # self.photo = tkinter.PhotoImage(file=sys.path[0] + '\\tech.gif')
        #self.photo = tkinter.PhotoImage('tech.gif')
        # self.file = open("C:\\Windows\\memo.txt", "wb")
        self.timer = threading.Timer(1.0, self.check_timer)
        self.timer.start()
        self.now = time.localtime(time.time())
        # self.music = pyglet.media.load(sys.path[0] + '\\tishi.wav')
        # pyglet.resource.path = ['.']
        # pyglet.resource.reindex()
        # self.music = pyglet.resource.media(sys.path[0] + '\\tishi.mp3', streaming=False)

    def check_timer(self):
        # print(f'{self.now.tm_year}-{self.now.tm_mon}-{self.now.tm_mday}: {self.now.tm_hour}:{self.now.tm_min}:{self.now.tm_sec}')

        self.now = time.localtime(time.time())
        for item in memo_todo:
            # print(f'todo:{item.todo}, time:{item.todo_year}-{item.todo_month}-{item.todo_day} | {item.todo_hour}:{item.todo_min}:{item.todo_sec}')
            if int(item.todo_year) == self.now.tm_year:
                if int(item.todo_month) == self.now.tm_mon:
                    if int(item.todo_day) == self.now.tm_mday:
                        if int(item.todo_hour) == self.now.tm_hour:
                            if int(item.todo_min) == self.now.tm_min:
                                print(f'55555555555555555')
                                if int(item.todo_sec) == self.now.tm_sec:
                                    print(f'666666666666666666')
                                    # self.music.play()
                                    # winsound.PlaySound(sys.path[0] + '\\tishi.wav', flags=1)
                                    # winsound.Beep(400, 1000)
                                    tkinter.messagebox.showinfo(title="待办任务",message=item.todo)
                                   
        self.timer = threading.Timer(1.0, self.check_timer)
        self.timer.start()

    def get_now_time(self):
        return self.now

    def init_window(self):
   
        self.resizable(0, 0)
        self.title("备忘录(伊利)")
        self.attributes("-alpha", 0.9)
        self['bg'] = "green"
        self.bg_label = tkinter.Label(self, padx=0, text="欢迎来到备忘录",bg="green", fg="red", font=('黑体', 20), relief=tkinter.SUNKEN,compound=tkinter.CENTER).grid(row=self.cur_row, column=0, columnspan=2)
        # self.bg_label = tkinter.Label(self,image=self.photo, padx=0, text="欢迎来到备忘录",bg="green", fg="red", font=('黑体', 20), relief=tkinter.SUNKEN,compound=tkinter.CENTER).grid(row=self.cur_row, column=0, columnspan=2)
        self.cur_row += 20
        
    def welcome(self):
        for item in self.button_list:
            print(f'item:{item}')
            tkinter.Button(self, text=item, bg="blue", fg="black", font=('Helvetica', '8', 'bold'), relief=tkinter.RIDGE, width=20, height=1, command=self.button_command[self.button_list.index(item)]).grid(row=self.button_row, column=1, columnspan=1)
            self.button_row += 1

    def add_memo(self):
        aw = AddDialog(self)
        self.wait_window(aw)
        return

    def del_memo(self):
        print('del')
        dw = DelItemDialog(self)
        self.wait_window(dw)
        return 

    def modify_memo(self):
        print('modify')


    def find_memo(self):
        # print(f'待办事项：{self.get_memo()}')
        # self.file = open("C:\\Windows\\memo.txt", "rb")
        # data = pickle.load(self.file)

        # for item in memo_todo:
        #     print(f'待办事项: {item.todo}')
        sw = ShowItemDialog(self)
        self.wait_window(sw)
        return 


    def save_memo(self):
        print('save')

    def add_memo_item(self, todo):
        print(f'todo:{todo}')
        self.memo_todo.append(todo)
        print(f'在父类中：待办列表:{self.memo_todo}')

    def get_memo(self):
        return self.memo_todo

class AddDialog(Memo):
    def __init__(self, parent):
        super().__init__()
        self.title("增加备忘")
        row1 = tkinter.Frame(self)
        row1.pack(fill="x")
        tkinter.Label(row1, text="事件", width=8).pack(side=tkinter.LEFT)
        self.name = "请输入待办事项"
        print(f'self.name:{self.name}')
        self.entry = tkinter.Entry(row1, textvariable=self.name, width=30)
        self.entry.pack(side=tkinter.LEFT)


        row2 = tkinter.Frame(self)
        row2.pack(fill='x')
        tkinter.Label(row2, text="提醒时间",width=8).pack(side=tkinter.LEFT)

        now = super(AddDialog, self).get_now_time()
        print(f'now:{now}')
        
        self.year_combox = ttk.Combobox(row2, width=4, textvariable="年")
        self.year_combox['values'] = (2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030)
        self.year_combox.pack(side=tkinter.LEFT)
        self.year_combox.current(now.tm_year - 2018)
        tkinter.Label(row2, text="年").pack(side=tkinter.LEFT)

        self.month_combox = ttk.Combobox(row2, width=2, textvariable="月")
        self.month_combox['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        self.month_combox.pack(side=tkinter.LEFT)
        self.month_combox.current(now.tm_mon - 1)
        
        tkinter.Label(row2, text="月").pack(side=tkinter.LEFT)
        
        self.day_combox = ttk.Combobox(row2, width=2, textvariable="日")
        self.day_combox['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
        self.day_combox.pack(side=tkinter.LEFT)
        self.day_combox.current(now.tm_mday - 1)
        tkinter.Label(row2, text="日").pack(side=tkinter.LEFT)
     
        self.hour_combox = ttk.Combobox(row2, width=2, textvariable="时")
        self.hour_combox['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
        self.hour_combox.pack(side=tkinter.LEFT)
        self.hour_combox.current(now.tm_hour)
        tkinter.Label(row2, text="时").pack(side=tkinter.LEFT)

        self.min_combox = ttk.Combobox(row2, width=2, textvariable="分")
        self.min_combox['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59)
        self.min_combox.pack(side=tkinter.LEFT)
        self.min_combox.current(now.tm_min)
        tkinter.Label(row2, text="分").pack(side=tkinter.LEFT)

        self.sec_combox = ttk.Combobox(row2, width=2, textvariable="秒")
        self.sec_combox['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59)
        self.sec_combox.pack(side=tkinter.LEFT)
        self.sec_combox.current(now.tm_sec)
        tkinter.Label(row2, text="秒").pack(side=tkinter.LEFT)

        row3=tkinter.Frame(self)
        row3.pack(fill='x')
        tkinter.Button(row3, text="增加备忘",command=self.ok).pack(side=tkinter.RIGHT)
        tkinter.Button(row3, text="完成增加",command=self.cancel).pack(side=tkinter.RIGHT)

    
    def ok(self):
        memo_str = str(self.month_combox.get())+ "月" + str(self.day_combox.get()) + "日" + str(self.hour_combox.get()) + "时" + str(self.min_combox.get()) + "分" + str(self.sec_combox.get()) + "秒:" + self.entry.get()
        memo =MemoItem(self.entry.get(), self.year_combox.get(), self.month_combox.get(), self.day_combox.get(), self.hour_combox.get(), self.min_combox.get(), self.sec_combox.get())
        memo_todo.append(memo)
        # super(AddDialog, self).add_memo_item(memo)
        
        # self.file = open("C:\\Windows\\memo.txt", "wb")
        # pickle.dump(memo_str, self.file)
        print(memo_todo)

        # 清空文本输入框内容
        self.entry.delete(0, tkinter.END)
        now = super(AddDialog, self).get_now_time()
        self.year_combox.current(now.tm_year - 2018)
        self.month_combox.current(now.tm_mon)
        self.day_combox.current(now.tm_mday)
        self.hour_combox.current(now.tm_hour)
        self.min_combox.current(now.tm_min)

    
    def cancel(self):
        print(f'增加完毕')
        # self.file.close()
        self.destroy()

class ShowItemDialog(Memo):
    def __init__(self, parent):
        super().__init__()
        self.title("显示已经添加的任务列表")
        row1 = tkinter.Frame(self)
        row1.pack(fill="x")
        tkinter.Label(row1, text="时间", width=20).pack(side=tkinter.LEFT)
        tkinter.Label(row1, text="任务", width=20).pack(side=tkinter.LEFT)

        for item in memo_todo:
            row = tkinter.Frame(self)
            row.pack(fill="x")
            item_todo = item.todo
            item_todo_time = str(item.todo_year) + "-" + str(item.todo_month) + "-" + str(item.todo_day) + "-" + str(item.todo_hour) + ":" +  str(item.todo_min) + ":" + str(item.todo_sec)
            tkinter.Label(row, text=item_todo_time, width=15, bg="yellow", fg="red").pack(side=tkinter.LEFT)
            tkinter.Label(row, text=item_todo, width=30, bg="yellow", fg="red").pack(side=tkinter.LEFT)

class DelItemDialog(Memo):
    def __init__(self, parent):
        super().__init__()
        row1 = tkinter.Frame(self)
        row1.pack(fill="x")
        tkinter.Label(row1, text="ID", width=20).pack(side=tkinter.LEFT)
        tkinter.Label(row1, text="时间", width=20).pack(side=tkinter.LEFT)
        tkinter.Label(row1, text="任务", width=20).pack(side=tkinter.LEFT)

        for item in memo_todo:
            row = tkinter.Frame(self)
            row.pack(fill="x")
            item_todo = item.todo
            item_todo_time = str(item.todo_year) + "-" + str(item.todo_month) + "-" + str(item.todo_day) + "-" + str(item.todo_hour) + ":" +  str(item.todo_min) + ":" + str(item.todo_sec)
            tkinter.Checkbutton(row, text="删除").pack(side=tkinter.LEFT)
            tkinter.Label(row, text=str(memo_todo.index(item) + 1), width = 15, bg="yellow", fg="red").pack(side=tkinter.LEFT)
            tkinter.Label(row, text=item_todo_time, width=15, bg="yellow", fg="red").pack(side=tkinter.LEFT)
            tkinter.Label(row, text=item_todo, width=30, bg="yellow", fg="red").pack(side=tkinter.LEFT)

    def del_item(self):
        memo_todo.remove()


# 主程序模块
if __name__ == "__main__":
    s = Memo()
    s.init_window()
    s.welcome()
    s.mainloop()