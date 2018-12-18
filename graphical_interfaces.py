# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 19:36:13 2018

@author: mellisos
"""

#graphic interface

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root=Tk()
root.title("Monty Python")

varRadio=IntVar()
myname=StringVar()
internet=IntVar()
TV=IntVar()
cellphone=IntVar()
telephon=IntVar()



barMenu=Menu(root)
root.config(menu=barMenu)

def infoProgram():
    
    messagebox.showinfo("Program info","Version 3.6.2 \n Copyright 2018")
    
    
def saveProgram():
    
    v = messagebox.askquestion("Save","Do you want to save this file?")

    
def closeProgram():
    
    va = messagebox.askokcancel("Quit","Do you want to exit this program?")

    if va==True:
        root.destroy()


def openFile():
    files=filedialog.askopenfilename(title="open", initialdir="C:/", filetypes=(("Text files","*.txt"),("Excel files",",xlsx"),
                                                                                ("All files","*.*")))
    print(files)
    
Button(root, text="Open File", command=openFile).pack()


fileMenu=Menu(barMenu, tearoff=0)
fileMenu.add_command(label="New file")
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveProgram)
fileMenu.add_command(label="Save as...")
fileMenu.add_separator()
fileMenu.add_command(label="Print")
fileMenu.add_separator()
fileMenu.add_command(label="Restart")
fileMenu.add_command(label="Quit", command=closeProgram)


fileEdit=Menu(barMenu, tearoff=0)
fileEdit.add_command(label="Copy")
fileEdit.add_command(label="Cut")
fileEdit.add_command(label="Paste")
fileEdit.add_command(label="Select All")


fileTools=Menu(barMenu, tearoff=0)
fileTools.add_command(label="Preferences")

    
fileHelp=Menu(barMenu, tearoff=0)
fileHelp.add_command(label="About this program...", command=infoProgram)

barMenu.add_cascade(label="File",menu=fileMenu)
barMenu.add_cascade(label="Edit",menu=fileEdit)
barMenu.add_cascade(label="Tools",menu=fileTools)
barMenu.add_cascade(label="Help",menu=fileHelp)


root.resizable(True,True)
root.geometry("1000x800")
root.config(bg="skyblue")

myFrame=Frame()
myFrame.pack(fill="y", expand="True",side="left", anchor="n")
myFrame.config(bg="blue",width="600", height="500", cursor="hand2")

#myImagen=PhotoImage(file="python_image.png")

Label(myFrame, text="Hello python!", fg="green", font=(40)).place(x=250,y=250)

squaretext=Entry(myFrame, textvariable=myname)
squaretext.grid(row=0, column=1)
squaretext.config(fg="blue", justify="center")

nameLabel=Label(myFrame, text="Name: ")
nameLabel.grid(row=0, column=0, sticky ="e", padx=5 , pady=5)


squaretext=Entry(myFrame)
squaretext.grid(row=0, column=3)
squaretext.config(fg="blue", justify="center")

nameLabel=Label(myFrame, text="Surname: ")
nameLabel.grid(row=0, column=2, sticky ="e", padx=5 , pady=5)


squaretext=Entry(myFrame)
squaretext.grid(row=1, column=1)
squaretext.config(fg="blue", justify="center")

nameLabel=Label(myFrame, text="Address: ")
nameLabel.grid(row=1, column=0, sticky ="e", padx=5 , pady=5)


squaretext=Entry(myFrame)
squaretext.grid(row=1, column=3)
squaretext.config(fg="blue", justify="center")

nameLabel=Label(myFrame, text="Dept.: ")
nameLabel.grid(row=1, column=2, sticky ="e", padx=5 , pady=5)


squaretext=Entry(myFrame)
squaretext.grid(row=2, column=1)
squaretext.config(fg="blue", justify="center")

nameLabel=Label(myFrame, text="Handy number: ")
nameLabel.grid(row=2, column=0, sticky ="e", padx=5 , pady=5)


squaretext=Entry(myFrame)
squaretext.grid(row=3, column=1)
squaretext.config(fg="blue", justify="center")

nameLabel=Label(myFrame, text="E-mail: ")
nameLabel.grid(row=3, column=0, sticky ="e", padx=5 , pady=5)


def chooseMedia():
    
    chooseSelected=""
    
    if(TV.get()==1):
        chooseSelected+=" TV"
        
    if(internet.get()==1):
        chooseSelected+=" Internet"
    
    if(cellphone.get()==1):
        chooseSelected+=" Cellphone"

    if(telephon.get()==1):
        chooseSelected+=" Telephon"

    textEnd.config(text=chooseSelected)
    
frame=Frame(root)
frame.pack()

Label(frame, text="choose destine", width=40).pack()

Checkbutton(frame, text="TV", variable=TV, onvalue=1,offvalue=0, command=chooseMedia).pack()
Checkbutton(frame, text="Internet", variable=internet, onvalue=1,offvalue=0, command=chooseMedia).pack()
Checkbutton(frame, text="Cellphone", variable=cellphone, onvalue=1,offvalue=0, command=chooseMedia).pack()
Checkbutton(frame, text="Telephon", variable=telephon, onvalue=1,offvalue=0, command=chooseMedia).pack()

textEnd=Label(frame)
textEnd.pack()

#foto=PhotoImage(file="backtothefuture_display.png")
#Label(root,image=foto).pack()



squaretext=Entry(myFrame)
squaretext.grid(row=3, column=1)
squaretext.config(fg="blue", justify="center", show="*")

nameLabel=Label(myFrame, text="Password: ")
nameLabel.grid(row=3, column=0, sticky ="e", padx=5 , pady=5)

def printer():
    
    #print(varRadio.get())
    
    if varRadio.get()==1:
        ticket.config(text="You have chosen male")
        
    else:
        ticket.config(text="You have chosen female")


Label(root, text="Gender").pack()

Radiobutton(root, text="male", variable=varRadio, value=1, command=printer).pack()
Radiobutton(root, text="female", variable=varRadio, value=2, command=printer).pack()

ticket=Label(root)
ticket.pack()

commentarytext=Text(myFrame, width=40, height=10)
commentarytext.grid(row=4 ,column=1)


scrollVertical=Scrollbar(myFrame, command=commentarytext.yview)
scrollVertical.grid(row=4,column=2,sticky="nsew")

commentarytext.config(yscrollcommand=scrollVertical.set)

commentaryLabel=Label(myFrame,text="Commentary: ")
commentaryLabel.grid(row=4 , column=0, sticky="e", padx=5, pady=5)

def codeButton():
    
    myname.set("Andres")

send=Button(root, text="Send", command=codeButton)
send.pack()

root.mainloop()


