from pytube import YouTube
import tkinter as tk


class Load_App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.load_v = tk.Entry(self)
        self.login_btn = tk.Button(self, text="Скачать",
                                   command=self.print_login)
        self.clear_btn = tk.Button(self, text="Очистить",
                                   command=self.clear_form)
        self.load_v.pack()
        self.login_btn.pack(fill=tk.BOTH)
        self.clear_btn.pack(fill=tk.BOTH)

    def print_login(self):
        link = ("Логин: {}".format(self.load_v.get()))
        yt = YouTube(link)
        ys = yt.streams.get_highest_resolution()
        print("Еще немножечко...")
        ys.download("Desktop\ютубчик")
        print("Лови видюху. ГОТОВО!!!!")

    def clear_form(self):
        self.load_v.delete(0, tk.END)
        self.load_v.focus_set()


if __name__ == "__main__":
    app = Load_App()
    app.mainloop()

    link = input("Введите ссылку с ютуба:  ")
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    print("Еще немножечко...")
    ys.download("Desktop\ютубчик")
    print("Лови видюху. ГОТОВО!!!!")
