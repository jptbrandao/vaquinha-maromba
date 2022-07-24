import csv
import datetime
import pandas as pd

class Bids:
    def __init__(self):
        self.bidWeeks = {}
        return
    def add(self, date):
        self.addToWeek(date)
        return
    def addToWeek(self, date):
        endWeekDate = self.getWeekEndDate(date)
        startWeekDate = self.addDaysToDate(endWeekDate, -6)
        bids = self.bidWeeks.get(startWeekDate, [])
        bids.append(date)
        bids = list(set(bids))
        self.bidWeeks[startWeekDate] = bids
        return
    def total(self):
        weeks = self.bidWeeks.keys()
        weekTotals = list(map(lambda x: min(5, len(self.bidWeeks[x])), weeks))
        total = sum(weekTotals)
        return total
    def weekTotal(self, week):
        bidWeek = self.bidWeeks.get(week, [])
        weekTotal = min(5, len(bidWeek))
        return weekTotal
    def weeks(self):
        return list(self.bidWeeks.keys())

    def addDaysToDate(self, date, numDays):
        startDate = datetime.datetime.strptime(date, "%d.%m.%Y")
        endDate = startDate + datetime.timedelta(days=numDays)
        newdate = endDate.strftime("%d.%m.%Y")
        return newdate
    def getWeekEndDate(self, startDate):
        startWeekDay = self.getDayOfWeek(startDate)
        weekRange = 6 - startWeekDay
        endDate = self.addDaysToDate(startDate, weekRange)
        return endDate
    def getDayOfWeek(self, date):
        dateElements = date.split('.')
        day = int(dateElements[0])
        month = int(dateElements[1])
        year = int(dateElements[2])
        weekday = datetime.date(year, month, day).weekday()
        # Monday is 0
        return weekday

class Player:
    def __init__(self, name):
        self.name = name
        self.bids = Bids()
        return
    def addBid(self, date):
        self.bids.addToWeek(date)
        return
    def countBids(self):
        weeks = self.bids.weeks()
        weekTotals = list(map(lambda x: self.bids.weekTotal(x), weeks))
        total = sum(weekTotals)
        return total
    def countBidsInWeek(self, week):
        return self.bids.weekTotal(week)
    def activeWeeks(self):
        return self.bids.weeks()



def mapPlayers(playername):
    playerNameMap = {'Fernanda': 'Fernanda', 'Coutinho': 'Couto', 'Filipo Negrao':'Filipo', 'Haroldo Olivieri':'Haroldo', 'João Pedro Brandão': 'Brandao', 'Argento': 'Argento', 'Dalma Cerro':'Dalma', 'Pedro Argento': 'Pedro', 'Garcia Joao': 'Garcia', 'Renan Almeida': 'Renem'}
    return playerNameMap[playername]

def loadBidsFromFile(filename, playersDict):
    with open(filename, 'r') as file:
        csvFile = csv.reader(file)
        header = next(csvFile)
        for row in csvFile:
            name = mapPlayers(row[1])
            player = playersDict.get(name,  Player(name))
            player.addBid(row[0])
            playersDict[name] = player
    return playersDict

def loadBids(filepaths):
    playersDict = {}
    for path in filepaths:
        playersDict = loadBidsFromFile(path, playersDict)
    outputBids(playersDict)
    return

def gameWeeks(playersDict):
    weeks = []
    for name in playersDict:
        weeks.extend(playersDict[name].activeWeeks())
    weeks = list(set(weeks))
    return weeks

def formatPlayerOutput(playersDict, name, weeks):
    player = playersDict[name]
    weeklyBids = list(map(lambda x: player.countBidsInWeek(x), weeks))
    playerOutput = [name, player.countBids()]
    playerOutput.extend(weeklyBids)
    return playerOutput

def outputBids(playersDict):
    names = list(playersDict.keys())
    names.sort()
    weeks = gameWeeks(playersDict)
    weeks.sort(reverse=True)
    columnNames = ['name', 'total']
    columnNames.extend(weeks)
    data = []
    for name in names:
        playerOutput = formatPlayerOutput(playersDict, name, weeks)
        data.append(playerOutput)
    df = pd.DataFrame(data, columns = columnNames)
    print(df)
    return
