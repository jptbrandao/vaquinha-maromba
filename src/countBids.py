import csv
import datetime

class Player:
    def __init__(self, name):
        self.name = name
        self.bidDates = []
        return
    def addBid(self, date):
        self.bidDates.append(date)
        return
    def countBids(self):
        self.bidDates = list(set(self.bidDates))
        self.bidDates.sort()
        firstBidDate = self.bidDates[0]
        lastEndDate = getWeekEndDate(self.bidDates[-1])
        startWeekDate = firstBidDate
        endWeekDate = getWeekEndDate(startWeekDate)
        count = 0
        while endWeekDate <= lastEndDate:
            weekCount = self.countBidsInWeek(startWeekDate, endWeekDate)
            count = count + weekCount
            startWeekDate = addDaysToDate(endWeekDate, 1)
            endWeekDate = getWeekEndDate(startWeekDate)
        return count
    def countBidsInWeek(self, startDate, endDate):
        weekCount = 0
        for date in self.bidDates:
            if date < startDate:
                continue
            if weekCount == 5:
                break
            if date > endDate:
                break
            weekCount = weekCount + 1
        return weekCount

def addDaysToDate(date, numDays):
    startDate = datetime.datetime.strptime(date, "%d.%m.%Y")
    endDate = startDate + datetime.timedelta(days=numDays)
    newdate = endDate.strftime("%d.%m.%Y")
    return newdate

def getWeekEndDate(startDate):
    startWeekDay = getDayOfWeek(startDate)
    weekRange = 6 - startWeekDay
    endDate = addDaysToDate(startDate, weekRange)
    return endDate

def getDayOfWeek(date):
    dateElements = date.split('.')
    day = int(dateElements[0])
    month = int(dateElements[1])
    year = int(dateElements[2])
    weekday = datetime.date(year, month, day).weekday()
    # Monday is 0
    return weekday

def mapPlayers(playername):
    mapPlayers = {'Fernanda': 'Fernanda', 'Coutinho': 'Couto', 'Filipo Negrao':'Filipo', 'Haroldo Olivieri':'Haroldo', 'João Pedro Brandão': 'Brandao', 'Argento': 'Argento', 'Dalma Cerro':'Dalma', 'Pedro Argento': 'Pedro', 'Garcia Joao': 'Garcia'}
    return mapPlayers[playername]

def countBidsFromFile(filename, playersDict):
    with open(filename, 'r') as file:
        csvFile = csv.reader(file)
        header = next(csvFile)
        for row in csvFile:
            name = mapPlayers(row[1])
            player = playersDict.get(name,  Player(name))
            player.addBid(row[0])
            playersDict[name] = player
    return playersDict

def countBids(filepaths):
    playersDict = {}
    for path in filepaths:
        playersDict = countBidsFromFile(path, playersDict)
    for name in playersDict:
        count = playersDict[name].countBids()
        print(name + ': ' + str(count))
    return
