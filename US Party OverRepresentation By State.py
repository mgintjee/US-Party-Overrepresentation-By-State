##########################################
## US Party OverRepresentation By State ##
## Created On: 07.18.19                 ## 
## Updated On: 07.18.19                 ##
##########################################

import HoRWikiInformationExtraction, GallupPollInformationExtraction, PartyRepresentationStateInformation
GALLUP_POLL_US_KEY = "U.S."
# Index | Item
#  0 | State
#  1 | Population
#  2 | Voters Democratic 
#  3 | Voters Republican
#  4 | Voters Indpendent
#  5 | Seats
#  6 | Seats Democratic Actual
#  7 | Seats Republican Actual
#  8 | Seats Independent Actual 
#  9 | Seats Democratic Expected
# 10 | Seats Republican Expected
# 11 | Seats Independent Expected
# 12 | Overrepresentation Democratic
# 13 | Overrepresentation Republican
# 14 | Overrepresentation Independent
DESIRED_INFORMATION_TEMPLATE_STRING = "{}\t" * 2  + "{}%\t" * 3 + "{}\t" * 7 + "{}%\t" * 3 + "\n"
DEMOCRATIC_KEY = PartyRepresentationStateInformation.DEMOCRATIC_KEY
REPUBLICAN_KEY = PartyRepresentationStateInformation.REPUBLICAN_KEY
INDEPENDENT_KEY = PartyRepresentationStateInformation.INDEPENDENT_KEY
WITH_INDEPENDENT_TSV_FILE = "ExpectedWithIndependent.tsv"
WITHOUT_INDEPENDENT_TSV_FILE = "ExpectedWithoutIndependent.tsv"

def main():
    withIndependentTsvFile = open(WITH_INDEPENDENT_TSV_FILE, "w+")
    withoutIndependentTsvFile = open(WITHOUT_INDEPENDENT_TSV_FILE, "w+")
    
    HoRWikiInformation = HoRWikiInformationExtraction.ExtractInfoFromHoRWiki()
    GallupPollInformation = GallupPollInformationExtraction.ExtractInfoFromGallupPoll()
    commonStates = []
    
    for state in GallupPollInformation.keys():
        if(state in HoRWikiInformation.keys()):
            commonStates.append(state)
            
    commonStates.sort()
    
    for state in commonStates:
        HoRWikiStateInfo = HoRWikiInformation[state]
        GallupPollStateInfo = GallupPollInformation[state]
        PartyRepStateInfo = PartyRepresentationStateInformation.StateInfo(GallupPollStateInfo, HoRWikiStateInfo)
        withIndependentInformation = ExtractDesiredInformationFromPartyRepresentationStateInfo(PartyRepStateInfo, True)
        withoutIndependentInformation = ExtractDesiredInformationFromPartyRepresentationStateInfo(PartyRepStateInfo, False)
        withIndependentTsvFile.write(withIndependentInformation)
        withoutIndependentTsvFile.write(withoutIndependentInformation)
        
    withIndependentTsvFile.close()
    withoutIndependentTsvFile.close()
    
def ExtractDesiredInformationFromPartyRepresentationStateInfo(PartyRepStateInfo, IncludeIndependent):
    state = PartyRepStateInfo.State
    population = PartyRepStateInfo.Population
    seatsTotal = PartyRepStateInfo.TotalSeats
    
    votersDemocratic = PartyRepStateInfo.DemocraticVoters
    votersRepublican = PartyRepStateInfo.RepublicanVoters
    votersIndependent = PartyRepStateInfo.IndependentVoters
    
    seatsDemocraticActual = PartyRepStateInfo.DemocraticSeats
    seatsRepublicanActual = PartyRepStateInfo.RepublicanSeats
    seatsIndependentActual = PartyRepStateInfo.IndependentSeats

    ExpectedSeats = PartyRepStateInfo.GetExpectedSeats(IncludeIndependent)

    seatsDemocraticExpected = ExpectedSeats[DEMOCRATIC_KEY]
    seatsRepublicanExpected = ExpectedSeats[REPUBLICAN_KEY]
    seatsIndependentExpected = ExpectedSeats[INDEPENDENT_KEY]

    overrepresentationDemocratic = (seatsDemocraticActual - seatsDemocraticExpected) * (100/seatsTotal)
    overrepresentationRepublican = (seatsRepublicanActual - seatsRepublicanExpected) * (100/seatsTotal)
    overrepresentationIndependent = (seatsIndependentActual - seatsIndependentExpected) * (100/seatsTotal)
    
    returnString = DESIRED_INFORMATION_TEMPLATE_STRING.format(state, population,
                                                              votersDemocratic, votersRepublican, votersIndependent,
                                                              seatsTotal,
                                                              seatsDemocraticActual, seatsRepublicanActual, seatsIndependentActual,
                                                              seatsDemocraticExpected, seatsRepublicanExpected, seatsIndependentExpected,
                                                              overrepresentationDemocratic, overrepresentationRepublican, overrepresentationIndependent)

    return returnString
if __name__=="__main__":
    main()
