#This function given an input for the teams and an input for the locations will output a list that has the optimal game order with the most unique locations.
#It sorts it in a priority as:
'''
!!! Unique team
!!! Unique location
!! Courts Taken
No thought is given to diverse playing time
    '''
from copy import deepcopy
import time
from typing import DefaultDict
import numpy
import pandas as pd
from pandas.io import excel
import numpy

class ReturnParam:
    def __init__(self, Success, ErrList, MagError, CscGame, rating, FERROR, DGames):
        self.success = Success
        self.NotPlayedGames = ErrList
        self.ConSecGame = CscGame
        self.MagError = MagError
        self.rating = rating
        self.Dgames = DGames
        self.FatalError = FERROR

from copy import deepcopy
def IniFindMatches(i1,i2,TimeOne, TimeTwo,gameYear):
    ListTeams = i1
    ListLocations = i2
    
    PossibleGames = []
    ListWeeks = []
    FGames = []
    PrevGames = []
    GamesPlayedPerTeam = []
    LocationCountPerTeam=[]
    for ele in ListTeams:
        GamesPlayedPerTeam.append(0)
        LocationCountPerTeam.append([1,1,1,1])
    for index,x in enumerate(ListTeams):
       for ind, team in enumerate(ListTeams):
           if not(ind<=index):
               PossibleGames.append([ListTeams[index],team])
    x=1
    def listToString(s):
        str1 = ""
        for ele in s:
            str1 += (f"{ele} ")
        return str1
    def LocationToIndex(Location):
        for indor,loc in enumerate(ListLocations):
            if loc == Location:
                return indor
    from datetime import date
    year = gameYear
    for i in range(3):
        x=1
        for k in range(30+(i+5)%2):
            dateasy = str(date(year,5+i,x).ctime())
            listm = dateasy.split(" ")
            if listm[0] == "Wed":
                if str((date(year,5,x).ctime())).split(" ")[2] == '':
                    ListWeeks.append(listToString(str((date(year,5+i,x).ctime())).split(" ")[1:4]))
                else:
                    ListWeeks.append(listToString(str((date(year,5+i,x).ctime())).split(" ")[1:3]))
            x+=1
        x=1
    x=1
    for k in range(31):
            dateasy = str(date(year,8,x).ctime())
            listm = dateasy.split(" ")
            if listm[0] == "Wed":
                if str((date(year,5,x).ctime())).split(" ")[2] == '':
                    ListWeeks.append(listToString(str((date(year,8,x).ctime())).split(" ")[1:4]))
                else:
                    ListWeeks.append(listToString(str((date(year,8,x).ctime())).split(" ")[1:3]))
            x+=1
        
    def TeamsInMatches(Matches):
        teamsinmatches = []
        for match in Matches:
            teamsinmatches.append(match[0])
            teamsinmatches.append(match[1])
        return set(teamsinmatches)
    def TeamToIndex(team):
        for ind,t in enumerate(ListTeams):
            if team == t:
                return ind
    for i in range(len(ListWeeks)*8):
        PossibleSelection = []
        WorsePossibleSelection = []
        BadPossibleSelection = []
        if i >= 4:
            if i%4 == 0:
                CurrGames = []
            if i%8 == 0:
                PrevGames = []
            if (i+4) %8 == 0:
                PrevGames.append(FGames[i-4])
                PrevGames.append(FGames[i-3])
                PrevGames.append(FGames[i-2])
                PrevGames.append(FGames[i-1])
        else:
            for match in PossibleGames:
                if match[0] not in TeamsInMatches(FGames) and match[1] not in TeamsInMatches(FGames):
                    FGames.append(match)
                    break
        if i>=4:
            for match in PossibleGames:
                if (match[0] not in TeamsInMatches(PrevGames) and match[1] not in TeamsInMatches(PrevGames)) and (match[0] not in TeamsInMatches(CurrGames) and match[1] not in TeamsInMatches(CurrGames)) and (match not in FGames):
                    PossibleSelection.append(match)
            if len(PossibleSelection) == 0:
                for match in PossibleGames:
                    if (match[0] not in TeamsInMatches(PrevGames) and match[1] not in TeamsInMatches(PrevGames)) and (match[0] not in TeamsInMatches(CurrGames) and match[1] not in TeamsInMatches(CurrGames)):
                        WorsePossibleSelection.append(match)
            if len(WorsePossibleSelection) == 0:
                for match in PossibleGames:
                    if match[0] not in TeamsInMatches(CurrGames):
                        BadPossibleSelection.append(match)
            if len(PossibleSelection)>0:
                Smallest = 100000
                for  element in PossibleSelection:
                    if GamesPlayedPerTeam[TeamToIndex(element[0])] + GamesPlayedPerTeam[TeamToIndex(element[1])] < Smallest:
                        Smallest = GamesPlayedPerTeam[TeamToIndex(element[0])] + GamesPlayedPerTeam[TeamToIndex(element[1])]
                        elebest = element
                FGames.append(elebest)
                GamesPlayedPerTeam[TeamToIndex(elebest[0])]+=1
                GamesPlayedPerTeam[TeamToIndex(elebest[1])]+=1
                CurrGames.append(elebest)
            elif len(WorsePossibleSelection)>0:
                Smallest = 100000
                for  element in WorsePossibleSelection:
                    if GamesPlayedPerTeam[TeamToIndex(element[0])] + GamesPlayedPerTeam[TeamToIndex(element[1])] < Smallest:
                        Smallest = GamesPlayedPerTeam[TeamToIndex(element[0])] + GamesPlayedPerTeam[TeamToIndex(element[1])]
                        elebest = element
                FGames.append(elebest)
                GamesPlayedPerTeam[TeamToIndex(elebest[0])]+=1
                GamesPlayedPerTeam[TeamToIndex(elebest[1])]+=1
                CurrGames.append(elebest)
            else:
                Smallest = 100000
                for  element in BadPossibleSelection:
                    if GamesPlayedPerTeam[TeamToIndex(element[0])] + GamesPlayedPerTeam[TeamToIndex(element[1])] < Smallest:
                        Smallest = GamesPlayedPerTeam[TeamToIndex(element[0])] + GamesPlayedPerTeam[TeamToIndex(element[1])]
                        elebest = element
                FGames.append(elebest)
                GamesPlayedPerTeam[TeamToIndex(elebest[0])]+=1
                GamesPlayedPerTeam[TeamToIndex(elebest[1])]+=1
                CurrGames.append(elebest)

    DGames = 0
    PossibleLocationIndicies = [
        [0,1,2,3],
        [0,1,3,2],
        [0,2,1,3],
        [0,2,3,1],
        [0,3,1,2],
        [0,3,2,1],
        [1,2,3,0],
        [1,2,0,3],
        [1,0,2,3],
        [1,0,3,2],
        [1,3,2,0],
        [1,3,0,2],
        [2,0,1,3],
        [2,0,3,1],
        [2,1,0,3],
        [2,1,3,0],
        [2,3,0,1],
        [2,3,1,0],
        [3,0,1,2],
        [3,0,2,1],
        [3,1,0,2],
        [3,1,2,0],
        [3,2,0,1],
        [3,2,1,0]
    ]
    def findscore(combination, inx,LocationCount):
        TotalScore = 0
        for k in range (4):
            multT1 = 1
            multT2 = 1
            for i,ele in enumerate(LocationCount[TeamToIndex(FGames[inx+k][0])]):
                if i == combination[k]:
                    multT1*=ele+1
                else:
                    multT1*=ele
            for i,ele in enumerate(LocationCount[TeamToIndex(FGames[inx+k][1])]):
                if i == combination[k]:
                    multT2*=ele+1
                else:
                    multT2*=ele
            TotalScore+=multT2
            TotalScore+=multT1
        return TotalScore
        LocationCount[TeamToIndex(FGames[inx][1])][combination[1]]
    scorelist = []
    for index, match in enumerate(FGames):
        if index%4 == 0:
            scorelist = []
            for combination in PossibleLocationIndicies:
                scorelist.append(findscore(combination,index,LocationCountPerTeam))
            larg = max(scorelist)
            for indx,score in enumerate(scorelist):
                if score == larg:
                    indexbest = indx
            for o in range(4):
                ModList = deepcopy(FGames[index+o])
                ModList.append(ListLocations[PossibleLocationIndicies[indexbest][o]])
                FGames.pop(index+o)
                FGames.insert(index+o,ModList)
            
            for f in range(4):
                LocationCountPerTeam[TeamToIndex(FGames[index+f][0])][PossibleLocationIndicies[indexbest][f]]+=1
                LocationCountPerTeam[TeamToIndex(FGames[index+f][1])][PossibleLocationIndicies[indexbest][f]]+=1
    
    ErrorList = []
    Closed = []
    for index,match in enumerate(FGames):
        if len(Closed) == 8:
            Closed = []
        if match[0] in Closed or match[1] in Closed:
            ErrorList.append(match)
        Closed.append(match[0])
        Closed.append(match[1])
    #Display for ease of use.
    #("Finished Calculating!")
    end = time.time()
    #("Time Elapsed: ", end = '')
    #(round(end - start,5),"seconds")

    ExcelList = []
    RowList = []
    LocationCountPerTeam = []
    B2BCount = 0
    count = 0

    PlayedBefore = []
    for match in FGames:
        if match[:2] in PlayedBefore:
            match.append("Duplicate")
            DGames+=1
            PlayedBefore.append(match[:2])
        else:
            PlayedBefore.append(match[:2])

    for i in range (len(ListTeams)):
        LocationCountPerTeam.append([0,0,0,0])
    for index, match in enumerate(FGames):
        if index%8 == 0: 
            if str(ListWeeks[int(index/8)]) == "Extra Week 0":
                break
            ExcelList.append(['','','','',''])
            ExcelList.append([ListWeeks[int(index/8)],'','','',''])
            ExcelList.append([TimeOne,'','','',''])
        elif index%4 ==0:
            ExcelList.append([TimeTwo,'','','',''])
        if match not in ErrorList:
            LocationCountPerTeam[TeamToIndex(match[0])][LocationToIndex(match[2])]+=1
            LocationCountPerTeam[TeamToIndex(match[1])][LocationToIndex(match[2])]+=1
            ExcelList.append([match[0],'vs',match[1], 'at', match[2]])
        else:
            pass
    df = pd.DataFrame(data=ExcelList)
    df.to_excel(".\Output-Folder\GameSchedule.xlsx",sheet_name= "Games")



    ExcelTeamGameList = []
    teamSearch = ''
    GameTime = ''
    GameDay = ''
    for teamSearch in ListTeams:
        cont=0
        for index, SearchGames in enumerate(ExcelList):
            if(cont>0):
                cont-=1
                continue
            if SearchGames[1] == "":
                if SearchGames[0] == '':
                    GameDay = ExcelList[index+1][0]
                    GameTime = ExcelList[index+2][0]
                    cont = 2
                else:
                    GameTime = ExcelList[index][0]
            elif SearchGames[0]==teamSearch:
                ExcelTeamGameList.append([teamSearch,'vs',SearchGames[2],'at', SearchGames[4],'on',GameDay, 'at', GameTime])
            elif SearchGames[2]==teamSearch:
                ExcelTeamGameList.append([teamSearch,'vs',SearchGames[0],'at', SearchGames[4],'on',GameDay, 'at', GameTime])
        ExcelTeamGameList.append(['','','','','','','','',''])
    df = pd.DataFrame(data=ExcelTeamGameList)
    df.to_excel(".\Output-Folder\Games-For-Each-Team.xlsx",sheet_name="TeamGames")    
     
    
    LocationCountPerTeam = []
    B2BCount = 0
    for i in range (len(ListTeams)):
        LocationCountPerTeam.append([0,0,0,0])
    for inds, match in enumerate(FGames):
        if len(match)>3 and match[3] == "Double Header":
            B2BCount+=1
        LocationCountPerTeam[TeamToIndex(match[0])][LocationToIndex(match[2])]+=1
        LocationCountPerTeam[TeamToIndex(match[1])][LocationToIndex(match[2])]+=1
    differential = -1
    
    TeamLocations = []
    TeamLocations.append(['Team Name',ListLocations[0],ListLocations[1],ListLocations[2],ListLocations[3]])
    for indx,locationcount in enumerate(LocationCountPerTeam):
        TeamLocations.append([ListTeams[indx], locationcount[0],locationcount[1],locationcount[2],locationcount[3]])        
        locationcount.sort()
        if (locationcount[-1] - locationcount[0]) > differential:
            differential = (locationcount[-1] - locationcount[0])
            indxstore = indx
    df = pd.DataFrame(data=TeamLocations)
    df.to_excel(".\Output-Folder\Team-Location-count.xlsx",sheet_name="Locations-per-team")  


    #(f"Maximum location error: +-{differential} in team {ListTeams[indxstore]}")
    #(LocationCountPerTeam)
    
    DebugInfo = ReturnParam(1,ErrorList, len(ErrorList),B2BCount,100-differential*1.5-len(ErrorList)-B2BCount*3,0,DGames)

    debuglist = []
    for index,match in enumerate(FGames):
        if len(debuglist) ==4:
            debuglist = []
        if match[2] in debuglist:
            DebugInfo.success = 0
            DebugInfo.FatalError = 1
            #("FATAL ERROR DETECTED! REPORT TO RHA 'Simultanious Location Access Detected!' ")
            exit()
        else:
            debuglist.append(match[2])
    #(f"Overall error/rating of this set is {100-differential*1.5-len(ErrorList)-B2BCount*3} points out of 100.")
    return DebugInfo








