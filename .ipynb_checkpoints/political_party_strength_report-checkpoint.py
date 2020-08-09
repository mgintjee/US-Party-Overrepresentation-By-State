#####################################
## Political Party Strength Report
#####################################

import math, random

DEMOCRATIC_KEY = "Democratic"
REPUBLICAN_KEY = "Republican"
INDEPENDENT_KEY = "Independent"
MID_THRESHOLD = 0.5

class report:
    # state           : string value of the name of the state
    # democratic_seats : int value of the democratic seats active
    # democratic_support : float value of the democratic support throughout the state
    # republican_seats: int value of the republican seats active
    # republican_support : float value of the republican support throughout the state
    # independent_seats: int value of the independent seats active
    # independent_support : float value of the independent support throughout the state
    def __init__(self, state, democratic_seats, democratic_support, republican_seats, republican_support, independent_seats, independent_support):
        self.state = state
        self.democratic_seats = democratic_seats
        self.democratic_support = democratic_support
        self.republican_seats = republican_seats
        self.republican_support = republican_support
        self.independent_seats = independent_seats
        self.independent_support = independent_support
        self.total_seats = self.democratic_seats + self.republican_seats + self.independent_seats
        self.actual_seats = self.build_actual_seats()
        self.expected_seats_with_independents = self.build_expected_seats_with_independents()
        self.expected_seats_without_independents = self.build_expected_seats_without_independents()

    def to_string(self):
        toString = "state: " + self.state
        toString += "\n>democratic_seats: " + str(self.democratic_seats)
        toString += "\n>democratic_support: " + str(self.democratic_support)
        toString += "\n>republican_seats: " + str(self.republican_seats)
        toString += "\n>republican_support: " + str(self.republican_support)
        toString += "\n>independent_seats: " + str(self.independent_seats)
        toString += "\n>independent_support: " + str(self.independent_support)
        return toString
    
    # Should Return a dict in a similar format to the following:
    # D["Democratic"] = X
    # D["Republican"] = Y
    # D["Independent"] = Z
    def build_actual_seats(self):
        dict_of_seats = dict()
        dict_of_seats[DEMOCRATIC_KEY] = self.democratic_seats
        dict_of_seats[REPUBLICAN_KEY] = self.republican_seats
        dict_of_seats[INDEPENDENT_KEY] = self.independent_seats
        return dict_of_seats
        
    def get_state(self):
        return self.state
    
    def get_total_seats(self):
        return self.total_seats
    
    def get_actual_seats(self):
        return self.actual_seats
    
    def get_expected_seats_with_independents(self):
        return self.expected_seats_with_independents
    
    def get_expected_seats_without_independents(self):
        return self.expected_seats_without_independents
        
    # Should Return a dict in a similar format to the following:
    # D["Democratic"] = X
    # D["Republican"] = Y
    # D["Independent"] = Z
    def build_expected_seats_with_independents(self):
        dict_of_seats = dict()
        dict_of_seats[DEMOCRATIC_KEY] = 0
        dict_of_seats[REPUBLICAN_KEY] = 0
        dict_of_seats[INDEPENDENT_KEY] = 0
        
        seats_remaining = self.total_seats

        print("\nState=", self.state, ", Total Seats=", self.total_seats, "\n")
        while(seats_remaining > 0):
            print("Seats Remaining=", seats_remaining)
            expected_democratic_seats_float = seats_remaining * int(self.democratic_support)/100
            expected_republican_seats_float = seats_remaining * int(self.republican_support)/100
            expected_independent_seats_float = seats_remaining * int(self.independent_support)/100
            print("expected_democratic_seats_float=", expected_democratic_seats_float)
            print("expected_republican_seats_float=", expected_republican_seats_float)
            print("expected_independent_seats_float=", expected_independent_seats_float)
            
            expected_democratic_seats_int = math.floor(expected_democratic_seats_float)
            expected_republican_seats_int = math.floor(expected_republican_seats_float)
            expected_independent_seats_int = math.floor(expected_independent_seats_float)

            if(expected_democratic_seats_int == 0 and
               expected_republican_seats_int == 0 and
               expected_independent_seats_int == 0):

                expected_seats_float_list = [expected_democratic_seats_float, expected_republican_seats_float, expected_independent_seats_float]
                max_expected_seats_float = max(expected_seats_float_list)
                
                if(seats_remaining == 1):
                    
                    if(max_expected_seats_float == expected_democratic_seats_float):
                        expected_democratic_seats_int += 1
                        
                    elif(max_expected_seats_float == expected_republican_seats_float):
                        expected_republican_seats_int += 1
                        
                    elif(max_expected_seats_float == expected_independent_seats_float):
                        expected_independent_seats_int += 1
                        
                    else:
                        # In the unlikely event there is a tie, we will flip a coin
                        coin_flip = random.choice([DEMOCRATIC_KEY, REPUBLICAN_KEY, INDEPENDENT_KEY])
                        if(coin_flip == DEMOCRATIC_KEY):
                            expected_democratic_seats_int += 1
                            
                        elif(coin_flip == REPUBLICAN_KEY):
                            expected_republican_seats_int += 1
                            
                        else:
                            expected_independent_seats_int += 1
                        
                elif(seats_remaining == 2):
                    
                    if(max_expected_seats_float == expected_democratic_seats_float):
                        expected_seats_float_list.remove(expected_democratic_seats_float)
                        expected_democratic_seats_int += 1
                        
                    elif(max_expected_seats_float == expected_republican_seats_float):
                        expected_seats_float_list.remove(expected_republican_seats_float)
                        expected_republican_seats_int += 1
                        
                    elif(max_expected_seats_float == expected_independent_seats_float):
                        expected_seats_float_list.remove(expected_independent_seats_float)
                        expected_independent_seats_int += 1
                        
                    max_expected_seats_float = max(expected_seats_float_list) 
                    
                    if(max_expected_seats_float == expected_democratic_seats_float):
                        expected_democratic_seats_int += 1
                        
                    elif(max_expected_seats_float == expected_republican_seats_float):
                        expected_republican_seats_int += 1
                        
                    elif(max_expected_seats_float == expected_independent_seats_float):
                        expected_independent_seats_int += 1
                    
                else:
                    if(expected_democratic_seats_float > MID_THRESHOLD):
                        expected_democratic_seats_int += 1
                    if(expected_republican_seats_float > MID_THRESHOLD):
                        expected_republican_seats_int += 1
                    if(expected_independent_seats_float > MID_THRESHOLD):
                        expected_independent_seats_int += 1

            dict_of_seats[DEMOCRATIC_KEY] += expected_democratic_seats_int
            dict_of_seats[REPUBLICAN_KEY] += expected_republican_seats_int
            dict_of_seats[INDEPENDENT_KEY] += expected_independent_seats_int
                        
            seats_remaining -= expected_democratic_seats_int
            seats_remaining -= expected_republican_seats_int
            seats_remaining -= expected_independent_seats_int
            
            print("expected_democratic_seats_int=", expected_democratic_seats_int)
            print("expected_republican_seats_int=", expected_republican_seats_int)
            print("expected_independent_seats_int=", expected_independent_seats_int)
            
        print("\nState=", self.state, ", Seats Remaining=", seats_remaining, "\n")
        return dict_of_seats

    # Should Return a dict in a similar format to the following:
    # D["Democratic"] = X
    # D["Republican"] = Y
    # D["Independent"] = 0
    def build_expected_seats_without_independents(self):
        dict_of_seats = dict()
        dict_of_seats[DEMOCRATIC_KEY] = 0
        dict_of_seats[REPUBLICAN_KEY] = 0
        dict_of_seats[INDEPENDENT_KEY] = 0

        seats_remaining = self.total_seats

        print("\nState=", self.state, ", Total Seats=", self.total_seats, "\n")
        while(seats_remaining > 0):
            print("Seats Remaining=", seats_remaining)
            expected_democratic_seats_float = seats_remaining * int(self.democratic_support)/(self.democratic_support + self.republican_support)
            expected_republican_seats_float = seats_remaining * int(self.republican_support)/(self.democratic_support + self.republican_support)
            print("expected_democratic_seats_float=", expected_democratic_seats_float)
            print("expected_republican_seats_float=", expected_republican_seats_float)
            
            expected_democratic_seats_int = math.floor(expected_democratic_seats_float)
            expected_republican_seats_int = math.floor(expected_republican_seats_float)

            if(expected_democratic_seats_int == 0 and
               expected_republican_seats_int == 0):
                if(seats_remaining == 1):
                    if(expected_democratic_seats_float > expected_republican_seats_float):
                        expected_democratic_seats_int += 1
                    elif(expected_republican_seats_float > expected_democratic_seats_float):
                        expected_republican_seats_int += 1
                    else:
                        # In the unlikely event there is a tie, we will flip a coin
                        coin_flip = random.choice([DEMOCRATIC_KEY, REPUBLICAN_KEY])
                        if(coin_flip == DEMOCRATIC_KEY):
                            expected_democratic_seats_int += 1
                        else:
                            expected_republican_seats_int += 1
                else:
                    if(expected_democratic_seats_float > MID_THRESHOLD):
                        expected_democratic_seats_int += 1
                    if(expected_republican_seats_float > MID_THRESHOLD):
                        expected_republican_seats_int += 1
            
            dict_of_seats[DEMOCRATIC_KEY] += expected_democratic_seats_int
            dict_of_seats[REPUBLICAN_KEY] += expected_republican_seats_int
                        
            seats_remaining -= expected_democratic_seats_int
            seats_remaining -= expected_republican_seats_int
            
            print("expected_democratic_seats_int=", expected_democratic_seats_int)
            print("expected_republican_seats_int=", expected_republican_seats_int)
            
        print("\nState=", self.state, ", Seats Remaining=", seats_remaining, "\n")
        return dict_of_seats
