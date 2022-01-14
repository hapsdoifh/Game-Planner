from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter
from typing import Sized
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

back_img = ImageTk.PhotoImage(Image.open(".\ProgramFiles\RHA1.png"))
back_label = Label(image=back_img)
back_label.place(x=0,y=0,relheight=1,relwidth=1)
root.configure(background="blue")

instruction = Label(root, text = "Enter the current year:",background="black", foreground="white")
instruction.place(x=10,y=60)

global year_text
year_text = Text(root, width=12,height=1, bd=0)
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
    #mytest = pd.read_excel("Book1.xlsx")
    other = myfile.to_numpy()
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

# def Resize(event):
#     print(event.height)
#     print(event.width)
#     print()
# root.bind("<Configure>",Resize)

global DebugInfoB
img= (Image.open(".\ProgramFiles\FileButton.png"))
img = img.resize((83,50), Image.ANTIALIAS)
FileBImage = ImageTk.PhotoImage(img)
DebugInfoB = Button(root,text = "debug Info", command = showDebugInfo)

img= (Image.open(".\ProgramFiles\FileButton.png"))
img = img.resize((83,50), Image.ANTIALIAS)
FileBImage = ImageTk.PhotoImage(img)
#FileBImage = PhotoImage(file=".\ProgramFiles\FileButton.png")
FileButton = Button(root,image=FileBImage,command=GetFile,borderwidth=0,bd = 0, background="black", activebackground="black")
#FileButton.place(x=10,y=10)
FileButton.pack(side="top")

img= (Image.open(".\ProgramFiles\Exit.png"))
img = img.resize((83,50), Image.ANTIALIAS)
ExitImg =ImageTk.PhotoImage(img)
ExitButton = Button(root,text = "EXIT", command = root.quit,background="black",borderwidth=0,bd = 0,image=ExitImg, activebackground="black")
ExitButton.pack(side="bottom")



root.mainloop()