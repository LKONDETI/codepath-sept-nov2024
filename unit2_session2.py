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

    