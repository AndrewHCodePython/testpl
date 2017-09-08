#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import urllib.request
from html.parser import HTMLParser
import re
import pprint
import time 
import sys

# inherits HTMLParser class
class MyHTMLParser(HTMLParser):

    startTag = ""
    endTag = ""
    titleContent = ""
    titleFlag = False 

    def handle_starttag(self, tag, attrs):
        self.startTag = tag
    
    def handle_endtag(self, tag):
        self.endTag = tag
       
    def handle_data(self, data):
        if ((self.startTag == "title") and (self.titleFlag == False)):
            # print ("encountered data: " + data)
            self.titleContent = data
            self.titleFlag = True
    
    def __del__(self):
        self.titleContent = ""

def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total*10)))
    print(filled_len)

    percents = round(10.0 * count / float(total), 2)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()  # As suggested by Rom Ruben

def main():

    # define objects/variables
    req         = urllib.request
    baseURL     = "https://www.tuc.org/zuluru/people/view/person:"
    redirectURL = "https://www.tuc.org/zuluru/leagues"
    
    startRange  = 50000
    endRange    = 50100
    playersDict = {}
    
    regexPattern = '\u00BB\s{1}(.+?)\s{1}\u00BB'
    fileName = "players.txt"
    startTime   = time.time()

    for playerID in range(startRange, endRange):
        msg = "get playerID: " + str(playerID) + " of " + str(endRange)
        progress(playerID, endRange, suffix=msg);
        
        playerURL = baseURL + str(playerID)
        page = req.urlopen(playerURL)
        #print(page)
        pageURL = page.geturl()
        #print(pageURL)
        parser = MyHTMLParser()

        if (pageURL == redirectURL):
            print("Does not exist, Player ID: " + str(playerID))
            del parser
        else:
            #print("Player exists, Player ID: " + str(playerID))
            pageContent = page.read()
            pageContent = str(pageContent)
            #print(pageContent)
            
            # html parser stuff
            parser.feed(pageContent)
            titleContent = parser.titleContent
            
            # explicitly call the object to delete it
            del parser

            # do the regex here on titleContent
            playerName = re.search(regexPattern, titleContent, re.UNICODE).group(1)

            # add players to dictionary
            playersDict[playerID] = playerName

            # output dictionary to file in intervals (just in case if memory/buffer overflow)
            if (len(playersDict) == 5):
                #print("Now writing to file...")
                with open('out.txt', 'a+') as f:
                    [f.write('{0},{1}\n'.format(key, value)) for key, value in playersDict.items()]
                
                # wipe the dictionary clean
                playersDict.clear()

    # append the last few entries of the dictionary to the file
    with open('out.txt', 'a+') as f:
        [f.write('{0},{1}\n'.format(key, value)) for key, value in playersDict.items()]

    executionTime = time.time() - startTime

    print ("total time of execution: " + str(executionTime))

if __name__ == "__main__":
    main()
