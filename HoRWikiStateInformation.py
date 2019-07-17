################################
## HoR Wiki State Information ##
## Created On: 07.17.19       ## 
## Updated On: 07.17.19       ##
################################

class StateInformation:
    # state          : String name of the state
    # seatsTotal     : Integer value of the amount of active seats of the state
    # seatsDemocratic: Integer value of the democratic seats active
    # seatsRepublican: Integer value of the republican seats active
    def __init__(self, state, seatsTotal, seatsDemocratic, seatsRepublican):
        self.State = state
        self.Total = seatsTotal
        self.Democratic = seatsDemocratic
        self.Republican = seatsRepublican

    def ToString(self):
        toString = "Location: " + self.State
        toString += "\n> Total: " + str(self.Total)
        toString += "\n> Democratic: " + str(self.Democratic)
        toString += "\n> Republican: " + str(self.Republican)
        return toString
