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
    def __init__(self, Success, ErrList, MagError, CscGame, rating, FERROR):
        self.success = Success
        self.NotPlayedGames = ErrList
        self.ConSecGame = CscGame
        self.MagError = MagError
        self.rating = rating
        self.FatalError = FERROR


def RETURNMATCHES(Input1, Input2,TimeOne,TimeTwo, GameYear):
    #Stores the list of teams
    ListTeams = Input1
    #Stores the list of locations
    ListLocations = Input2
    #List for storing the sorted list or 'Final Games'
    FGames = []
    #How many times each team played at each location. Stored as a 2d list
    LocationCountPerTeam = []
    #List of weeks
    ListWeeks = []
    #Stores how many games each team played. Used for selecting the best match to play first as well as Debugging to make sure every game is played
    GamesPlayedPerTeam = []
    #Stores Possible Games
    PossibleGames = []
    #Goes through the list of teams to convert a team name to an index
    def TeamToNumber(team):
        for index,item in enumerate(ListTeams):
            if item == team:
                return index
    #Generates LocationCountPerTeam and sets GamesPlayedPerTeam to 0
    LocationCountPerTeamCopy = []
    for o in range(len(ListTeams)):
        LocationCountPerTeam.append([1,1,1,1])
        LocationCountPerTeamCopy.append([1,1,1,1])
        GamesPlayedPerTeam.append(0)
    #Using an algorithm, generates all possible games. Works by appending a team versus the teams after it and none before it.
    '''
    eg:
    1v2,3,4,5,6,7,8
    2vs3,4,5,6,7,8
    3vs4,5,6,7,8
    4vs5,6,7,8
    5vs6,7,8
    6vs7,8
    7vs8
    '''
    def LocationToIndex(location):
        for index,item in enumerate(ListLocations):
            if item == location:
                return index
    for index,x in enumerate(ListTeams):
        for ind, team in enumerate(ListTeams):
            if not(ind<=index):
                PossibleGames.append([ListTeams[index],team])
    #Generates WeekList
    from datetime import date
    year = GameYear
    #("Calculating..")
    start = time.time()
    x=1
    def listToString(s):
        str1 = "" 
        for ele in s:
            str1 += (f"{ele} ")
        return str1
    
    for k in range(31):
        dateasy = str(date(year,5,x).ctime())
        listm = dateasy.split(" ")
        if listm[0] == "Sat" or listm[0] == "Sun":
            if str((date(year,5,x).ctime())).split(" ")[2] == '':
                ListWeeks.append(listToString(str((date(year,5,x).ctime())).split(" ")[1:4]))
            else:
                ListWeeks.append(listToString(str((date(year,5,x).ctime())).split(" ")[1:3]))
        x+=1
    
    x=1
    for k in range(30):
        dateasy = str(date(year,6,x).ctime())
        listm = dateasy.split(" ")
        if listm[0] == "Sat" or listm[0] == "Sun":
            if str((date(year,5,x).ctime())).split(" ")[2] == '':
                ListWeeks.append(listToString(str((date(year,6,x).ctime())).split(" ")[1:4]))
            else:
                ListWeeks.append(listToString(str((date(year,6,x).ctime())).split(" ")[1:3]))
        x+=1
    
    x=1
    for aa in range(1000):
        ListWeeks.append(f"Extra Week {aa}")
    for k in range(30):
        dateasy = str(date(year,6,x).ctime())
        listm = dateasy.split(" ")
        if listm[0] == "Sat" or listm[0] == "Sun":
            if str((date(year,5,x).ctime())).split(" ")[2] == '':
                ListWeeks.append(listToString(str((date(year,6,x).ctime())).split(" ")[1:4]))
            else:
                ListWeeks.append(listToString(str((date(year,6,x).ctime())).split(" ")[1:3]))
        x+=1
    #Algorithm that sorts the list with the priority of allowing each team to play an equal amount of Games.
    while len(PossibleGames)>0:
        smallest = 1000
        for index, match in enumerate(PossibleGames):
            if GamesPlayedPerTeam[TeamToNumber(match[0])] + GamesPlayedPerTeam[TeamToNumber(match[1])]  < smallest:
                smallest =  GamesPlayedPerTeam[TeamToNumber(match[0])] +  GamesPlayedPerTeam[TeamToNumber(match[1])]
                indexstore = index
            BestMatch = PossibleGames[indexstore]
        FGames.append(BestMatch)
        GamesPlayedPerTeam[TeamToNumber(BestMatch[0])]+=1
        GamesPlayedPerTeam[TeamToNumber(BestMatch[1])]+=1
        PossibleGames.remove(BestMatch)
    
    #Gives locations per team.Sorts by least played per pair, and does not allow duplicate locations for groups of four.
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
    scorelist = []
    def FindScore(LocationCount,group,Combination):
        score = 0
        counter = 1
        for ind,match in enumerate(group):
            counter = 1
            for k in range(4):
                if k!=Combination[ind]:
                    
                    counter*= LocationCount[TeamToNumber(match[0])][k]
                else:
                    
                    counter*= (LocationCount[TeamToNumber(match[0])][k]+1)
            score+=counter
            for l in range(4):
                if l!=Combination[ind]:
                    
                    counter*= LocationCount[TeamToNumber(match[1])][l]
                else:
                    
                    counter*= (LocationCount[TeamToNumber(match[1])][l]+1)
            score+=counter
        return score
    indexbest = 0

    try:
        for index,match in enumerate(FGames):
            scorelist = []
            if index%4 == 0 :

                scorelist = []
                for combination in PossibleLocationIndicies:
                    scorelist.append(FindScore(LocationCountPerTeam, [FGames[index],FGames[index+1],FGames[index+2],FGames[index+3]],combination))
                largestt = -100

                for indd,score in enumerate(scorelist):
                    if score>largestt:
                        largestt = score
                        indexbest = deepcopy(indd)
             
                for lp in range(4):
                    LocationCountPerTeam[TeamToNumber(FGames[index+lp][0])][PossibleLocationIndicies[indexbest][lp]]+=1
                    LocationCountPerTeam[TeamToNumber(FGames[index+lp][1])][PossibleLocationIndicies[indexbest][lp]]+=1
                    
                for ii in range(4):
                    FGames[index+ii].append(ListLocations[PossibleLocationIndicies[indexbest][ii]])
            indtrack = deepcopy(index)
    except IndexError:
        Taken = []
        smallest = 100000000
        for i in range(len(FGames)-indtrack):
            smallest = 100000000
            for inddd in range(4):
                if LocationCountPerTeam[TeamToNumber(FGames[-1-i][0])][inddd] + LocationCountPerTeam[TeamToNumber(FGames[-1-i][1])][inddd] <smallest and (ListLocations[inddd] not in Taken):
                    smallest = LocationCountPerTeam[TeamToNumber(FGames[-1-i][0])][inddd] + LocationCountPerTeam[TeamToNumber(FGames[-1-i][1])][inddd]
                    indexstore = inddd
            Taken.append(ListLocations[indexstore])
            FGames[-1-i].append(ListLocations[indexstore])
    PlayedOnce = []
    Contrastlist = []
    B2BCount = 0
    intindex = 0
    try:
        for index, match in enumerate(FGames):
            PlayedOnce.append(match[0])
            PlayedOnce.append(match[1])
            intindex+=1
            if intindex == 9 :
                intindex = 1
            if PlayedOnce.count(match[0]) >=2:
                if intindex == 5:
                    for k in range(index, index+4, 1):
                        FGames[k].pop(2)
                    Contrast = FGames[index-4:index]
                elif intindex == 6:
                    for k in range(index-1, index+3, 1):
                        FGames[k].pop(2)
                    Contrast = FGames[index-5:index-1]
                elif intindex == 7:
                    for k in range(index-2, index+2, 1):
                        FGames[k].pop(2)
                    Contrast = FGames[index-6:index-2]
                elif intindex == 8:
                    for k in range(index-3, index+1, 1):
                        FGames[k].pop(2)
                    Contrast = FGames[index-7:index-3]
                B2BCount +=1
                
                Contrastlist.append(Contrast)
            if len(PlayedOnce) == 16:
                PlayedOnce = []
    except IndexError:
        pass
    InstanceOfB2B = 0
    Taken = []
    #Used to avoid potential index errors as a result of consecutive games, or in the rare instance of back to back consecutive games
    for loop in range(3):
        Contrastlist.append(['',''])
    for index,match in enumerate(FGames):
        if len(match) == 2:
            for game in Contrastlist[InstanceOfB2B]:
                if match[0] in game or match[1] in game:
                    match.append(game[2])
                    match.append("Back To Back Game")
                    InstanceOfB2B+=1
    tiniest = 100000000
    try:
        for index,match in enumerate(FGames):
            if index %4 == 0 and (len(FGames[index+1]) == 2 or len(FGames[index+2]) == 2 or len(FGames[index+3]) == 2 or len(FGames[index]) == 2):
                if len(Taken)>3:
                    Taken = []
                inndex = 0
                for i in range(4):
                    if len(FGames[index+i]) >= 3: 
                        Taken.append(FGames[index+i][2])
                for k in range(4):
                    locationbest = ""
                    tiniest = 100000
                    if len(FGames[index+k]) == 2:
                        for ind,location in enumerate(Input2):
                            if (LocationCountPerTeam[TeamToNumber(FGames[index+k][0])][ind] + LocationCountPerTeam[TeamToNumber(FGames[index+k][1])][ind] < tiniest) and (location not in Taken):
                                if location not in Taken:
                                    tiniest = LocationCountPerTeam[TeamToNumber(FGames[index+k][0])][ind] + LocationCountPerTeam[TeamToNumber(FGames[index+k][1])][ind]
                                    locationbest = location
                                    inndex = ind
                        LocationCountPerTeam[TeamToNumber(FGames[index+k][0])][inndex] +=1
                        LocationCountPerTeam[TeamToNumber(FGames[index+k][1])][inndex] +=1
                        FGames[index+k].append(locationbest)
                        Taken.append(locationbest)
                       
    except IndexError:
        pass
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
    for i in range (len(ListTeams)):
        LocationCountPerTeam.append([0,0,0,0])
    for index, match in enumerate(FGames):
        if index%8 == 0: 
            if str(ListWeeks[int(index/8)]) == "Extra Week 0":
                break
            #print(ListWeeks[int(index/8)])
            #print(TimeOne)
            ExcelList.append(['','','','',''])
            ExcelList.append([ListWeeks[int(index/8)],'','','',''])
            ExcelList.append([TimeOne,'','','',''])
        elif index%4 ==0:
            #print(TimeTwo)
            ExcelList.append([TimeTwo,'','','',''])
        if match not in ErrorList:
            LocationCountPerTeam[TeamToNumber(match[0])][LocationToIndex(match[2])]+=1
            LocationCountPerTeam[TeamToNumber(match[1])][LocationToIndex(match[2])]+=1
            if len(match)>3 and match[3] == "Back To Back Game":
                B2BCount+=1
            count+=1
            #print(match)
            ExcelList.append([match[0],'vs',match[1], 'at', match[2]])
        else:
            pass
            #print(end="")
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
     
    
            
    TeamLocations = []
    TeamLocations.append(['Team Name',ListLocations[0],ListLocations[1],ListLocations[2],ListLocations[3]])
    #print(f'Games That Could Not Be Played: {ErrorList}')
    differential = -1
    for indx,locationcount in enumerate(LocationCountPerTeam):
        TeamLocations.append([ListTeams[indx], locationcount[0],locationcount[1],locationcount[2],locationcount[3]])
        locationcount.sort()
        if (locationcount[-1] - locationcount[0]) > differential:
            differential = (locationcount[-1] - locationcount[0])
            indxstore = indx
     
    df = pd.DataFrame(data=TeamLocations)
    df.to_excel(".\Output-Folder\Team-Location-count.xlsx",sheet_name="Locations-per-team")           
    #print(f"Maximum location error: +-{differential} in team {ListTeams[indxstore]}")
    if len(ErrorList)>0:
        pass
        #print(f"Non-ideal team vs team spread detected. Magnitude of error: {len(ErrorList)}")
    else:
        pass
        #print("Ideal Team vs Team spread.")
    if B2BCount == 0:
        pass
        #print(f"No Teams Play Consecutively.")
    else:
        pass
        #print(f"There has been {B2BCount} instances of Consecutive games")
    debuglist = []
    DebugInfo = ReturnParam(1,ErrorList, len(ErrorList),B2BCount,100-differential*1.5-len(ErrorList)-B2BCount*3,0)

    for index,match in enumerate(FGames):
        if len(debuglist) ==4:
            debuglist = []
        if match[2] in debuglist:
            #print("FATAL ERROR DETECTED! REPORT TO RHA 'Simultanious Location Access Detected!' ")
            DebugInfo.success = 0
            DebugInfo.FatalError = 1
        else:
            debuglist.append(match[2])
    debuglist = []
    return DebugInfo
        #(f"Overall error/rating of this set is {100-differential*1.5-len(ErrorList)-B2BCount*3} points out of 100.")
#Inputs/Function Call
