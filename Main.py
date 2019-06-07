import tkinter as tk


class application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createElements()
    def createElements(self):
        self.NameLabel = self.makeLabel(title="Name",rowX=0,columnX=0)
        self.NameEntry = self.makeEntry(rowX=0,columnX=1)
        self.PsswdLabel = self.makeLabel(title="Password",rowX=1,columnX=0)
        self.PsswdEntry = self.makeEntry(rowX=1,columnX=1)
        self.ConfirmButton = self.makeButton(title="CONNECT",rowX=2,columnX=0 ,action=self.verifyConnection)

    def verifyConnection(self):
        with open("data.txt", "r") as file:
            name = file.readline()
            name= name.rstrip(" \n")
            pwd = file.readline()
            pwd = pwd.rstrip(" \n")
        NameValue = self.NameEntry.get()
        PwdValue = self.PsswdEntry.get()
        if NameValue == name and PwdValue == pwd :
            self.level = tk.Toplevel(self.master)
            LabelHelloWorld = tk.Label( self.level,text="Hello Worldfsdf")
            LabelHelloWorld.pack()
        else:
            self.message = self.makeLabel(title="ERROR 404",rowX=4,columnX=0 )
            self.message.configure(fg="red")




root=tk.Tk()

app = application(master=root)
with open("data.txt" ,"r") as file:
    name = file.readline()
    name.rstrip(" \n")
    pwd = file.readline()
    pwd.rstrip(" \n")

root.mainloop()