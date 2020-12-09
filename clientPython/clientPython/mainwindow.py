from tkinter import *
from login import Login, Register
import socket

class MainWindow:
    def __init__(self):
        self.app = Tk()
        self.app.title("Login with Python")
        self.app.geometry("300x250")
        self.label = Label(self.app, text="Welcome To App", background='red')
        self.label.place(x=95, y=40)
        self.login = Button(self.app, text="Login",
                            pady=5, padx=20, command=login, background='tomato')
        self.login.place(x=100, y=100)
        self.register = Button(self.app, text="Register",
                               pady=5, padx=14, command=register, background='tomato')
        self.register.place(x=100, y=150)
        self.app.configure(bg='red')

    def run(self):
        self.app.mainloop()


def login():
    loginTk = Login()
    loginTk.run()


def register():
    registerTk = Register()
    registerTk.run()


#app = MainWindow()
#app.run()