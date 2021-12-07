#This function given an input for the teams and an input for the locations will output a list that has the optimal game order with the most unique locations.
#It sorts it in a priority as:
'''
!!! Courts occupied
!! Unique team
! Unique location
'''

from tkinter import *
from tkinter import ttk
from typing import DefaultDict
import numpy
import pandas as pd
from pandas.io import excel
import numpy



def RETURNMATCHES(INPUT1,INPUT2,T1,T2):
    #Sets the list of the teams as the first input
    LISTTEAMS = INPUT1
    #Sets the list of the locations as the second input
    LOCATIONLIST = INPUT2
    #Given the list of teams, this function returns every possible game as a 2d list.
    def RETURNPOSSIBLEMATCHES(LISTTEAMS):
        TEAMNUMBER =[]
        for i in range(len(LISTTEAMS)):
            TEAMNUMBER.append(i+1)
        returnlist = []
        for index,x in enumerate(LISTTEAMS):
            for ind, team in enumerate(LISTTEAMS):
                if not(ind<=index):
                    returnlist.append([LISTTEAMS[index],team])
        return returnlist
    #this function returns a given team to an index on the list of teams
    def TEAMTONUMBER (team):
        for index,thing in enumerate(LISTTEAMS):
            if team == thing:
                return index
    #Gives each team a location count of [0,0,0,0] with each 0 being a separate location.
    LOCATIONCOUNTPERTEAM = []
    for i in range(len(LISTTEAMS)):
        LOCATIONCOUNTPERTEAM.append([0,0,0,0])
    #sets POSSIBLEGAMES to the 2d list with all possible games
    POSSIBLEGAMES = RETURNPOSSIBLEMATCHES(LISTTEAMS)
    #currently playing
    PLAYING = []
    #Final Games
    FGAMES = []
    #For each match in possible games, as long as the teams arent playing, it will append that match to final games and set each team to be playing.
    
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
    
        # for each game in the sorted list, remove it from possible games.
        for finalized_game in FGAMES:
            if finalized_game in POSSIBLEGAMES:
                POSSIBLEGAMES.remove(finalized_game)
    TIMEARRAY = []
    FFGAMES = []
    
    # In the end, FGAMES will be a sorted list with the order of the games so there cannot be multiple teams playing at once
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
    
    indl = 1
    TTLIST = []
    DAYSLIST = []
    g=0
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
        ExcelList.append([TTLIST[inddd],'','','',''])
        for indor,match in enumerate(timegroup):
            if isinstance(match, list):
                print(FFGAMES[inddd][indor])
                ExcelList.append([FFGAMES[inddd][indor][0],'vs',FFGAMES[inddd][indor][1],'at',FFGAMES[inddd][indor][2]])
                g+=1
    if len(RETURNPOSSIBLEMATCHES(LISTTEAMS)) != g:
        print("ERROR!! FOR SOME REASON THERE ISNT THE MAX AMOUNT OF GAMES")
        exit()
    df = pd.DataFrame(data=ExcelList)
    df.to_excel("OUTPUT.xlsx",sheet_name= "test")


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
    "Team Nine",
    "Team Ten",
    "Team Eleven",
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
        if not pd.isnull(other[y][x]):
            if x == 0:
                tList.append(str(other[y][x]))
            else:
                lList.append(str(other[y][x]))
        else:
            break
RETURNMATCHES(TeamList,LocationList,TimeOne,TimeTwo)

print(tList)
print(lList)
print(TeamList)
print(LocationList)