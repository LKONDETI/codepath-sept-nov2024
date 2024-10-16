
#The _ placeholder is used to ignore the index returned by enumerate. We only care about the item itself
def reverse_sentence(sentence):
    splited = sentence.split()
    reverse = []
    for _, item in enumerate(splited):
        reverse.append(item)
    return ' '.join(reverse)
#sentence = "tubby little cubby all stuffed with fluff"
sentence = "Pooh"
print(reverse_sentence(sentence))

def goldilocks_approved(nums):
    nums.sort()
    for item in nums:
        if min(nums) < item < max(nums):
            return item
    return -1
#nums = [3, 2, 1, 4]
#nums = [1,2]
nums = [3, 2, 1]
print(goldilocks_approved(nums))

def delete_minimum_elements(hunny_jar_sizes):
	#hunny_jar_sizes.sort()
    result = []
    while hunny_jar_sizes:
        min_index = hunny_jar_sizes.index(min(hunny_jar_sizes))
        result.append(hunny_jar_sizes.pop(min_index))
    return result

#hunny_jar_sizes = [5, 3, 2, 4, 1]
hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))

def sum_of_digits(num):
    lst = map(int, str(num))
    return sum(lst)
#num = 423
#num = 123123234
num = 4
print(sum_of_digits(num))

def final_value_after_operations(operations):
	trigger = 1
	for item in operations:
		if item == "bouncy":
			trigger +=1
		elif item == "flouncy":
			trigger +=1
		elif item == "trouncy":
			trigger -=1
		elif item == "pouncy":
			trigger -=1
	return trigger

#operations = ["trouncy", "flouncy", "flouncy"]
operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))

def is_acronym(words, s):
    for i, char in enumerate(s):
        if words[i][0].lower() != char.lower():
            return False
    return True


words = ["christopher", "robin", "milne"]
s = "crm"
print(is_acronym(words, s))

def make_divisible_by_3(nums):
    count = 0
    for item in nums:
        if item % 3 != 0:
            count += 1
    return count

#nums = [1, 2, 3, 4]
nums = [3, 6, 9]
print(make_divisible_by_3(nums))

def exclusive_elemts(lst1, lst2):
	lst = lst1 +lst2
	for item1 in lst1:
		for item2 in lst2:
			if item1 == item2:
				lst.remove(item1)
				lst.remove(item2)
			
	return lst
#lst1 = ["pooh", "roo", "piglet"]
#lst2 = ["piglet", "eeyore", "owl"]
#lst1 = ["pooh", "roo"]
#lst2 = ["piglet", "eeyore", "owl", "kanga"]
lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
print(exclusive_elemts(lst1, lst2))

def merge_alternately(word1, word2):
    merged = ""
    length_word1 = len(word1)
    length_word2 = len(word2)
    max_length = max(length_word1, length_word2)
    for i in range(max_length):
        if i < length_word1:
            merged += word1[i]
        if i < length_word2:
            merged += word2[i]
    
    return merged
#word1 = "wol"
#word2 = "oze"
word1 = "hfa"
word2 = "eflump"
print(merge_alternately(word1, word2)) 

def good_pairs(pile1, pile2, k):
    count = 0
    for i in range(0 , len(pile1)):
        for j in range(0 , len(pile2)):
            modified_pile2 = pile2[j] * k
            if pile1[i] % modified_pile2 == 0:
                count += 1
                
    return count
#pile1 = [1, 3, 4]
#pile2 = [1, 3, 4]
#k = 1
pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))

    



