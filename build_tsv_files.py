####################
## Build Tsv Files                
####################

import wiki_political_party_strength_extraction

WITH_INDEPENDENT_TSV_FILE = "tsvFiles/expectedSeatsWithIndependent.tsv"
WITHOUT_INDEPENDENT_TSV_FILE = "tsvFiles/expectedSeatsWithoutIndependent.tsv"
DEMOCRATIC_KEY = "Democratic"
REPUBLICAN_KEY = "Republican"
INDEPENDENT_KEY = "Independent"
WITH_INDEPENDENT_KEY = "with_independents"
WITHOUT_INDEPENDENT_KEY = "without_independents"
TSV_FILE_HEADER = "state\t" + \
"totalSeats\t" + \
"democraticExpectedSeats\t" + \
"democraticActualSeats\t" + \
"democraticRepresentation\t" + \
"republicanExpectedSeats\t" + \
"republicanActualSeats\t" + \
"republicanRepresentation\t" + \
"independentExpectedSeats\t" + \
"independentActualSeats\t" + \
"independentRepresentation\n"

report_set = wiki_political_party_strength_extraction.extract_report_set()

def print_report_set():
    if(len(report_set) < 1):
        print("report_set is empty")
        
    for report in report_set:
        print(report.to_string())
        print("Actual Seats        :", report.get_actual_seats())
        print("Expected Seats (W/) :", report.get_expected_seats_with_independents())
        print("Expected Seats (W/O):", report.get_expected_seats_without_independents())
        
def build_tsv_files():
    tsv_file_with_independent = open(WITH_INDEPENDENT_TSV_FILE, "w+")
    tsv_file_without_independent = open(WITHOUT_INDEPENDENT_TSV_FILE, "w+")
    
    democratic_with_independent_overrepresented_states_dict = dict()
    democratic_without_independent_overrepresented_states_dict = dict()
    republican_with_independent_overrepresented_states_dict = dict()
    republican_without_independent_overrepresented_states_dict = dict()
    
    tsv_file_with_independent.write(TSV_FILE_HEADER)
    tsv_file_without_independent.write(TSV_FILE_HEADER)
    
    # Represents State: with/without independents: party: represnetation
    party_representation = dict()
        
    for report in report_set:
        actual_seats = report.get_actual_seats()
        state = report.get_state()
        total_seats = report.get_total_seats()
        democratic_actual_seats = actual_seats[DEMOCRATIC_KEY]
        republican_actual_seats = actual_seats[REPUBLICAN_KEY]
        independent_actual_seats = actual_seats[INDEPENDENT_KEY]
        
        expected_seats_without_independent = report.get_expected_seats_without_independents()
        
        democratic_expected_seats_without_independent = expected_seats_without_independent[DEMOCRATIC_KEY]
        republican_expected_seats_without_independent = expected_seats_without_independent[REPUBLICAN_KEY]
        
        democratic_representation = round(100 * (democratic_actual_seats - democratic_expected_seats_without_independent) / total_seats, 2)
        republican_representation = round(100 * (republican_actual_seats - republican_expected_seats_without_independent) / total_seats, 2)
        
        party_representation[state] = dict()
            
        party_representation[state][WITHOUT_INDEPENDENT_KEY] = dict()
        party_representation[state][WITHOUT_INDEPENDENT_KEY][DEMOCRATIC_KEY] = democratic_representation
        party_representation[state][WITHOUT_INDEPENDENT_KEY][REPUBLICAN_KEY] = republican_representation
            
        entry_without_independent = state + "\t" + \
            str(total_seats) + "\t" + \
            str(democratic_expected_seats_without_independent) + "\t" + \
            str(democratic_actual_seats) + "\t" + \
            str(democratic_representation) + "\t" + \
            str(republican_expected_seats_without_independent) + "\t" + \
            str(republican_actual_seats) + "\t" + \
            str(republican_representation) + "\n"
        
        tsv_file_without_independent.write(entry_without_independent)
        
        expected_seats_with_independent = report.get_expected_seats_with_independents()
        
        democratic_expected_seats_with_independent = expected_seats_with_independent[DEMOCRATIC_KEY]
        republican_expected_seats_with_independent = expected_seats_with_independent[REPUBLICAN_KEY]
        independent_expected_seats_with_independent = expected_seats_with_independent[INDEPENDENT_KEY]
        
        democratic_representation = round(100 * (democratic_actual_seats - democratic_expected_seats_with_independent) / total_seats, 2)
        republican_representation = round(100 * (republican_actual_seats - republican_expected_seats_with_independent) / total_seats, 2)
        independent_representation = round(100 * (independent_actual_seats - independent_expected_seats_with_independent) / total_seats, 2)
        
        party_representation[state][WITH_INDEPENDENT_KEY] = dict()
        party_representation[state][WITH_INDEPENDENT_KEY][DEMOCRATIC_KEY] = democratic_representation
        party_representation[state][WITH_INDEPENDENT_KEY][REPUBLICAN_KEY] = republican_representation
        party_representation[state][WITH_INDEPENDENT_KEY][INDEPENDENT_KEY] = independent_representation
            
        entry_with_independent = state + "\t" + \
            str(total_seats) + "\t" + \
            str(democratic_expected_seats_with_independent) + "\t" + \
            str(democratic_actual_seats) + "\t" + \
            str(democratic_representation) + "\t" + \
            str(republican_expected_seats_with_independent) + "\t" + \
            str(republican_actual_seats) + "\t" + \
            str(republican_representation) + "\t" + \
            str(independent_expected_seats_with_independent) + "\t" + \
            str(independent_actual_seats) + "\t" + \
            str(independent_representation) + "\n"
        
        tsv_file_with_independent.write(entry_with_independent)
    
    tsv_file_with_independent.close()
    tsv_file_without_independent.close()
    
    return party_representation
