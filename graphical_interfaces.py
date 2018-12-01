# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 19:36:13 2018

@author: mellisos
"""

#graphic interface

from tkinter import *

root=Tk()
root.title("Monty Python")

myname=StringVar()

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


squaretext=Entry(myFrame)
squaretext.grid(row=3, column=1)
squaretext.config(fg="blue", justify="center", show="*")

nameLabel=Label(myFrame, text="Password: ")
nameLabel.grid(row=3, column=0, sticky ="e", padx=5 , pady=5)


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


