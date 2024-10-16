
def welcome():
	print("Welcome to The Hundred Acre Wood!")
welcome()

def greetings(name):
	print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

greetings("Michael")
greetings("Winnie the Pooh")

def print_catchphrase(character):
	if character == "Pooh":
		print("Oh bother!")
	elif character == "Tigger":
		print("TTFN: Ta-ta for now!")
	elif character == "Eeyore":
		print("Thanks for noticing me.")
	elif character == "Christopher Robin":
		print("Silly old bear.")
	else:
		print(f"Sorry! I don't know {character}'s catchphrase!")
		
#character = "Pooh"
#print_catchphrase(character)
character = "Piglet"
print_catchphrase(character)
def get_item(items, x):
	if x > len(items):
		return None
	else:
		return items[x]
	
#items = ["piglet", "pooh", "roo", "rabbit"]
#x = 5
items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
print(get_item(items, x))	 
def sum_honey(hunny_jars):
	i = 0 
	for items in hunny_jars: 
		i += items
	return i
#hunny_jars = [2, 3, 4, 5]
hunny_jars = []
print(sum_honey(hunny_jars))
def doubled(hunny_jars):
	i = []
	for items in hunny_jars: 
		i.append(items * 2)
	return i
hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))	
def count_less_than(race_times, threshold):
	count = 0
	for race in race_times:
		if race < threshold:
			count += 1
	return count
#race_times = [1, 2, 3, 4, 5, 6]
#threshold = 4
#race_times = []
#threshold = 4
race_times = [1,2,3,4,5,6,7,3]
threshold = 6
print(count_less_than(race_times, threshold))
def print_todo_list(task):
	print("Pooh's To Dos:")
	for i , item in enumerate(task, start = 1):
		print(f"{i}.{item}")
task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print(print_todo_list(task))
def can_pair(item_quantities):
	for item in item_quantities:
		if item%2 != 0:
			return False
	return True
#item_quantities = [2, 4, 6, 8]
#item_quantities = [1, 2, 3, 4]
item_quantities = []
print(can_pair(item_quantities))
def split_haycorns(quantity):
	factors = []
	for i in range(1, quantity+1):
		if quantity % i == 0:
			factors.append(i)
	return factors
#quantity = 6
#quantity = 1
quantity = 2
print(split_haycorns(quantity))
def tiggerfy(s):
	s = s.lower()
	splitted = list(s)
	to_remove = ["t" , "i", "g", "e", "r"]
	result = [char for char in splitted if char not in to_remove]
	return "".join(result)
#s = "suspicerous"
#s = "Trigger"
s = "Hunny"
print(tiggerfy(s))
def locate_thistles(items):
	indexes = []
	for i in range(0,len(items)):
		if items[i] == "thistle":
			indexes.append(i)
	return indexes
#items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))



