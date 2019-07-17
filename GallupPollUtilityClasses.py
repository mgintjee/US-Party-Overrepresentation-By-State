###################################
## Gallup Poll State Information ##
## Created On: 07.17.19          ## 
## Updated On: 07.17.19          ##
###################################

class StateInformation:
    # state     : String name of the state
    # democratic: Integer value of the democratic voters
    # republican: Integer value of the republican voters
    def __init__(self, state, democratic, republican):
        self.State = state
        self.DemocraticVotes = democratic
        self.RepublicanVotes = republican
