'''
# UMPIRE strategy
1. understand
2. match
3. plan
4. implement 
5. review 
6. evaluate

# Remove all dupilicate adjustments

def check_oxygen_levels(oxygen_levels):
    stack = []
    for c in oxygen_levels:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)

#oxygen_levels = "abbaca"
oxygen_levels = "azxxzy"
# Time and Space complexity: O(n)
print (check_oxygen_levels(oxygen_levels))

def process_performance_requests(requests):
    requests.sorted()  

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))
'''

def collect_festival_points(points):
    total = 0
    while points:
        total += points.pop()
    return total

print(collect_festival_points([5, 8, 3, 10])) 
print(collect_festival_points([2, 7, 4, 6])) 
print(collect_festival_points([1, 5, 9, 2, 8])) 