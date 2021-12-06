from tkinter import *
from tkinter import ttk
import pandas as pd

df = pd.read_excel('Book1.xlsx')
df.head()
print(df.shape)

root = Tk()
root.geometry("300x300")
myCanv = Canvas(root,height = 1080, width = 1920)
myCanv.pack()
global myl
myl = Label(root,text="temp")
myl.place(x=10,y=60)   
mylb = Label(root,text="temp")
mylb.place(x=10,y=40) 
myCircle = myCanv.create_oval(0,0,50,50,fill="red",width=5,outline="red") 

myCanv.move(myCircle,30,30)
myCanv.move(myCircle,30,30)
myCanv.move(myCircle,30,30)
def CanvResize(event):
    xval = event.width
    yval = event.height
   #myl.configure(text = str(xval))
    myl.configure(text = df)
    mylb.configure(text = str(yval))
    myCanv.moveto(myCircle,xval/2-30,yval/2-30)
    
def DestroyCanv():
    myCanv.delete("all")
    
desbutton = Button(root,text="destroy",command=DestroyCanv)
myCanv.bind("<Configure>",CanvResize)
desbutton.place(x=10,y=10)

root.mainloop()