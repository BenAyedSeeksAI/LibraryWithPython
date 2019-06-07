import tkinter as tk
import backEnd
from tkinter import ttk
table1= None
def DisplayBooksList():
    Windowlist=tk.Tk()
    Windowlist.geometry("900x800")
    Windowlist.configure(background="MediumOrchid1")
    table = ttk.Treeview(Windowlist)
    table["columns"]=("one","two","three")
    table.column("one", width=200)
    table.column("two", width=200)
    table.column("three" ,  width=200)
    table.heading("#0",text="books")
    table.heading("one" , text="Title of the book")
    table.heading("two", text="Author")
    table.heading("three" ,text="genre")
    list = backEnd.selectBook()
    iterator=1
    for item in list:
        table.insert("" , 0,  text="Book "+str(iterator), values=(str(item[1]),str(item[2]),item[3]))
        iterator+=1
    table.grid(row=0,column=1)
    Windowlist.mainloop()
def banStudent():
    info = table1.get_children()
    selectedItem= table1.selection()
    info2 = table1.set(selectedItem[0])
    table1.delete(selectedItem[0])
    #print(info2)
    backEnd.deleteStudent(str(info2["one"]))





def DisplayStudents():
    global table1
    Windowlist = tk.Tk()
    Windowlist.geometry("900x800")
    Windowlist.configure(background="MediumOrchid1")
    table1 = ttk.Treeview(Windowlist)
    table1["columns"] = ("one", "two")
    table1.column("one", width=200)
    table1.column("two", width=200)
    table1.heading("#0", text="student")
    table1.heading("one", text="Name")
    table1.heading("two", text="password")
    list = backEnd.selectStudent()
    iterator = 1
    for item in list:
        table1.insert("", 0, text="student" + str(iterator), values=(str(item[1]), str(item[2])))
        iterator += 1
    table1.grid(row=0, column=1)
    login = tk.Button(Windowlist, text="ban", command=banStudent, width=10, fg="Black", font=("Helvetica", 12),
                      background="SteelBlue2").grid(row=2, column=1)
    Windowlist.mainloop()
