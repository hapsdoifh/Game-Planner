import math
import pandas 
import copy

class Team:
    loctnCnt = [0,0,0,0]
    def __init__(self,name,Ngames,Avail):
        self.name = name
        self.Ngames = Ngames
        self.Avail = Avail
    def clearAvail(self):
        self.Avail = 1    

class Games:
    location = ''
    def __init__(self,Team1,Team2,played):
        self.Team1 = Team1
        self.Team2 = Team2
        self.played = played



def GenerateGames(Teams): #Teams is a string 
    ListReturn = []
    for i in range(len(Teams)):
        for j in range(i+1,len(Teams)):
            temp = Games(Teams[i],Teams[j],0)
            ListReturn.append(temp)
    return ListReturn

def PackageTeams(TeamList):
    StructedList = []
    for index, i in enumerate(TeamList):
        temp = Team(i, 0, 1)
        StructedList.append(temp)
    return StructedList   

def GetTeamForGame(GameList,TeamList): #find team for the next game
    MinPlayed = 0
    MinPlace = 0
    for i in range(len(TeamList)):
        if i == 0:
            MinPlayed = TeamList[i].Ngames
            MinPlace = i
        if TeamList[i].Ngames < MinPlayed:
            if TeamList[i].Avail == 1: #the team is available for that time
                MinPlayed = TeamList[i].Ngames
                MinPlace = i
    TeamList[MinPlace].Ngames += 1
    for i in range(len(GameList)):
        #if the current game include the team that was selected
        if TeamList[MinPlace].name == GameList[i].Team1.name or TeamList[MinPlace].name == GameList[i].Team2.name: 
            #Finds the first game that hasn't been played and both players are available, TODO: might needs to impletement so it picks the two teams that has played the least
            if GameList[i].played == 0 and GameList[i].Team1.Avail == 1 and GameList[i].Team2.Avail == 1:
                GameList[i].Team1.Avail = 0
                GameList[i].Team2.Avail = 0
                return GameList[i]

def OrganizeGames(GameList,TeamList,Locations,timeLimit):
    LocationList = Locations.copy()
    OrganizedGames = []
    for i in range(timeLimit):
        for i in range(len(Locations)):
            #copy location list used to help location distribution
            LocationList = Locations.copy()
            myGame = GetTeamForGame(GameList,TeamList)
            minL = 0
            minLplace = 0
            first = 0
            #find location that they played the least in
            for j in range(len(myGame.Team1.loctnCnt)):
                #if location is least played and not already taken 
                if first == 0 and (not LocationList[i] == '') :
                    minL = myGame.Team1.loctnCnt[i]
                    minLplace = i
                    first = 1
                if myGame.Team1.loctnCnt[i] < minL and (not LocationList[i] == '') :
                    minL = myGame.Team1.loctnCnt[i]
                    minLplace = i
            myGame.Team1.loctnCnt[i] += 1
            myGame.location =  LocationList[i]
            LocationList[i] = ''
            OrganizedGames.append(myGame)
        for i in TeamList:
            i.clearAvail()
    return OrganizedGames
    

        


inputlist = ['a','b','c','d','e','f','g','h']  
inputLocation = ['l1','l2','l3','l4']
TeamList = PackageTeams(inputlist)  
GameList = GenerateGames(TeamList) 
Fgames = OrganizeGames(GameList,TeamList,inputLocation,5)
for i in Fgames:
    print(i.Team1.name, 'vs', i.Team2.name, 'at', i.location)