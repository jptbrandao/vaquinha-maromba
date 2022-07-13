import sys
from bs4 import BeautifulSoup
import re
import csv

# Player has structure:
# - name: string
# - date: string
# - messageId: string

def getDate(div):
    divTimestamp = div.find('div', class_='pull_right date details')
    date = re.search("title=\".*\"", str(divTimestamp)).group().split('"')[1][:10]
    return date

def getPlayerName(msgId, soup):
    for i in range(0, 20):
        nextNumber = int(msgId.split('message')[1])-i
        currentMsgId = 'message'+ str(nextNumber)
        msgBlock = soup.find('div', id=currentMsgId)
        nameDiv = msgBlock.find('div', class_='from_name')
        if nameDiv != None:
            return nameDiv.text.strip()

def extractPlayerFromBlockMessage(msgId, soup):
    msgBlock = soup.find('div', id=msgId)
    date = getDate(msgBlock)
    playerName = getPlayerName(msgId, soup)
    player = { "name": playerName, "date": date, "messageId": msgId }
    return player


def confirmMessageBlock(msgBlock, hashtag):
    regexMatch = re.search(hashtag, str(msgBlock).lower())
    if regexMatch == None:
        return False
    return msgBlock.find('img') != None

def getValidPlayersBidFromFile(filename):
    f = open(filename, "r")
    index = f.read()
    soup = BeautifulSoup(index, 'html.parser')
    msgIdList = list(map(lambda x: x.get('id') , soup.find_all('div', id=True)))
    confirmedList = []
    for msgId in msgIdList:
        msgBlock = soup.find('div', id=msgId)
        if confirmMessageBlock(msgBlock, "#maromba23"):
            confirmedList.append(msgId)

    playerList = []
    for msgId in confirmedList:
        player = extractPlayerFromBlockMessage(msgId, soup)
        playerList.append(player)
    return playerList


def outputData(filepath, fields, rows):
    with open(filepath, "w") as output:
        csvwriter = csv.writer(output)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)


def parse(inputFilename, outputFilename):
    fields = ['date', 'name', 'messageId']
    playerList = getValidPlayersBidFromFile(inputFilename)
    print(playerList)

    playerRows = list(map(lambda x: [x['date'], x['name'], x['messageId']], playerList))
    print(fields)
    print(playerRows)

    outputData(outputFilename, fields, playerRows)

if __name__ == "__main__":
    inputFilename = sys.argv[1]
    outputFilename = sys.argv[2]
    if outputFilename == None:
        outputFilename = "output.txt"
    print(inputFilename)
    print(outputFilename)
    parse(inputFilename, outputFilename)
