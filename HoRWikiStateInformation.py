################################
## HoR Wiki State Information ##
## Created On: 07.17.19       ## 
## Updated On: 07.17.19       ##
################################

class StateInformation:
    # state           : String name of the state
    # seatsDemocratic : Integer value of the democratic seats active
    # seatsRepublican : Integer value of the republican seats active
    # seatsIndependent: Integer value of the independent seats active
    def __init__(self, state, seatsDemocratic, seatsRepublican, seatsIndependent):
        self.State = state
        self.Democratic = seatsDemocratic
        self.Republican = seatsRepublican
        self.Independent = seatsIndependent
        self.Total = seatsDemocratic + seatsRepublican + seatsIndependent

    def ToString(self):
        toString = "Location: " + self.State
        toString += "\n> Democratic: " + str(self.Democratic)
        toString += "\n> Republican: " + str(self.Republican)
        toString += "\n> Independent: " + str(self.Independent)
        toString += "\n> Total: " + str(self.Total)
        return toString
