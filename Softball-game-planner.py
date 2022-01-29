 
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter
from turtle import back, right, width
from typing import Sized
import pandas as pd
import Game_Algorithm 
from PIL import ImageTk, Image
from Game_Algorithm import IniFindMatches
from Game_Algorithm import ReturnParam

root = Tk()
root.geometry("500x300")
# root.maxsize(width=700,height=400)
# root.minsize(width=300, height=200)
# myCanv = Canvas(root,height = root.winfo_screenwidth(), width = root.winfo_screenheight())
# myCanv.place(x=0,y=0)   


class pos:
    x = 150;
    y = 150;



#myCircle = myCanv.create_oval(0,0,50,50,fill="red",width=5,outline="red") 

bkimg= Image.open(".\ProgramFiles\RHA1.png")
bkimgcpy = bkimg.copy()
bkimg = bkimg.resize((root.winfo_width(),root.winfo_height()), Image.ANTIALIAS)
back_img = ImageTk.PhotoImage(bkimg)
#back_img = ImageTk.PhotoImage(Image.open(".\ProgramFiles\RHA1.png"))
back_label = tkinter.Label(root, image=back_img)
back_label.pack(fill=BOTH, expand=YES)

global year_text
year_text = Text(root, width=12,height=1, bd=0)
year_text.place(x=10,y=80)
year_text.insert(tkinter.END, "")
instruction = Label(root, text = "Enter the current year:",background="black", foreground="white")
instruction.place(x=200,y=80)


def Resize(event): 
    global winx
    global winy
    winx=root.winfo_width()
    winy=root.winfo_height()
    newimg = bkimgcpy.resize((root.winfo_width(),root.winfo_height()))
    photoimg = ImageTk.PhotoImage(newimg)
    back_label.configure(image=photoimg)
    back_label.image = photoimg
    ExitButton.place(x=winx/2-30, y=winy-60)
    FileButton.place(x=winx/2-30, y=30)
    year_text.place(x=winx/2-35, y=100)
    instruction.place(x=winx/2-50,y=80)
back_label.bind("<Configure>",Resize)

def GetFile():
    try:
        gameYear = int(year_text.get('1.0',END))
    except ValueError:
        year_text.delete(1.0,END)
        year_text.insert(tkinter.END,"ENTER YEAR FIRST")
        return 0
    filename = filedialog.askopenfilename(filetypes=(("xlsx file","*.xlsx"),("xlsx file","*.xlsx")))
    myfile = pd.read_excel(filename)
    ConvertedFile = myfile.to_numpy()
    lList=[]
    tList=[]
    timeSlotList = []
    for x in range(3):
        for y in range(len(ConvertedFile)):
            if not pd.isnull(ConvertedFile[y][x]):
                if x == 0:
                    tList.append(str(ConvertedFile[y][x]))
                elif x==1:
                    lList.append(str(ConvertedFile[y][x]))
                else:
                    timeSlotList.append(str(ConvertedFile[y][x]))
            else:
                break
    global eval
    eval = IniFindMatches(tList,lList,timeSlotList[0],timeSlotList[1],gameYear)
    showDebugButton()

def showDebugButton():
    DebugInfoB.place(x=winx/2-30,y=180)

def showDebugInfo():
    top = Toplevel(root)
    top.geometry("300x140")
    top.title("Debug Info")
    top.configure(background="#1C327D")
    outputstr = "Is sucessful: "+ str(eval.success)+"\n"+ "games not played: " + str(eval.NotPlayedGames)+"\n" + "Consecutive Games: " + str(eval.ConSecGame)+"\n"
    outputstr += "Magnitude of Error: "+str(eval.MagError)+"\n"+ "Overall Rating: " +str(eval.rating)+"\n"+ "Fatal Error: "+str(eval.FatalError)+"\nDuplicated games: " + str(eval.Dgames)
    debugLabel = Label(top,text = outputstr, anchor='w', wraplength=280, bg="#1C327D", fg="white")
    debugLabel.pack(side=TOP)
    DebugInfoB.place_forget()

# def Resize(event):
#     print(event.height)
#     print(event.width)
#     print()
# root.bind("<Configure>",Resize)

global DebugInfoB
img= (Image.open(".\ProgramFiles\DebugInfo.png"))
img = img.resize((83,50), Image.ANTIALIAS)
dbgInfo = ImageTk.PhotoImage(img)
DebugInfoB = Button(root,text = "debug Info",image=dbgInfo, command = showDebugInfo,background="black", activebackground="black", bd=0)

img= (Image.open(".\ProgramFiles\Exit.png"))
img = img.resize((83,50), Image.ANTIALIAS)
ExitImg =ImageTk.PhotoImage(img)

img= (Image.open(".\ProgramFiles\FileButton.png"))
img = img.resize((83,50), Image.ANTIALIAS)
FileBImage = ImageTk.PhotoImage(img)
FileButton = Button(root,image=FileBImage,command=GetFile,borderwidth=0,bd = 0, background="black", activebackground="black")
FileButton.place(x=200,y=20)

img= (Image.open(".\ProgramFiles\Exit.png"))
img = img.resize((83,50), Image.ANTIALIAS)
ExitImg =ImageTk.PhotoImage(img)
ExitButton = Button(root,text = "EXIT", command = root.quit,background="black",borderwidth=0,bd = 0,image=ExitImg, activebackground="black")
ExitButton.place(x=200,y=300)



root.mainloop()