#####################################
## Party Representation Plot Utils
#####################################

import matplotlib.pyplot as plt
import numpy as np

DEMOCRATIC_KEY = "Democratic"
REPUBLICAN_KEY = "Republican"
INDEPENDENT_KEY = "Independent"
WITH_INDEPENDENT_KEY = "with_independents"
WITHOUT_INDEPENDENT_KEY = "without_independents"

def plot_democratic_representation_with_independents(party_representation):
    stateList = list(party_representation.keys())
    democratic_representation = list()
    democratic_sorted_state_list = sorted(stateList, key=lambda item: party_representation[item][WITH_INDEPENDENT_KEY][DEMOCRATIC_KEY], reverse=True)
    
    for state in democratic_sorted_state_list:
        democratic_representation.append(party_representation[state][WITH_INDEPENDENT_KEY][DEMOCRATIC_KEY])
        
    build_plot(democratic_sorted_state_list, democratic_representation, "blue", "Democratic Representation W/ Ind.s", "Democratic Representation")
    
def plot_republican_representation_with_independents(party_representation):
    stateList = list(party_representation.keys())
    republican_representation = list()
    republican_sorted_state_list = sorted(stateList, key=lambda item: party_representation[item][WITH_INDEPENDENT_KEY][REPUBLICAN_KEY], reverse=True)
        
    for state in republican_sorted_state_list:
        republican_representation.append(party_representation[state][WITH_INDEPENDENT_KEY][REPUBLICAN_KEY])
        
    build_plot(republican_sorted_state_list, republican_representation, "red", "Republican Representation W/ Ind.s", "Republican Representation")
       
        
def plot_independent_representation_with_independents(party_representation):
    stateList = list(party_representation.keys())
    independent_representation = list()
    independent_sorted_state_list = sorted(stateList, key=lambda item: party_representation[item][WITH_INDEPENDENT_KEY][INDEPENDENT_KEY], reverse=True)
    
    for state in independent_sorted_state_list:
        independent_representation.append(party_representation[state][WITH_INDEPENDENT_KEY][INDEPENDENT_KEY])
        
    build_plot(independent_sorted_state_list, independent_representation, "grey", "Independent Representation W/ Ind.s", "Independent Representation")
    
def plot_democratic_representation_without_independents(party_representation):
    stateList = list(party_representation.keys())
    democratic_representation = list()
    democratic_sorted_state_list = sorted(stateList, key=lambda item: party_representation[item][WITHOUT_INDEPENDENT_KEY][DEMOCRATIC_KEY], reverse=True)
    
    for state in democratic_sorted_state_list:
        democratic_representation.append(party_representation[state][WITHOUT_INDEPENDENT_KEY][DEMOCRATIC_KEY])
        
    build_plot(democratic_sorted_state_list, democratic_representation, "blue", "Democratic Representation W/O Ind.s", "Democratic Representation")

def plot_republican_representation_without_independents(party_representation):
    stateList = list(party_representation.keys())
    republican_representation = list()
    republican_sorted_state_list = sorted(stateList, key=lambda item: party_representation[item][WITHOUT_INDEPENDENT_KEY][REPUBLICAN_KEY], reverse=True)
        
    for state in republican_sorted_state_list:
        republican_representation.append(party_representation[state][WITHOUT_INDEPENDENT_KEY][REPUBLICAN_KEY])
        
    build_plot(republican_sorted_state_list, republican_representation, "red", "Republican Representation W/O Ind.s", "Republican Representation")

def build_plot(y_values, x_values, color, title, x_label):    
    # Logistics for the plt
    plt.rcdefaults()
    fig, ax = plt.subplots()
    fig.set_size_inches(20, 15)
    ax.barh(y_values, x_values, align='center', color=color)
    yTickCount = np.arange(len(y_values))
    ax.set_yticks(yTickCount)
    ax.set_yticklabels(y_values)
    ax.set_title(title)
    ax.set_ylabel('State')
    ax.set_xlabel(x_label)
    ax.invert_yaxis()  # labels read top-to-bottom
    # Iterate over the y-Values
    for i, v in enumerate(x_values):
        # Display the text on the bar
        ax.text(v, i + 0.2, "{:.2f}%".format(v))
    # Display the Plot
    plt.show()