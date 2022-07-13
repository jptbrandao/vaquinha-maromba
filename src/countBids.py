import csv
import datetime

def getDayOfWeek(date):
    dateElements = date.split('.')
    day = int(dateElements[0])
    month = int(dateElements[1])
    year = int(dateElements[2])
    weekday = datetime.date(year, month, day).weekday()
    # Monday is 0
    return weekday

def mapPlayers(playername):
    mapPlayers = {'Fernanda': 'Fernanda', 'Coutinho': 'Couto', 'Filipo Negrao':'Filipo', 'Haroldo Olivieri':'Haroldo', 'João Pedro Brandão': 'Brandao', 'Argento': 'Argento', 'Dalma Cerro':'Dalma', 'Pedro Argento': 'Pedro'}
    return mapPlayers[playername]

def registerPlayerBidsPerWeekDay(row, bidWeek):
    # Get day of the week
    dayOfWeek = getDayOfWeek(row[0])
    # Map name
    player = mapPlayers(row[1])
    bidWeek[dayOfWeek].append(player)
    return bidWeek

def applyGameRules(bidWeek):
    # For each day, remove duplicates
    for i in range(len(bidWeek)):
        bidWeek[i] = list(set(bidWeek[i]))
    # For each player, add total of week, max out at 5
    playersTotalBid = {}
    for day in bidWeek:
        for player in day:
            playersTotalBid[player] = playersTotalBid.get(player, 0) + 1
            playersTotalBid[player] = min(playersTotalBid[player], 5)
    return playersTotalBid

def countPlayersBidsInFile(filename):
    # Initialize week
    bidWeek = [[] for i in range(7)]

    with open(filename, 'r') as file:
        csvFile = csv.reader(file)
        header = next(csvFile)
        for row in csvFile:
            bidWeek = registerPlayerBidsPerWeekDay(row, bidWeek)

    playersTotalBids = applyGameRules(bidWeek)
    return playersTotalBids

filename = 'bid-22-07-11.csv'
playersTotalBids = countPlayersBidsInFile(filename)
print()
print(playersTotalBids)
