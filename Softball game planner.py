from tkinter import *
from tkinter import ttk
from typing import DefaultDict
import numpy
import pandas as pd
from pandas.io import excel


def RETURNMATCHES(INPUT1,INPUT2,T1,T2):
    LISTTEAMS = INPUT1
    LOCATIONLIST = INPUT2
    def RETURNPOSSIBLEMATCHES(LISTTEAMS,LOCATIONCOUNTPERTEAM):
        TEAMNUMBER =[]
        for i in range(len(LISTTEAMS)):
            TEAMNUMBER.append(i+1)
        returnlist = []
        for index,x in enumerate(LISTTEAMS):
            for ind, team in enumerate(LISTTEAMS):
                if not(ind<=index):
                    returnlist.append([LISTTEAMS[index],team])
        return returnlist
    def TEAMTONUMBER (team):
        for index,thing in enumerate(LISTTEAMS):
            if team == thing:
                return index
    LOCATIONCOUNTPERTEAM = []
    for i in range(len(LISTTEAMS)):
        LOCATIONCOUNTPERTEAM.append([0,0,0,0])
    POSSIBLEGAMES = RETURNPOSSIBLEMATCHES(LISTTEAMS,LOCATIONCOUNTPERTEAM)
    PLAYING = []
    FGAMES = []
    while len(POSSIBLEGAMES)>0:
        for game in POSSIBLEGAMES:
            if game[0] in PLAYING or game[1] in PLAYING:
                continue
            elif len(PLAYING)!=8:
                PLAYING.append(game[0])
                PLAYING.append(game[1])
                FGAMES.append([game[0],game[1]])
            else:
                continue
        PLAYING = []
        POSSIBLEGAMES.reverse()
        
        for finalized_game in FGAMES:
            if finalized_game in POSSIBLEGAMES:
                POSSIBLEGAMES.remove(finalized_game)
    TIMEARRAY = []
    FFGAMES = []

    try:
        for i in range(0,len(FGAMES),4):
            if len(LISTTEAMS)>=8:
                for k in range(4):
                    TIMEARRAY.append(FGAMES[i+k])
                FFGAMES.append(TIMEARRAY)
                TIMEARRAY = []
            else:
                for m in range(len(LISTTEAMS)//2):
                    TIMEARRAY.append(FGAMES[i+m])
                FFGAMES.append(TIMEARRAY)
                TIMEARRAY = []
        TIMEARRAY = []
    except IndexError:
        for o in range(4):
            if FGAMES[-(o+1)] not in FFGAMES[-1]:
                TIMEARRAY.append(FGAMES[-(o+1)])
        FFGAMES.append(TIMEARRAY)
        TIMEARRAY = []
        for i in range (int(len(FFGAMES[-1])/2)):
            FFGAMES[-1].pop(-1)

    for i in range(len(FFGAMES)):
        pplay = []
        for ind,game in enumerate(FFGAMES[i]):
            smallest = 100
            
            for k in range(4):
                if LOCATIONCOUNTPERTEAM[TEAMTONUMBER(game[0])][k]+LOCATIONCOUNTPERTEAM[TEAMTONUMBER(game[1])][k]<smallest and (k not in pplay):
                    smallest = LOCATIONCOUNTPERTEAM[TEAMTONUMBER(game[0])][k]+LOCATIONCOUNTPERTEAM[TEAMTONUMBER(game[1])][k]
                    smallestindex = k
            pplay.append(smallestindex)
            FFGAMES[i][ind].append(LOCATIONLIST[smallestindex])
            LOCATIONCOUNTPERTEAM[TEAMTONUMBER(game[0])][smallestindex]+=1
            LOCATIONCOUNTPERTEAM[TEAMTONUMBER(game[1])][smallestindex]+=1
    for indd,time in enumerate(FFGAMES):
        FFGAMES[indd].append(f"{indd+1}")
    print(FFGAMES)

    indl = 1
    TTLIST = []
    DAYSLIST = []
    for day in range(len(FFGAMES)):
        if (day+1)%2==0:
            DAYSLIST.append((f"Day {indl}"))
            indl+=1
    DAYSLIST.append((f"Day {indl}"))
    ExcelList = []
    RowList = []
    for q in range(len(DAYSLIST)):
        TTLIST.append(T1)
        TTLIST.append(T2)
    for inddd,timegroup in enumerate(FFGAMES):
        if inddd%2==0:
            print(DAYSLIST[int(inddd/2)])
            ExcelList.append(['','','','',''])
            ExcelList.append([DAYSLIST[int(inddd/2)],'','','',''])
        print(TTLIST[inddd])
        for indor,match in enumerate(timegroup):
            if isinstance(match, list):
                ExcelList.append([FFGAMES[inddd][indor][0],'vs',FFGAMES[inddd][indor][1],'at',FFGAMES[inddd][indor][2]])
                print(FFGAMES[inddd][indor])
    df = pd.DataFrame(data=ExcelList)
    df.to_excel("OUTPUT.xlsx",sheet_name= "test")
    print()

#INPUTS
TeamList = [
    "Team One",
    "Team Two",
    "Team Three",
    "Team Four",
    "Team Five",
    "Team Six",
    "Team Seven",
    "Team Eight",
    
]
LocationList = [
    "Location One",
    "Location Two",
    "Location Three",
    "Location Four",
]
TimeOne = "3 pm"
TimeTwo = "7 pm"

mytest = pd.read_excel("Book1.xlsx")
other = mytest.to_numpy()
lList=[]
tList=[]

for x in range(2):
    for y in range(len(other)):
        if(other[y][x] != numpy.nan):
            if x == 0:
                tList.append(str(other[y][x]))
            else:
                lList.append(str(other[y][x]))
        else:
            break
RETURNMATCHES(tList,lList,TimeOne,TimeTwo)

