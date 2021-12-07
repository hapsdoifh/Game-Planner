import math
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

def RETURNMATCHES(Input1, Input2,TimeOne,TimeTwo):
    ListTeams = Input1
    ListLocations = Input2
    TeamNumbers =[]
    FGames = []
    LocationCountPerTeam = []
    ListWeeks = []
    def TeamToNumber(team):
        for index,item in enumerate(ListTeams):
            if item == team:
                return index
    for o in range(len(ListTeams)):
        LocationCountPerTeam.append([0,0,0,0])
    for i in range(len(ListTeams)):
        TeamNumbers.append(i)
    PossibleGames = []
    
    for index,x in enumerate(ListTeams):
        for ind, team in enumerate(ListTeams):
            if not(ind<=index):
                PossibleGames.append([ListTeams[index],team])
    GamesPlayedPerTeam = []
    for l in ListTeams:
        GamesPlayedPerTeam.append(0)
    for i in range(math.ceil(len(PossibleGames)/8)):
        ListWeeks.append(f"Week{i+1}")
    print(len(PossibleGames))
    g=0
    while len(PossibleGames)>0:
        smallest = 1000
        for index, match in enumerate(PossibleGames):
            if GamesPlayedPerTeam[TeamToNumber(match[0])] + GamesPlayedPerTeam[TeamToNumber(match[1])]  < smallest:
                smallest =  GamesPlayedPerTeam[TeamToNumber(match[0])] +  GamesPlayedPerTeam[TeamToNumber(match[1])]
                indexstore = index
            BestMatch = PossibleGames[indexstore]
        FGames.append(BestMatch)
        g+=1
        GamesPlayedPerTeam[TeamToNumber(BestMatch[0])]+=1
        GamesPlayedPerTeam[TeamToNumber(BestMatch[1])]+=1
        PossibleGames.remove(BestMatch)
        
    print(g)
    Taken = []
    for match in FGames:
        tiniest = 1000
        
        for index,location in enumerate(ListLocations):
            if LocationCountPerTeam[TeamToNumber(match[0])][index] + LocationCountPerTeam[TeamToNumber(match[1])][index] < tiniest and location not in Taken:
                tiniest = LocationCountPerTeam[TeamToNumber(match[0])][index] + LocationCountPerTeam[TeamToNumber(match[1])][index]
                locationbest = location
                inndex = index
        LocationCountPerTeam[TeamToNumber(match[0])][inndex] +=1
        LocationCountPerTeam[TeamToNumber(match[1])][inndex] +=1
        match.append(locationbest)
        Taken.append(locationbest)
        if len(Taken) == 4:
            Taken = []
    print(FGames)
    ExcelList = []
    RowList = []
    if input("Display Organized? (y)") == "y":
        for index, match in enumerate(FGames):
            if index%8 == 0:
                ExcelList.append(['','','','',''])
                print(ListWeeks[int(index/8)])
                print(TimeOne)
                ExcelList.append([ListWeeks[int(index/8)],'','','',''])
                ExcelList.append([TimeOne,'','','',''])
            elif index%4 ==0:
                print(TimeTwo)
                ExcelList.append([TimeTwo,'','','',''])
            print(match)          
            ExcelList.append([match[0],'vs',match[1], 'at', match[2]])
    
    df = pd.DataFrame(data=ExcelList)
    df.to_excel("OUTPUT.xlsx",sheet_name= "test")


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
RETURNMATCHES(tList,lList,TimeOne,TimeTwo)
