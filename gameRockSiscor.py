import tkinter as tk
from random import randint
score=scoreM=0
choice=choiceM=0
Statement = " choisir une boutton pour jouer !" 
game= tk.Tk()
def CalculateScore(j,m):
    global score , scoreM , Label4 ,  Label6
    if j!=m:
        if j==2 and m==1 or j==1 and m==0 or j==0 and m==2 :
            score+=1
        else:
            scoreM+=1
    Label4.configure(text=str(score))
    Label6.configure(text=str(scoreM))
    
    
def ChoosePaper():
    global choice ,choiceM, Label7, Label9
    choice=1
    Label7.configure(image=paper)
    choiceM=randint(0,3)
    if choiceM == 0:
        Label9.configure(image=rock)
    elif choiceM == 1:
        Label9.configure(image=paper)
    elif choiceM == 2:
        Label9.configure(image=scissors)
    CalculateScore(choice ,  choiceM)
def ChooseRock():
    global choice ,choiceM, Label7, Label9
    choice=0
    Label7.configure(image=rock)
    choiceM=randint(0,3)
    if choiceM == 0:
        Label9.configure(image=rock)
    elif choiceM == 1:
        Label9.configure(image=paper)
    elif choiceM == 2:
        Label9.configure(image=scissors)
    CalculateScore(choice ,  choiceM)
def ChooseScissors():
    global choice ,choiceM, Label7, Label9
    choice=2
    Label7.configure(image=scissors)
    choiceM=randint(0,3)
    if choiceM == 0:
        Label9.configure(image=rock)
    elif choiceM == 1:
        Label9.configure(image=paper)
    elif choiceM == 2:
        Label9.configure(image=scissors)
    CalculateScore(choice , choiceM)
    
    
    
nothing=tk.PhotoImage(file="rien.gif")
vs=tk.PhotoImage(file="versus.gif")
rock=tk.PhotoImage(file="pierre.gif")
scissors=tk.PhotoImage(file="ciseaux.gif")
paper=tk.PhotoImage(file ="papier.gif")

game.configure(background="SteelBlue2")
Label1=tk.Label(game ,text="Joueur" ,fg="Black" ,  font=("Helvetica", 12),background="SteelBlue2")
Label1.grid(row=0 , column=0)
Label3=tk.Label(game ,text="Machine" ,fg="Black" ,font=("Helvetica", 12), background="SteelBlue2")
Label3.grid(row=0 , column=2)
Label4=tk.Label(game ,text=str(score) ,fg="Black" ,font=("Helvetica", 12),background="SteelBlue2")
Label4.grid(row=1 , column=0)
Label6=tk.Label(game ,text=str(scoreM) ,fg="Black",font=("Helvetica", 12),background="SteelBlue2")
Label6.grid(row=1 , column=2)
Label7=tk.Label(game ,image=nothing,fg="Black" ,font=("Helvetica", 12),background="SteelBlue2")
Label7.grid(row=2 , column=0)
Label8=tk.Label(game ,image=vs,fg="Black" ,font=("Helvetica", 12),background="SteelBlue2")
Label8.grid(row=2 , column=1)
Label9=tk.Label(game ,image=nothing ,fg="Black",font=("Helvetica", 12),background="SteelBlue2")
Label9.grid(row=2 , column=2)
Labela=tk.Label(game ,text=Statement,fg="Black" ,font=("Helvetica", 12),background="SteelBlue2")
Labela.grid(row=3, column=0 , columnspan=3)
Button1= tk.Button(game,image=rock , command=ChooseRock)
Button1.grid(row=4,column=0)
Button2= tk.Button(game,image=paper , command=ChoosePaper)
Button2.grid(row=4,column=1)
Button3= tk.Button(game,image=scissors , command=ChooseScissors)
Button3.grid(row=4,column=2)
Button4= tk.Button(game,text="Recommencer")
Button4.grid(row=5,column=0)
Button5= tk.Button(game,text="Quitter")
Button5.grid(row=5,column=2)

#Container=tk.Label(game ,image=nothing)
game.mainloop()
