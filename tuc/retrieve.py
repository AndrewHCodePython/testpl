import urllib.request
from html.parser import HTMLParser
import re
import pprint


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
        print ('died')

def main():

    # create request object 
    req = urllib.request
    baseURL = "https://www.tuc.org/zuluru/people/view/person:"
    redirectURL = "https://www.tuc.org/zuluru/leagues"

    # dictionary to hold players
    playersDict = {}

    # regex 
    regexPattern = '\u00BB\s{1}(.+?)\s{1}\u00BB'
    
    
    
    for playerID in range(50001, 50003):
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
            playerName = re.search('\u00BB\s{1}(.+?)\s{1}\u00BB', titleContent, re.UNICODE).group(1)

            # add players to dictionary
            playersDict[playerID] = playerName

            # clear
            

    pprint.pprint(playersDict)

if __name__ == "__main__":
    main()