########################################
## Gallup Poll Information Extraction ##
## Created On: 07.17.19               ## 
## Updated On: 07.17.19               ##
########################################

# Other Imports
import requests
from bs4 import BeautifulSoup

# My Imports
import GallupPollStateInformation

# Static Globals
GALLUP_POLL_URL = "https://news.gallup.com/poll/226643/2017-party-affiliation-state.aspx"
TBODY_TAG = "tbody"
TR_TAG = "tr"
TH_TAG = "th"
TD_TAG = "td"
TD_DEMOCRAT_INDEX = 0
TD_REPUBLICAN_INDEX = 1
TD_POPULATION_INDEX = 3

def main():
    information = ExtractInfoFromGallupPoll()
    for key in information.keys():
        print(information[key].ToString())
    
def ExtractInfoFromGallupPoll():
    extractedDictOfStateInformation = dict()
    html = ExtractHtmlFromUrl(GALLUP_POLL_URL)
    tables = ExtractTablesFromHtml(html)
    
    for table in tables:
        rows = ExtractRowsFromTable(table)
        
        for row in rows:
            state = ExtractLocationFromRow(row)
            data = ExtractDataFromRow(row)
            index = 0
            democratic = -1
            republican = -1
            population = -1
            
            for datum in data:
                if index == TD_DEMOCRAT_INDEX:
                    democratic = datum.text
                elif index == TD_REPUBLICAN_INDEX:
                    republican = datum.text
                elif index == TD_POPULATION_INDEX:
                    population = datum.text
                    
                index += 1
                
            StateInformation = GallupPollStateInformation.StateInformation(state, population, democratic, republican)
            extractedDictOfStateInformation[state] = StateInformation
            
    return extractedDictOfStateInformation

def ExtractHtmlFromUrl(url):
    request = requests.get(url)
    html = BeautifulSoup(request.text, "html.parser")
    return html

def ExtractTablesFromHtml(html):    
    tables = html.find_all(TBODY_TAG)
    return tables

def ExtractRowsFromTable(table):
    rows = table.find_all(TR_TAG)
    return rows

def ExtractLocationFromRow(row):
    location = row.find(TH_TAG)
    return location.text

def ExtractDataFromRow(row):
    data = row.find_all(TD_TAG)
    return data
    
if __name__=="__main__":
    main()
