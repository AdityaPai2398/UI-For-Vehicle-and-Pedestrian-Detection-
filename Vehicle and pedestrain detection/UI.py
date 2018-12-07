#import module from tkinter for UI
from tkinter import *
import os
from datetime import datetime;
#creating instance of TK
root=Tk()

root.configure(background="black")

#root.geometry("300x300")

def function1():
    
    os.system("py car.py")
    
def function2():
    
    os.system("py bike.py")

def function3():

    os.system("py pedestrian.py")

def function4():

    os.system("py bus.py")
    
 
def function6():

    root.destroy()

#stting title for the window
root.title("Detections")

#creating a text label
Label(root, text="Vechicle and Pedestrain Detection Using Haar Cascades",font=("times new roman",20),fg="white",bg="black",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Label(root, text="Checkout link in Description to build your own Haar Cascades",font=("times new roman",15),fg="white",bg="black",height=2).grid(row=2,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Car Detecton",font=("times new roman",20),bg="#000000",fg='green',command=function1).grid(row=4,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Bike Detection",font=("times new roman",20),bg="#000000",fg='green',command=function2).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Pedestrian Detection",font=('times new roman',20),bg="#000000",fg="green",command=function3).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Bus Detection",font=('times new roman',20),bg="#000000",fg="green",command=function4).grid(row=7,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',20),bg="black",fg="red",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
