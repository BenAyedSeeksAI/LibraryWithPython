import tkinter as tk
from tkinter import messagebox
import Student
import backEnd
from Projects.MainWindowFP import window


class application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.createElements()
        self.NameRegisterLabel =  None
        self.msg= None
    def createElements(self):
        self.NameLabel = tk.Label( text="User",background="MediumOrchid1" ,font=("Helvetica", 12),fg="White",width=20).grid(row=0, column=0)
        self.NameEntry = tk.Entry(font=("Helvetica", 12), fg="Black",width=30)
        self.NameEntry.grid(row=0, column=1)
        self.PsswdLabel = tk.Label(text="Password",background="MediumOrchid1" ,font=("Helvetica", 12),fg="White",width=20).grid(row=1, column=0)
        self.PsswdEntry = tk.Entry(show="*",font=("Helvetica", 12), fg="Black",width=30)
        self.PsswdEntry.grid(row=1, column=1)

        self.ConfirmButton = tk.Button(text="Sign in" ,width=10 ,fg="Black", font=("Helvetica", 12),background="SteelBlue2", command=self.signin).grid(row=2, column=0)
        self.RegisterButton = tk.Button( text="Sign up",width=10 , fg="Black", font=("Helvetica", 12),background="SteelBlue2",command=self.signup).grid(row=2, column=1)
        self.ConfirmStudent = tk.Button(text="Login student", width=10, fg="Black", font=("Helvetica", 12),
                                        background="SteelBlue2", command=Student.LoginStudent).grid(row=2, column=2)
    def signin(self):
        if backEnd.search(self.NameEntry.get(), self.PsswdEntry.get()):
            self.master.destroy()
            window()
        else:
            messagebox.showinfo("Error", "Login Failed!")
    def RegisterYeah(self):
        if self.NameRegisterEntry.get()=="" and self.PsswdRegisterEntry.get()=="":
            messagebox.showinfo("Error", "an Input is empty!\nplease fill it.")
        else:
            backEnd.register(self.NameRegisterEntry.get(), self.PsswdRegisterEntry.get())
            self.msg = tk.Label(text="Registration Accepted!",font=("Helvetica", 12),background="MediumOrchid1", fg="Green")
            self.msg.grid(row=3, column=0)


    def signup(self):
        self.NameRegisterLabel = tk.Label( fg="white" , background="MediumOrchid1" ,font=("Helvetica", 12),text="New User",width=20).grid(row=3, column=0)
        self.NameRegisterEntry = tk.Entry(font=("Helvetica", 12), fg="Black",width=30)
        self.NameRegisterEntry.grid(row=3, column=1)
        self.PsswdRegisterLabel = tk.Label(fg="white" ,  background="MediumOrchid1" ,font=("Helvetica", 12),text="Password",width=20).grid(row=4, column=0)
        self.PsswdRegisterEntry = tk.Entry( font=("Helvetica", 12), fg="Black",show="*",width=30)
        self.PsswdRegisterEntry.grid(row=4, column=1)
        self.ValidButton = tk.Button( text="Register",width=10 , fg="Black", font=("Helvetica", 12),background="SteelBlue2", command=self.RegisterYeah).grid(row=5, column=1)
root=tk.Tk()
root.geometry("700x500")
root.configure(background="MediumOrchid1")
backEnd.connect()
app = application(master=root)

root.mainloop()