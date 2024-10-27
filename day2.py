
def lineup(artists, set_times):
    return dict(zip(artists, set_times))

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

#print(lineup(artists1, set_times1))
#print(lineup(artists2, set_times2))

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

#print(get_artist_info("Blood Orange", festival_schedule)) 
#print(get_artist_info("Taylor Swift", festival_schedule))  

#problem3
def total_sales(ticket_sales):
    return sum(ticket_sales.values())
ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

#print(total_sales(ticket_sales))

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

#print(identify_conflicts(venue1_schedule, venue2_schedule))


#problem 5
def best_set(votes):
    vote_counts = {}
    for artist in votes.values():
        if artist in vote_counts:
            vote_counts[artist] += 1
        else:
            vote_counts[artist] = 1
    
    max_votes = 0
    best_artist = None
    for artist, count in vote_counts.items():
        if count > max_votes:
            max_votes = count
            best_artist = artist
    
    return best_artist
votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

#print(best_set(votes1))
#print(best_set(votes2))

#problem 6
'''
def max_audience_performances(audiences):
    max_audience = max(audiences)
    total_sum_max_audience = sum(i for i in audiences if i == max_audience)
    return total_sum_max_audience

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]'''

#print(max_audience_performances(audiences1))
#print(max_audience_performances(audiences2))

#problem 7
def max_audience_performances(audiences):
    if not audiences:
        return []

    max_audience = audiences[0]
    total_max_audience = 0

    for audience in audiences:
        if audience > max_audience:
            max_audience = audience
            total_max_audience = audience
        elif audience == max_audience:
            total_max_audience += audience

    return total_max_audience

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]
#print(max_audience_performances(audiences1))
#print(max_audience_performances(audiences2))

#problem 8
def num_popular_pairs(popularity_scores):
    score_count = {}
    pairs = 0
    for score in popularity_scores:
        if score in score_count:
            pairs += score_count[score]
            score_count[score] += 1
        else:
            score_count[score] = 1

    return pairs

popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

#print(num_popular_pairs(popularity_scores1))
#print(num_popular_pairs(popularity_scores2))
#print(num_popular_pairs(popularity_scores3)) 

#problem 9
def find_stage_arrangement_difference(s, t):
    index_map = {performer: idx for idx, performer in enumerate(s)}
    total_difference = 0

    for idx, performer in enumerate(t):
        original_index = index_map[performer]
        total_difference += abs(original_index - idx)
    
    return total_difference
s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

#print(find_stage_arrangement_difference(s1, t1))
#print(find_stage_arrangement_difference(s2, t2))

# problem 10
def num_VIP_guests(vip_passes, guests):
    vip_set = set()
    count = 0
    for char in vip_passes:
        vip_set.add(char)
    for i in guests:
        if i in vip_set:
            count += 1
    return count

vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

#print(num_VIP_guests(vip_passes1, guests1))
#print(num_VIP_guests(vip_passes2, guests2))

#problem 11
def schedule_pattern(pattern, schedule):
    
    genres = schedule.split()

    if len(genres) != len(pattern):
        return False

    char_to_genre = {}
    genre_to_char = {}

    for char, genre in zip(pattern, genres):
        if char in char_to_genre:
            if char_to_genre[char] != genre:
                return False
        else:
            char_to_genre[char] = genre

        if genre in genre_to_char:
            if genre_to_char[genre] != char:
                return False
        else:
            genre_to_char[genre] = char

    return True


pattern1 = "abba"
schedule1 = "rock jazz jazz rock"

pattern2 = "abba"
schedule2 = "rock jazz jazz blues"

pattern3 = "aaaa"
schedule3 = "rock jazz jazz rock"

print(schedule_pattern(pattern1, schedule1))
print(schedule_pattern(pattern2, schedule2))
print(schedule_pattern(pattern3, schedule3))

#problem 12
def sort_performers(performer_names, performance_times):
    combined = list(zip(performance_times, performer_names))
    combined.sort(key=lambda x: x[0], reverse=True)
    sorted_names = [name for _, name in combined]
    
    return sorted_names
performer_names1 = ["Mary", "John", "Emma"]
performance_times1 = [180, 165, 170]

performer_names2 = ["Alice", "Bob", "Bob"]
performance_times2 = [155, 185, 150]

print(sort_performers(performer_names1, performance_times1)) 
print(sort_performers(performer_names2, performance_times2))









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
#print(most_endangered(species_list))
