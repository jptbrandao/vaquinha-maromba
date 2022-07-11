from bs4 import BeautifulSoup
import re

# Player has structure:
# - name: string
# - timestap: date (string)
# - messageId: string

def getTimeStamp(div):
    divTimestamp = div.find('div', class_='pull_right date details')
    timestamp = re.search("title=\".*\"", str(divTimestamp)).group().split('"')[1]
    return timestamp

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
    timestamp = getTimeStamp(msgBlock)
    playerName = getPlayerName(msgId, soup)
    player = { "name": playerName, "date": timestamp, "messageId": msgId }
    return player


def confirmMessageBlock(msgBlock, hashtag):
    regexMatch = re.search(hashtag, str(msgBlock))
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
    print(playerList)



filename = "messages.html"
getValidPlayersBidFromFile(filename)

