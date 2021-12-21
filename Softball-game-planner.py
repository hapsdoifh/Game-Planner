from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter
import pandas as pd
import Game_Algorithm 
from PIL import ImageTk, Image
from Game_Algorithm import RETURNMATCHES


root = Tk()
root.geometry("300x300")
root.maxsize(width=700,height=400)
root.minsize(width=300, height=200)
myCanv = Canvas(root,height = 1000, width = 1000)
myCanv.place(x=0,y=0)   

back_img = ImageTk.PhotoImage(Image.open("RHA1.png"))
back_label = Label(image=back_img)
back_label.place(x=0,y=0,relheight=1,relwidth=1)

global year_text
year_text = Text(root, width=12,height=1)
year_text.place(x=10,y=80)
year_text.insert(tkinter.END, "Enter year of games")
#myCircle = myCanv.create_oval(0,0,50,50,fill="red",width=5,outline="red") 

    

def CanvResize(event):
    xval = event.width
    yval = event.height
    #myCanv.moveto(myCircle,xval/2-30,yval/2-30)


def GetFile():
    try:
        gameYear = int(year_text.get('1.0',END))
    except ValueError:
        print("NOO")
        year_text.delete(1.0,END)
        year_text.insert(tkinter.END,"ENTER YEAR FIRST")
        return 0
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
    RETURNMATCHES(tList,lList,TimeOne,TimeTwo,gameYear)

    
FileButton = Button(root,text="Get File",font=("Helvetica",10),command=GetFile, bg="#D3D3D3",padx = 30, pady = 10)
myCanv.bind("<Configure>",CanvResize)
FileButton.place(x=10,y=10)
ExitButton = Button(root,text = "EXIT", command = root.quit,bg="#D3D3D3",padx = 20, pady = 5)
ExitButton.pack(side=BOTTOM)
root.mainloop()