import os
import re
from parseHtmlFile import parseHtml
from countBids import loadBids

def getFilenames(path):
    path = "../data/chats-html"
    dirList = os.listdir(path)
    return dirList

def ioFilePath(inputfilename, inputPathDir, outputPathDir):
    outputfilepath = outputPathDir + re.sub("\.html", ".csv", inputfilename)
    inputfilepath = inputPathDir + inputfilename
    return (inputfilepath, outputfilepath)

def getIOFilePaths(inputPathDir, outputPathDir):
    inputFilenames = getFilenames(inputPathDir)
    ioFilePaths = list(map(lambda x: ioFilePath(x, inputPathDir, outputPathDir), inputFilenames))
    return ioFilePaths

if __name__ == "__main__":
    inputDir = '../data/chats-html/'
    outputDir = '../data/chat-bids/'
    ioFilePaths = getIOFilePaths(inputDir, outputDir)

    for ioFiles in ioFilePaths:
        if re.match(".*\.DS_Store", ioFiles[0]):
            continue
        print()
        print('Extracting bids from:', ioFiles[0])
        print('Writing them to:', ioFiles[1])
        parseHtml(ioFiles[0], ioFiles[1])

    print('Bids extracted from html files')
    print('Aggregating bids')
    print()
    print()
    print('=========================')
    print()
    outputPaths = list(map(lambda x: x[1], ioFilePaths))
    loadBids(outputPaths)
    print()
    print('=========================')
    print()
    print()
    print('done')
