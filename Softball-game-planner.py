from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter
import pandas as pd
import Game_Algorithm 
from PIL import ImageTk, Image
from Game_Algorithm import RETURNMATCHES
from Game_Algorithm import ReturnParam



root = Tk()
root.geometry("300x300")
root.maxsize(width=700,height=400)
root.minsize(width=300, height=200)
myCanv = Canvas(root,height = 600, width = 300)
myCanv.place(x=0,y=0)   

class pos:
    x = 150;
    y = 150;

back_img = ImageTk.PhotoImage(Image.open("RHA1.png"))
back_label = Label(image=back_img)
back_label.place(x=0,y=0,relheight=1,relwidth=1)

instruction = Label(root, text = "Enter the current year:",background="black", foreground="white")
instruction.place(x=10,y=60)

global year_text
year_text = Text(root, width=12,height=1)
year_text.place(x=10,y=80)
year_text.insert(tkinter.END, "")

#myCircle = myCanv.create_oval(0,0,50,50,fill="red",width=5,outline="red") 


#def CanvResize(event):
    #myCanv.moveto(myCircle,xval/2-30,yval/2-30)

def GetFile():
    try:
        gameYear = int(year_text.get('1.0',END))
    except ValueError:
        year_text.delete(1.0,END)
        year_text.insert(tkinter.END,"ENTER YEAR FIRST")
        return 0
    filename = filedialog.askopenfilename(filetypes=(("xlsx file","*.xlsx"),("xlsx file","*.xlsx")))
    myfile = pd.read_excel(filename)
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
    global eval
    eval = RETURNMATCHES(tList,lList,TimeOne,TimeTwo,gameYear)
    showDebugButton()

def showDebugButton():
    DebugInfoB.place(x=200,y=20)

def showDebugInfo():
    top = Toplevel(root)
    top.geometry("300x140")
    top.title("Debug Info")
    top.configure(background="#1C327D")
    outputstr = "Is sucessful: "+ str(eval.success)+"\n"+ "games not played: " + str(eval.NotPlayedGames)+"\n" + "Consecutive Games: " + str(eval.ConSecGame)+"\n"
    outputstr += "Magnitude of Error: "+str(eval.MagError)+"\n"+ "Overall Rating: " +str(eval.rating)+"\n"+ "Fatal Error: "+str(eval.FatalError)
    debugLabel = Label(top,text = outputstr, anchor='w', wraplength=280, bg="#1C327D", fg="white")
    debugLabel.pack(side = TOP)
    DebugInfoB.place_forget()


global DebugInfoB
DebugInfoB = Button(root,text = "debug Info", command = showDebugInfo)

FileButton = Button(root,text="Get File",font=("Helvetica",10),command=GetFile, bg="#D3D3D3",padx = 30, pady = 10)
#myCanv.bind("<Configure>",CanvResize)
FileButton.place(x=10,y=10)
ExitButton = Button(root,text = "EXIT", command = root.quit,bg="#D3D3D3",padx = 20, pady = 5)
ExitButton.pack(side=BOTTOM)
root.mainloop()