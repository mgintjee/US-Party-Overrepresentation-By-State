##############################################
## Wiki Political Party Strength Extraction
##############################################

# Other Imports
import requests
import political_party_strength_report
from bs4 import BeautifulSoup

# Static Globals
WIKI_POLITICAL_PARTY_STRENGTH_LINK =  "https://en.wikipedia.org/wiki/Political_party_strength_in_U.S._states"
TBODY_TAG = "tbody"
TR_TAG = "tr"
TH_TAG = "th"
TD_TAG = "td"
TD_STATE_INDEX = 0
TD_US_HoR_SEAT_INDEX = 7
TD_PARTISAN_SPLIT_INDEX = 8
PARTY_LEADER_EVEN = "EVEN"
PARTY_LEADER_DEMOCRATIC = "Democratic"
PARTY_LEADER_REPUBLICAN = "Republican"
PARTY_LEADER_INDEPENDENT = "Independent"

def extract_report_set():
    report_set = set()
    html = extract_html_from_url(WIKI_POLITICAL_PARTY_STRENGTH_LINK)
    if(html != None):
        table = extract_table_from_html(html)
        if(table != None):            
            rows = extract_rows_from_table(table)
            if(rows != None):
                for row in rows:                    
                    data = extract_data_from_row(row)
                    state = ""
                    us_hor_seat = ""
                    us_hor_seat_party_leader = ""
                    partisan_split =""
                    partisan_split_party_leader = ""
                    index = 0
                    
                    if(data != None and len(data) > TD_PARTISAN_SPLIT_INDEX):
                        state = data[TD_STATE_INDEX].text.strip().strip("\n").replace("–", "-")
                        us_hor_seat_party_leader, us_hor_seat = extract_us_hor_seat_info(
                            data[TD_US_HoR_SEAT_INDEX].text.strip().strip("\n").replace("–", "-"))
                        partisan_split_party_leader, partisan_split = extract_party_strength_info(
                            data[TD_PARTISAN_SPLIT_INDEX].text.strip().strip("\n").replace("–", "-"))
                    if(state != "" and
                      us_hor_seat_party_leader != "" and us_hor_seat != "" and
                      partisan_split_party_leader != "" and partisan_split != ""):
                        report_set.add(build_report(state, us_hor_seat_party_leader, us_hor_seat, partisan_split_party_leader, partisan_split))  
    return report_set

def extract_html_from_url(url):
    request = requests.get(url)
    html = BeautifulSoup(request.text, "html.parser")
    return html

def extract_table_from_html(html):
    table = html.find("table", {"class": "sortable wikitable"})
    return table

def extract_rows_from_table(table):
    rows = table.find_all(TR_TAG)
    return rows

def extract_data_from_row(row):
    data = row.find_all(TD_TAG)
    return data

def build_report(state, us_hor_seat_party_leader, us_hor_seat, partisan_split_party_leader, partisan_split ):
    democratic_seats = 0
    democratic_support = 0.0
    republican_seats = 0
    republican_support = 0.0
    independent_seats = 0
    independent_support = 0.0
    
    us_hor_seat_parts = us_hor_seat.split("-")
    partisan_split_parts = partisan_split.split("-")
    
    if( us_hor_seat_party_leader == PARTY_LEADER_DEMOCRATIC):
        democratic_seats = int(us_hor_seat_parts[0])
        republican_seats = int(us_hor_seat_parts[1])
    elif(us_hor_seat_party_leader == PARTY_LEADER_REPUBLICAN):
        republican_seats = int(us_hor_seat_parts[0])
        democratic_seats = int(us_hor_seat_parts[1])
        
    if( partisan_split_party_leader == PARTY_LEADER_DEMOCRATIC):
        democratic_support = round(float(partisan_split_parts[0]), 2)
        republican_support = round(float(partisan_split_parts[1]), 2)
    elif(partisan_split_party_leader == PARTY_LEADER_REPUBLICAN):
        republican_support = round(float(partisan_split_parts[0]), 2)
        democratic_support = round(float(partisan_split_parts[1]), 2)
    elif(partisan_split_party_leader == PARTY_LEADER_EVEN):
        republican_support = round(float(partisan_split_parts[0]), 2)
        democratic_support = round(float(partisan_split_parts[1]), 2)
        
    if(len(us_hor_seat_parts) > 2):
        independent_seats = int(us_hor_seat_parts[2])
    independent_support = round(100 - democratic_support - republican_support, 2)
        
    return political_party_strength_report.report(state, democratic_seats, democratic_support, 
                                                  republican_seats, republican_support, 
                                                  independent_seats, independent_support)

def extract_party_strength_info(datumText): 
    partisan_split =""
    partisan_split_party_leader = ""                       
    if(PARTY_LEADER_DEMOCRATIC in datumText):
        partisan_split_party_leader = PARTY_LEADER_DEMOCRATIC
    elif(PARTY_LEADER_REPUBLICAN in datumText):
        partisan_split_party_leader = PARTY_LEADER_REPUBLICAN
    elif(PARTY_LEADER_EVEN in datumText):
        partisan_split_party_leader = PARTY_LEADER_EVEN
    partisan_split = datumText[len(partisan_split_party_leader):].strip()
    
    partisan_split = remove_sourcing(partisan_split)
    
    return partisan_split_party_leader, partisan_split

def extract_us_hor_seat_info(datumText):
    us_hor_seat_party_leader = ""
    us_hor_seat = ""
    if(PARTY_LEADER_DEMOCRATIC in datumText):
        us_hor_seat_party_leader = PARTY_LEADER_DEMOCRATIC
    elif(PARTY_LEADER_REPUBLICAN in datumText):
        us_hor_seat_party_leader = PARTY_LEADER_REPUBLICAN
    elif(PARTY_LEADER_EVEN in datumText):
        us_hor_seat_party_leader = PARTY_LEADER_INDEPENDENT
    us_hor_seat = datumText[len(us_hor_seat_party_leader):].strip()
    if(us_hor_seat == ""):
        us_hor_seat = "1"
    if(len(us_hor_seat.split('-')) == 1):
        us_hor_seat += "-0"
    us_hor_seat = remove_sourcing(us_hor_seat)
    return us_hor_seat_party_leader, us_hor_seat
    
def remove_sourcing(entry):
    valid_string = ""
    for char in entry:
        if( char in "0123456789-."):
            valid_string += char
        else:
            break
    return valid_string
        