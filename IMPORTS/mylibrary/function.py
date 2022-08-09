from pytube import YouTube
from tkinter import *

a,b = 0,1

class Load_App(Tk):

    def __init__(self):
        super().__init__()
        self.title("Загрузчик")
        self.geometry("500x500")
        self.msg = Message(self, text=a)


        self.load_v = Entry(self, width=100)
        self.login_btn = Button(self, text="Скачать",
                                command=self.print_login)
        self.clear_btn = Button(self, text="Очистить",
                                command=self.clear_form)
        self.load_v.pack()
        self.login_btn.pack(fill=BOTH)
        self.clear_btn.pack(fill=BOTH)
        self.msg.pack()


    def print_login(self):
        global a,b
        link = ("ссылка: {}".format(self.load_v.get()))
        yt = YouTube(link)
        a = "загружаю"
        ys = yt.streams.get_highest_resolution()
        ys.download("Desktop\ютубчик")
        b = "Готово!"

    def clear_form(self):
        self.load_v.delete(0, END)
        self.load_v.focus_set()


if __name__ == "__main__":
    app = Load_App()

    app.mainloop()
