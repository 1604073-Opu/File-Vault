
from tkinter import messagebox
import tkinter as tk

from timeloop import Timeloop

import SecondPage
import tkinter.ttk as ttk
from PIL import Image, ImageTk

import os.path
import pickle
import Lock


def login():
    global val, w, root
    root = tk.Tk()
    top = LogIn(root)
    root.mainloop()


def FaceLock():
    if Lock.capture():
        return True
    return False


def start():
    '''Starting point when module is the main routine'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel(root)
    root.mainloop()


def create_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = Toplevel(w)
    return (w, top)


def destroy_Toplevel():
    global root
    root.destroy()
    root = None


class Toplevel:

    def onSubmit(self):
        if self.passw.get() == self.cPass.get():
            dict = {}
            dict['username'] = self.username.get()
            dict['password'] = self.passw.get()
            dict['facelock'] = None
            f = open("Storage/Info.pkl", "wb")
            pickle.dump(dict, f)
            f.close()
            destroy_Toplevel()
            SecondPage.start(dict)
        else:
            messagebox.showerror('ERROR!', 'Password should match on both fields!')

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("684x484+360+111")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Locker")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.name = tk.Label(self.Frame1)
        self.name.place(relx=0.599, rely=0.227, height=21, width=38)
        self.name.configure(activebackground="#f9f9f9")
        self.name.configure(activeforeground="black")
        self.name.configure(background="#d9d9d9")
        self.name.configure(disabledforeground="#a3a3a3")
        self.name.configure(foreground="#000000")
        self.name.configure(highlightbackground="#d9d9d9")
        self.name.configure(highlightcolor="black")
        self.name.configure(text='''Name''')

        self.username = tk.Entry(self.Frame1)
        self.username.place(relx=0.599, rely=0.289, height=20, relwidth=0.24)
        self.username.configure(background="white")
        self.username.configure(disabledforeground="#a3a3a3")
        self.username.configure(font="TkFixedFont")
        self.username.configure(foreground="#000000")
        self.username.configure(highlightbackground="#d9d9d9")
        self.username.configure(highlightcolor="black")
        self.username.configure(insertbackground="black")
        self.username.configure(selectbackground="#c4c4c4")
        self.username.configure(selectforeground="black")

        self.password = tk.Label(self.Frame1)
        self.password.place(relx=0.599, rely=0.372, height=21, width=58)
        self.password.configure(activebackground="#f9f9f9")
        self.password.configure(activeforeground="black")
        self.password.configure(background="#d9d9d9")
        self.password.configure(disabledforeground="#a3a3a3")
        self.password.configure(foreground="#000000")
        self.password.configure(highlightbackground="#d9d9d9")
        self.password.configure(highlightcolor="black")
        self.password.configure(text='''Password''')

        self.passw = tk.Entry(self.Frame1, show="*")
        self.passw.place(relx=0.599, rely=0.434, height=20, relwidth=0.24)
        self.passw.configure(background="white")
        self.passw.configure(disabledforeground="#a3a3a3")
        self.passw.configure(font="TkFixedFont")
        self.passw.configure(foreground="#000000")
        self.passw.configure(highlightbackground="#d9d9d9")
        self.passw.configure(highlightcolor="black")
        self.passw.configure(insertbackground="black")
        self.passw.configure(selectbackground="#c4c4c4")
        self.passw.configure(selectforeground="black")

        self.cPassword = tk.Label(self.Frame1)
        self.cPassword.place(relx=0.599, rely=0.517, height=21, width=104)
        self.cPassword.configure(activebackground="#f9f9f9")
        self.cPassword.configure(activeforeground="black")
        self.cPassword.configure(background="#d9d9d9")
        self.cPassword.configure(disabledforeground="#a3a3a3")
        self.cPassword.configure(foreground="#000000")
        self.cPassword.configure(highlightbackground="#d9d9d9")
        self.cPassword.configure(highlightcolor="black")
        self.cPassword.configure(text='''Confirm Password''')

        self.cPass = tk.Entry(self.Frame1, show="*")
        self.cPass.place(relx=0.599, rely=0.579, height=20, relwidth=0.24)
        self.cPass.configure(background="white")
        self.cPass.configure(disabledforeground="#a3a3a3")
        self.cPass.configure(font="TkFixedFont")
        self.cPass.configure(foreground="#000000")
        self.cPass.configure(highlightbackground="#d9d9d9")
        self.cPass.configure(highlightcolor="black")
        self.cPass.configure(insertbackground="black")
        self.cPass.configure(selectbackground="#c4c4c4")
        self.cPass.configure(selectforeground="black")

        self.submit = tk.Button(self.Frame1, command=self.onSubmit)
        self.submit.place(relx=0.673, rely=0.744, height=34, width=57)
        self.submit.configure(activebackground="#ececec")
        self.submit.configure(activeforeground="#000000")
        self.submit.configure(background="#d9d9d9")
        self.submit.configure(disabledforeground="#a3a3a3")
        self.submit.configure(foreground="#000000")
        self.submit.configure(highlightbackground="#d9d9d9")
        self.submit.configure(highlightcolor="black")
        self.submit.configure(pady="0")
        self.submit.configure(text='''Submit''')

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.234, rely=0.455, height=141, width=174)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.117, rely=0.248, height=221, width=214)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        photo_location = os.path.join("E:\Python\Projects\Vault1.0\Images\locker.png")
        global _img0
        _img0 = ImageTk.PhotoImage(file=photo_location)
        self.Label2.configure(image=_img0)


class LogIn:

    def onSubmit(self):
        if self.passw.get() == self.x['password']:
            destroy_Toplevel()
            SecondPage.start(self.x)
        else:
            messagebox.showerror('ERROR!', 'Wrong Password!')

    def __init__(self, top=None):

        with open('Storage/Info.pkl', 'rb') as f:
            self.x = pickle.load(f)
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("684x484+360+111")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Locker")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.name = tk.Label(self.Frame1)
        self.name.place(relx=0.599, rely=0.227, height=21, width=38)
        self.name.configure(activebackground="#f9f9f9")
        self.name.configure(activeforeground="black")
        self.name.configure(background="#d9d9d9")
        self.name.configure(disabledforeground="#a3a3a3")
        self.name.configure(foreground="#000000")
        self.name.configure(highlightbackground="#d9d9d9")
        self.name.configure(highlightcolor="black")
        self.name.configure(text='''Name''')

        self.username = tk.Label(self.Frame1)
        self.username.place(relx=0.599, rely=0.289, height=20, relwidth=0.24)
        self.username.configure(background="white")
        self.username.configure(disabledforeground="#a3a3a3")
        self.username.configure(font="TkFixedFont")
        self.username.configure(foreground="#000000")
        self.username.configure(highlightbackground="#d9d9d9")
        self.username.configure(highlightcolor="black")
        self.username.configure(text=self.x['username'])

        self.password = tk.Label(self.Frame1)
        self.password.place(relx=0.599, rely=0.372, height=21, width=58)
        self.password.configure(activebackground="#f9f9f9")
        self.password.configure(activeforeground="black")
        self.password.configure(background="#d9d9d9")
        self.password.configure(disabledforeground="#a3a3a3")
        self.password.configure(foreground="#000000")
        self.password.configure(highlightbackground="#d9d9d9")
        self.password.configure(highlightcolor="black")
        self.password.configure(text='''Password''')

        self.passw = tk.Entry(self.Frame1, show="*")
        self.passw.place(relx=0.599, rely=0.434, height=20, relwidth=0.24)
        self.passw.configure(background="white")
        self.passw.configure(disabledforeground="#a3a3a3")
        self.passw.configure(font="TkFixedFont")
        self.passw.configure(foreground="#000000")
        self.passw.configure(highlightbackground="#d9d9d9")
        self.passw.configure(highlightcolor="black")
        self.passw.configure(insertbackground="black")
        self.passw.configure(selectbackground="#c4c4c4")
        self.passw.configure(selectforeground="black")

        self.submit = tk.Button(self.Frame1, command=self.onSubmit)
        self.submit.place(relx=0.673, rely=0.744, height=34, width=57)
        self.submit.configure(activebackground="#ececec")
        self.submit.configure(activeforeground="#000000")
        self.submit.configure(background="#d9d9d9")
        self.submit.configure(disabledforeground="#a3a3a3")
        self.submit.configure(foreground="#000000")
        self.submit.configure(highlightbackground="#d9d9d9")
        self.submit.configure(highlightcolor="black")
        self.submit.configure(pady="0")
        self.submit.configure(text='''Log In''')

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.234, rely=0.455, height=141, width=174)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.117, rely=0.248, height=221, width=214)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        photo_location = os.path.join("Images\locker.png")
        global _img0
        _img0 = ImageTk.PhotoImage(file=photo_location)
        self.Label2.configure(image=_img0)


if __name__ == '__main__':
    if os.path.exists('Storage/Info.pkl'):
        with open('Storage/Info.pkl', 'rb') as f:
            dict = pickle.load(f)
        if dict['facelock'] == None:
            login()
        else:
            if FaceLock():
                SecondPage.start(dict,True)
            else:
                login()
    else:
        start()
