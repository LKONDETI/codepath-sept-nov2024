#problem 1
def most_endangered(species_list):
    if not species_list:
        return None
    
    min_population = species_list[0]["population"]
    endangered_species = species_list[0]["name"]

    for species in species_list:
        if species["population"] < min_population:
            min_population = species["population"]
            endangered_species = species["name"]
    
    return endangered_species


species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]
#print(most_endangered(species_list))

#problem 2

def count_endangered_species(endangered_species, observed_species):
    species = set()
    count = 0
    for char in endangered_species:
        species.add(char)
    for i in observed_species:
        if i in species:
            count += 1
    return count
endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

#print(count_endangered_species(endangered_species1, observed_species1)) 
#print(count_endangered_species(endangered_species2, observed_species2))  

#problem 3
def navigate_research_station(station_layout, observations):
    time = 0
    station_indices = {}

    for index in range(0,26):
        station_indices[station_layout[index]] = index

    current_index = 0

    for obs in observations:
        next_index = station_indices[obs]
        time += abs(current_index - next_index)
        current_index = next_index

    return time

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

#print(navigate_research_station(station_layout1, observations1))  
#print(navigate_research_station(station_layout2, observations2))

#problem 4

def prioritize_observations(observed_species, priority_species):
    
    priority_count = {species: 0 for species in priority_species}
    remaining_species = []
    
    for species in observed_species:
        if species in priority_count:
            priority_count[species] += 1
        else:
            remaining_species.append(species)
    
    
    result = []
    for species in priority_species:
        result.extend([species] * priority_count[species])
    
    
    result.extend(sorted(remaining_species))
    
    return result


observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 


    