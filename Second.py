import tkinter as tk

class mainwindow:
    def __init__(self,master):
        self.master= master
        self.createElements()

    def createElements(self):
        self.NameLabel = self.makeLabel(title="Name", rowX=0, columnX=0)

    def makeLabel(master,title,rowX=0,columnX=0):
        Lab = tk.Label(master,text=title)
        Lab.grid(row=rowX,column=columnX)
        return Lab
