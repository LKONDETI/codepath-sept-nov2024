# factorial of the n using recursive
def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial(n-1)
#print(factorial(5))

# sum of the n using recursive
def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursive(n-1)
#print(sum_recursive(5))

# [1,2,3,4,5], output = 15 -> edge case: [] None 
# write a recursive function that calculates the sum of all elements in alist

def resursive_sum(arr):
    if not arr:
        return 0
    return arr[0] + resursive_sum(arr[1: ])

arr = [1,2,3,4,5]
#print(resursive_sum(arr))
#[1,2,3,4,5]
#[2,3,4,5]
#[3,4,5]
#[4,5]
#[5]

# problem 1
def count_suits_iterative(suits):
    count = 0
    for suit in suits:
        count +=1
    return count
def count_suits_recursive(suits):
    if not suits:
        return 0
    return 1+ count_suits_recursive(suits[1:])
#print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
#print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))
#problem 2
def sum_stones(stones):
    if not stones:
        return 0
    return stones[0] + sum_stones(stones[1: ])

print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))

#problem3
def count_suits_iterative(suits):
    count = 0
    unique_suits = []
    for suit in suits:
        if suit not in unique_suits:
            unique_suits.append(suit)
            count += 1
    return count

def count_suits_recursive(suits):
    if not suits:
        return 0
    if suits[0] in suits[1:]:
        suits.pop(0)
        return count_suits_recursive(suits)
    else:
        return 1 + count_suits_recursive(suits[1:])

#print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
#print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))

#problem 4
def fibonacci_growth(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci_growth(n-1) + fibonacci_growth(n-2)

#print(fibonacci_growth(5))
#print(fibonacci_growth(8))

#problem 5

def power_of_four(n):
    if n == 0:
        return 1
    elif n > 0:
        return 4 * power_of_four(n-1)
    else:
        return 1/ (power_of_four(-n))

#print(power_of_four(2))
#print(power_of_four(-2))

#problem 6  
def strongest_avenger(strengths):
    if len(strengths) == 1:
        return strengths[0]
    
    maximum = strongest_avenger(strengths[1:])

    return strengths[0] if strengths[0] > maximum else maximum

#print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
#print(strongest_avenger([50, 75, 85, 60, 90]))

#problem 7

def count_deposits(resources):
    if not resources:
        return 0
    count = 1 if resources[0] == 'V' else 0
    return count + count_deposits(resources[1: ])
print(count_deposits("VVVVV"))
print(count_deposits("VXVYGA"))

