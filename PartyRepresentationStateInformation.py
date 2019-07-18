############################################
## Party Representation State Information ##
## Created On: 07.18.19                   ##
## Updated On: 07.18.19                   ##
############################################

import math, random

DEMOCRATIC_KEY = "Democratic"
REPUBLICAN_KEY = "Republican"
INDEPENDENT_KEY = "Independent"
MID_THRESHOLD = 0.5

class StateInfo:
    # GallupPollStateInfo: GallupPollStateInformation object for a state 
    # HoRWikiStateInfo   : HoRWikiStateInformation object for a state
    # Note: Both of the states should match
    def __init__(self, GallupPollStateInfo, HoRWikiStateInfo):
        self.State = GallupPollStateInfo.State
        self.Population = GallupPollStateInfo.Population
        self.TotalSeats = HoRWikiStateInfo.Total
        self.DemocraticSeats = HoRWikiStateInfo.Democratic
        self.DemocraticVoters = GallupPollStateInfo.Democratic
        self.RepublicanSeats = HoRWikiStateInfo.Republican
        self.RepublicanVoters = GallupPollStateInfo.Republican
        self.IndependentSeats = HoRWikiStateInfo.Independent
        self.IndependentVoters = GallupPollStateInfo.Independent

    def GetExpectedSeats(self, IncludeIndependent):
        if(IncludeIndependent):
            return self.ExpectedSeatsWithIndependent()
        else:
            return self.ExpectedSeatsWithoutIndependent()

    # Should Return a dict in a similar format to the following:
    # D["Democratic"] = X
    # D["Republican"] = Y
    # D["Independent"] = Z
    def ExpectedSeatsWithIndependent(self):
        dictOfSeats = dict()
        dictOfSeats[DEMOCRATIC_KEY] = 0
        dictOfSeats[REPUBLICAN_KEY] = 0
        dictOfSeats[INDEPENDENT_KEY] = 0
        
        seatsRemaining = self.TotalSeats

        while(seatsRemaining > 0):
            seatsExpectedFloatDemocratic = seatsRemaining * int(self.DemocraticVoters)/100
            seatsExpectedFloatRepublican = seatsRemaining * int(self.RepublicanVoters)/100
            seatsExpectedFloatIndependent = seatsRemaining * int(self.IndependentVoters)/100
            
            seatsExpectedIntDemocratic = math.floor(seatsExpectedFloatDemocratic)
            seatsExpectedIntRepublican = math.floor(seatsExpectedFloatRepublican)
            seatsExpectedIntIndependent = math.floor(seatsExpectedFloatIndependent)

            if(seatsExpectedIntDemocratic == 0 and
               seatsExpectedIntRepublican == 0 and
               seatsExpectedIntIndependent == 0):

                seatsExpectedFloats = [seatsExpectedFloatDemocratic, seatsExpectedFloatRepublican, seatsExpectedFloatIndependent]
                seatsExpectedFloatMax = max(seatsExpectedFloats)
                if(seatsRemaining == 1):
                    if(seatsExpectedFloatMax == seatsExpectedFloatDemocratic):
                        seatsExpectedIntDemocratic += 1
                    elif(seatsExpectedFloatMax == seatsExpectedFloatRepublican):
                        seatsExpectedIntRepublican += 1
                    elif(seatsExpectedFloatMax == seatsExpectedFloatIndependent):
                        seatsExpectedIntIndependent += 1
                    else:
                        # In the unlikely event there is a tie, we will flip a coin
                        coinFlip = random.choice([DEMOCRATIC_KEY, REPUBLICAN_KEY, INDEPENDENT_KEY])
                        if(coinFlip == DEMOCRATIC_KEY):
                            seatsExpectedIntDemocratic += 1
                        elif(coinFlip == REPUBLICAN_KEY):
                            seatsExpectedIntRepublican += 1
                        else:
                            seatsExpectedIntIndependent += 1
                        
                elif(seatsRemaining == 2):
                    if(seatsExpectedFloatMax == seatsExpectedFloatDemocratic):
                        seatsExpectedFloats.remove(seatsExpectedFloatDemocratic)
                        seatsExpectedIntDemocratic += 1
                    elif(seatsExpectedFloatMax == seatsExpectedFloatRepublican):
                        seatsExpectedFloats.remove(seatsExpectedFloatRepublican)
                        seatsExpectedIntRepublican += 1
                    elif(seatsExpectedFloatMax == seatsExpectedFloatIndependent):
                        seatsExpectedFloats.remove(seatsExpectedFloatIndependent)
                        seatsExpectedIntIndependent += 1
                        
                    if(seatsExpectedFloatMax == seatsExpectedFloatDemocratic):
                        seatsExpectedIntDemocratic += 1
                    elif(seatsExpectedFloatMax == seatsExpectedFloatRepublican):
                        seatsExpectedIntRepublican += 1
                    elif(seatsExpectedFloatMax == seatsExpectedFloatIndependent):
                        seatsExpectedIntIndependent += 1
                    
                else:
                    if(seatsExpectedFloatDemocratic > MID_THRESHOLD):
                        seatsExpectedIntDemocratic += 1
                    if(seatsExpectedFloatRepublican > MID_THRESHOLD):
                        seatsExpectedIntRepublican += 1
                    if(seatsExpectedFloatIndependent > MID_THRESHOLD):
                        seatsExpectedIntIndependent += 1

            dictOfSeats[DEMOCRATIC_KEY] += seatsExpectedIntDemocratic
            dictOfSeats[REPUBLICAN_KEY] += seatsExpectedIntRepublican
            dictOfSeats[INDEPENDENT_KEY] += seatsExpectedIntIndependent
                        
            seatsRemaining -= seatsExpectedIntDemocratic
            seatsRemaining -= seatsExpectedIntRepublican
            seatsRemaining -= seatsExpectedIntIndependent

        return dictOfSeats

    # Should Return a dict in a similar format to the following:
    # D["Democratic"] = X
    # D["Republican"] = Y
    # D["Independent"] = 0
    def ExpectedSeatsWithoutIndependent(self):
        dictOfSeats = dict()
        dictOfSeats[DEMOCRATIC_KEY] = 0
        dictOfSeats[REPUBLICAN_KEY] = 0
        dictOfSeats[INDEPENDENT_KEY] = 0

        seatsRemaining = self.TotalSeats

        while(seatsRemaining > 0):
            
            seatsExpectedFloatDemocratic = seatsRemaining * int(self.DemocraticVoters)/100
            seatsExpectedFloatRepublican = seatsRemaining * int(self.RepublicanVoters)/100
            
            seatsExpectedIntDemocratic = math.floor(seatsExpectedFloatDemocratic)
            seatsExpectedIntRepublican = math.floor(seatsExpectedFloatRepublican)

            if(seatsExpectedIntDemocratic == 0 and
               seatsExpectedIntRepublican == 0):
                if(seatsRemaining == 1):
                    if(seatsExpectedFloatDemocratic > seatsExpectedFloatRepublican):
                        seatsExpectedIntDemocratic += 1
                    elif(seatsExpectedFloatRepublican > seatsExpectedFloatDemocratic):
                        seatsExpectedIntRepublican += 1
                    else:
                        # In the unlikely event there is a tie, we will flip a coin
                        coinFlip = random.choice([DEMOCRATIC_KEY, REPUBLICAN_KEY])
                        if(coinFlip == DEMOCRATIC_KEY):
                            seatsExpectedIntDemocratic += 1
                        else:
                            seatsExpectedIntRepublican += 1
                            
                else:
                    if(seatsExpectedFloatDemocratic > MID_THRESHOLD):
                        seatsExpectedIntDemocratic += 1
                    if(seatsExpectedFloatRepublican > MID_THRESHOLD):
                        seatsExpectedIntRepublican += 1

            dictOfSeats[DEMOCRATIC_KEY] += seatsExpectedIntDemocratic
            dictOfSeats[REPUBLICAN_KEY] += seatsExpectedIntRepublican
                        
            seatsRemaining -= seatsExpectedIntDemocratic
            seatsRemaining -= seatsExpectedIntRepublican
            
        return dictOfSeats

    def ToString(self):
        toString = "Location: " + self.State
        toString += "\n> Total Seats: " + str(self.TotalSeats)
        toString += "\n-> Democratic Seats : " + str(self.DemocraticSeats)
        toString += "\n-> Republican Seats : " + str(self.RepublicanSeats)
        toString += "\n-> Independent Seats: " + str(self.IndependentSeats)
        toString += "\n> Population: " + str(self.Population)
        toString += "\n-> Democratic Voters : " + str(self.DemocraticVoters)
        toString += "\n-> Republican Voters : " + str(self.RepublicanVoters)
        toString += "\n-> Independent Voters: " + str(self.IndependentVoters)
        return toString
