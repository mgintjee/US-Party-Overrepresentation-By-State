# US Party Representation By State
import json, math
# Whether or not we are including 3rd party as a party to be represented
Include3rd = False
Debug = False

class StateInfo:
    def __init__(self, State, StateInformation):
        self.State = State
        self.PercentDem = StateInformation["PercentDem"]
        self.PercentRep = StateInformation["PercentRep"]
        self.Percent3rd = 100-(self.PercentDem + self.PercentRep)
        self.SeatsSum = StateInformation["SeatsSum"]
        self.SeatsDemA = StateInformation["SeatsDem"]
        self.SeatsRepA = StateInformation["SeatsRep"]
        self.Seats3rdA = self.SeatsSum - (self.SeatsDemA + self.SeatsRepA)

        if(Include3rd):
            Expected = self.GetExpectedSeatsWith3rd()
        else:
            Expected = self.GetExpectedSeatsWithout3rd()
                
        self.SeatsDemX = Expected[0]
        self.SeatsRepX = Expected[1]
        self.Seats3rdX = Expected[2]
        
    def GetExpectedSeatsWith3rd(self):        
        Seats = [0, 0, 0]
        SeatsRem = self.SeatsSum
                  
        while SeatsRem > 0:
            c = SeatsRem
            ExpectedDemFloat = SeatsRem * (self.PercentDem/100)
            ExpectedRepFloat = SeatsRem * (self.PercentRep/100)
            Expected3rdFloat = SeatsRem * (self.Percent3rd/100)

            ExpectedDem = math.floor(ExpectedDemFloat)
            ExpectedRep = math.floor(ExpectedRepFloat)
            Expected3rd = math.floor(Expected3rdFloat)

            if(ExpectedDem == 0 and ExpectedRep == 0 and Expected3rd == 0):
                Floats = [ExpectedDemFloat, ExpectedRepFloat, Expected3rdFloat]
                if SeatsRem == 1:
                    if  (ExpectedDemFloat == max(Floats)):
                        ExpectedDem += 1
                    elif(ExpectedRepFloat == max(Floats)):
                        ExpectedRep += 1
                    elif(Expected3rdFloat == max(Floats)):
                        Expected3rd += 1
                elif(SeatsRem == 2):
                    if  (ExpectedDemFloat == max(Floats)):
                        Floats.remove(ExpectedDemFloat)
                        ExpectedDem += 1
                    elif(ExpectedRepFloat == max(Floats)):
                        Floats.remove(ExpectedRepFloat)
                        ExpectedRep += 1
                    elif(Expected3rdFloat == max(Floats)):
                        Floats.remove(Expected3rdFloat)
                        Expected3rd += 1
                    if  (ExpectedDemFloat == max(Floats)):
                        ExpectedDem += 1
                    elif(ExpectedRepFloat == max(Floats)):
                        ExpectedRep += 1
                    elif(Expected3rdFloat == max(Floats)):
                        Expected3rd += 1
                else:
                    if(ExpectedDemFloat > 0.5):
                        ExpectedDem += 1
                    if(ExpectedRepFloat > 0.5):
                        ExpectedRep += 1
                    if(Expected3rdFloat > 0.5):
                        Expected3rd += 1
                        
            Seats[0] += ExpectedDem
            Seats[1] += ExpectedRep
            Seats[2] += Expected3rd
            
            SeatsRem -= ExpectedDem
            SeatsRem -= ExpectedRep
            SeatsRem -= Expected3rd

        return Seats
    
    def GetExpectedSeatsWithout3rd(self):
        Seats = [0, 0, 0]
        SeatsRem = self.SeatsSum
                  
        while SeatsRem > 0:
            c = SeatsRem
            ExpectedDemFloat = SeatsRem * (self.PercentDem/100)
            ExpectedRepFloat = SeatsRem * (self.PercentRep/100)

            ExpectedDem = math.floor(ExpectedDemFloat)
            ExpectedRep = math.floor(ExpectedRepFloat)

            if(ExpectedDem == 0 and ExpectedRep == 0):
                if SeatsRem == 1:
                    if  (ExpectedDemFloat > ExpectedRepFloat):
                        ExpectedDem += 1
                    elif(ExpectedRepFloat > ExpectedDemFloat):
                        ExpectedRep += 1
                else:
                    if(ExpectedDemFloat > 0.5):
                        ExpectedDem += 1
                    if(ExpectedRepFloat > 0.5):
                        ExpectedRep += 1
            Seats[0] += ExpectedDem
            Seats[1] += ExpectedRep
            
            SeatsRem -= ExpectedDem
            SeatsRem -= ExpectedRep

        return Seats

    def DebugPrintSeatsA(self):
        print("State:",self.State,"| D: {0:3}".format(self.SeatsRepA),"R: {0:3}".format(self.SeatsDemA))

    def DebugPrintPercents(self):
        print("State:",self.State,"| D: {0:2}".format(self.PercentDem),"R: {0:2}".format(self.PercentRep))
        

