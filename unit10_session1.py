# problem 1
flights = {
    "JFK": ["DFW", "LAX"],
    "LAX": ["JFK"],
    "DFW": ["ATL", "JFK"],
    "ATL": ["DFW"]
}

#problem2

def bidirectional_flights(flights):
    for airport in range(len(flights)): 
        for destination in flights[airport]: 
            print("Airport is: " + str(airport))
            print("Destination is: " + str(destination))
            print("Flights[destination] is " + str(flights[destination]))
            if not airport in flights[destination]: 
                return False
    return True

flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

#print(bidirectional_flights(flights1))
#print(bidirectional_flights(flights2))

#problem 4
    
