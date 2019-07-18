###################################
## Gallup Poll State Information ##
## Created On: 07.17.19          ## 
## Updated On: 07.17.19          ##
###################################

class StateInformation:
    # state     : String name of the state
    # population: Integer value of the amount of voters of the state
    # democratic: Integer value of the percent of democratic voters
    # republican: Integer value of the percent of republican voters
    def __init__(self, state, population, democratic, republican):
        self.State = state
        self.Population = population
        self.Democratic = democratic
        self.Republican = republican
        self.Independent = 100 - int(democratic) - int(republican)

    def ToString(self):
        toString = "Location: " + self.State
        toString += "\n> Democratic: " + str(self.Democratic)
        toString += "\n> Republican: " + str(self.Republican)
        toString += "\n> Independent: " + str(self.Independent)
        toString += "\n> Population: " + str(self.Population)
        return toString
