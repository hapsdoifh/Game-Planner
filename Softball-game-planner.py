from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import Game_Algorithm 
from Game_Algorithm import RETURNMATCHES


root = Tk()
root.geometry("300x300")

myCanv = Canvas(root,height = 1000, width = 1000)
myCanv.pack()   
mylb = Label(root,text="temp")
mylb.place(x=10,y=40) 
#myCircle = myCanv.create_oval(0,0,50,50,fill="red",width=5,outline="red") 


def CanvResize(event):
    xval = event.width
    yval = event.height
    mylb.configure(text = str(yval))
    #myCanv.moveto(myCircle,xval/2-30,yval/2-30)
    
def GetFile():
    filename = filedialog.askopenfilename(filetypes=(("xlsx file","*.xlsx"),("xlsx file","*.xlsx")))
    myfile = pd.read_excel(filename)
    print(myfile)
    TimeOne = "3 pm"
    TimeTwo = "7 pm"
    mytest = pd.read_excel("Book1.xlsx")
    other = mytest.to_numpy()
    lList=[]
    tList=[]

    for x in range(2):
        for y in range(len(other)):
            if not pd.isnull(other[y][x]):
                if x == 0:
                    tList.append(str(other[y][x]))
                else:
                    lList.append(str(other[y][x]))
            else:
                break
    print(tList)
    print(lList)
    RETURNMATCHES(tList,lList,TimeOne,TimeTwo)

    
desbutton = Button(root,text="Get File",command=GetFile)
myCanv.bind("<Configure>",CanvResize)
desbutton.place(x=10,y=10)

root.mainloop()