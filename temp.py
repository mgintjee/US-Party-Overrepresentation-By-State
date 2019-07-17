####
## Loads Information from the Gallup poll
## Created On: 07.17.19
## Updated On: 07.17.19
###
import requests, json
from bs4 import BeautifulSoup

GALLUP_POLL_URL = "https://news.gallup.com/poll/226643/2017-party-affiliation-state.aspx"
WIKI_CURRENT_HOUSE_OF_REPRESENTATIVES_URL = "https://en.wikipedia.org/wiki/List_of_current_members_of_the_United_States_House_of_Representatives"

class GallupStateInformation:
    def __init__(self, state, stateStatistics):
        self.State = state
        self.StateStatistices = stateStatistics

class GallupStateStatistics:
    def __init__(self, democratic, republican):
        self.DemocraticVotes = democratic
        self.RepublicanVotes = republican
                 
def main():
    print(GetJsonDataFromUrl(GALLUP_POLL_URL))
    print("\n\n\n")

def GetJsonDataFromUrl(url):
    request = requests.get(url)

    soup = BeautifulSoup(request.text, "html.parser")
    temp = soup.find_all("tbody")
    for row in temp:
        temp1 = row.find_all("tr")
        for row in temp1:
            header = row.find_all("th")
            data = row.find_all("td")
            print("State: ", end = "")
            print(header[0])
            for datum in data:
                print("\tDatum: ", end = "")
                print(datum)
    #print(pythonObject)
    #jsonObject = json.parse(request.text)#json.loads(request.text)
    #print(jsonObject)

    #print(type(jsonObject))
    
    #GallupFileJson = open("GallupFilePython.txt", "w+")
    #GallupFileJson.write(pythonObject)
    #GallupFileJson.close()
    #GallupFileJson = open("GallupFileJson.txt", "w+")
    #GallupFileJson.write(jsonObject)
    #GallupFileJson.close()
    
if __name__ == "__main__":
    main()
