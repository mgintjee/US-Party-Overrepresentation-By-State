# US Party Representation By State
import json

def main():
    print("Hello World")
    
    with open('DataByState.json') as f:
        data = json.load(f)
        
    for State in data.keys():
        print(StateInfoAsString(State, data))

def StateInfoAsString(State, StateData):
    StateInfo = "> " + State
    for Key in StateData[State].keys():
        StateInfo += "\n  > " + Key + ": " + str(StateData[State][Key])
    return StateInfo
            
if __name__ == "__main__":
    main()
