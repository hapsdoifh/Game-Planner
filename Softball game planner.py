from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pandas as pd


root = Tk()
root.geometry("300x300")

myCanv = Canvas(root,height = 1000, width = 1000)
myCanv.pack()   
mylb = Label(root,text="temp")
mylb.place(x=10,y=40) 
myCircle = myCanv.create_oval(0,0,50,50,fill="red",width=5,outline="red") 

global myl
myl = Label(root,text="myfile")

def CanvResize(event):
    xval = event.width
    yval = event.height
    mylb.configure(text = str(yval))
    myl.place(x=xval/2-100,y=yval/2-100)
    myCanv.moveto(myCircle,xval/2-30,yval/2-30)
    
def GetFile():
    filename = filedialog.askopenfilename(filetypes=(("xlsx file","*.xlsx"),("xlsx file","*.xlsx")))
    myfile = pd.read_excel(filename)
    myl.configure(text = myfile)
    print(myfile)

    
desbutton = Button(root,text="Get File",command=GetFile)
myCanv.bind("<Configure>",CanvResize)
desbutton.place(x=10,y=10)

root.mainloop()