def main():
    with open('DataByState.json') as f:
        data = json.load(f)
    
    Header = "State\tD%\tR%"
    if(Include3rd):
        Header += "\t3%"
    Header += "\tSeats\tD X\tR X"
    if(Include3rd):
        Header += "\t3 X"
    Header += "\tD A\tR A "
    if(Include3rd):
        Header += "\t3 A "
    Header += "\t\tOverrepresentations"
    
    print(Header)
    
    OverCount =[0,0,0]
    StateCount =[[] for i in range(3)]
    for State in data.keys():
        stateInfo = StateInfo(State, data[State])
        if(Debug):
            stateInfo.DebugPrintSeatsA()
            stateInfo.DebugPrintPercents()
        FormattedInformation = FormatStateInfo(stateInfo)
        print(FormattedInformation[0])
        Count = FormattedInformation[1]
        for i in range(3):
            OverCount[i] += len(Count[i])
            for state in Count[i]:
                StateCount[i].append(state)
    BothStateCount = ListIntersection(StateCount[0], StateCount[1])
    print("OverRepCounts\nDem\t{0:2}\t{1:100}\nRep\t{2:2}\t{3}\nBoth\t{4:2}\t{5}"
          .format(OverCount[0], ", ".join(StateCount[0]), OverCount[1],
                  ", ".join(StateCount[1]), len(BothStateCount), ", ".join(BothStateCount)))
        
def FormatStateInfo(stateInfo):
    
        StateInformation = "{0:5}".format(stateInfo.State)
        StateInformation += "\t{0:2}".format(stateInfo.PercentDem)
        StateInformation += "\t{0:2}".format(stateInfo.PercentRep)
        if(Include3rd):
            StateInformation += "\t{0:2}".format(stateInfo.Percent3rd)
        StateInformation += "\t{0:5}".format(stateInfo.SeatsSum)
        StateInformation += "\t{0:3}".format(stateInfo.SeatsDemX)
        StateInformation += "\t{0:3}".format(stateInfo.SeatsRepX)
        if(Include3rd):
            StateInformation += "\t{0:3}".format(stateInfo.Seats3rdX)
        StateInformation += "\t{0:3}".format(stateInfo.SeatsDemA)
        StateInformation += "\t{0:3}".format(stateInfo.SeatsRepA)
        if(Include3rd):
            StateInformation += "\t{0:3}".format(stateInfo.Seats3rdA)

        overD = "\t"
        overR = "\t"
        over3 = "\t"
        Count =[[] for i in range(3)]
        
        if(stateInfo.SeatsDemA > stateInfo.SeatsDemX):
            overD += "Dem"
            Count[0].append(stateInfo.State)
            
        if(stateInfo.SeatsRepA > stateInfo.SeatsRepX):
            overR += "Rep"
            Count[1].append(stateInfo.State)
            
        if(Include3rd and stateInfo.Seats3rdA > stateInfo.Seats3rdX):
            over3 += "3rd"
            Count[2].append(stateInfo.State)
            
        StateInformation += "{0:3} {1:3} {2:3}".format(overD, overR, over3)
        return [StateInformation, Count]
    
def ListIntersection(L1, L2):
    L3 = [value for value in L1 if value in L2]
    return L3

def GetRemainder(Val):
    return Val - math.floor(Val)

if __name__ == "__main__":
    main()
