'''
def lineup(artists, set_times):
    return dict(zip(artists, set_times))

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))

#problem2
def get_artist_info(artist, festival_schedule):
    if artist in festival_schedule:
        return festival_schedule[artist]
    else:
        return {'message':'Artist not found'}
festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  

#problem3
def total_sales(ticket_sales):
    return sum(ticket_sales.values())
ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))

#problem 4
def identify_conflicts(venue1_schedule, venue2_schedule):
    conflicts = {artist: time for artist, time in venue1_schedule.items() 
                 if artist in venue2_schedule and venue2_schedule[artist] == time}
    return conflicts
    

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))
'''

#problem 5
def best_set(votes):
    












'''
def most_endangered(species_list):

    endager_species = species_list[0] # Set the most endaged species to be the first element

    for name in species_list:
        if endager_species["population"] > species_list["population"]:
            endager_species = endager_species["name"]

    return endager_species
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
print(most_endangered(species_list))
'''