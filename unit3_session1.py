
def unique_counts(souvenirs) :
    hashMap = {}
    for i in souvenirs:
        hashMap[i] = 1 + hashMap.get(i, 0) # { "keychain": 1, "hat" : 2 }
    return len(list(hashMap.values())) == len(list(set(hashMap.values())))


#souvenirs = ["keychain", "magnet","hat", "candy"]
souvenirs = ["keychain", "hat","hat", "keychain", "keychain", "postcard"]
#print(unique_counts(souvenirs))
# Dat structures Applicable
# - dictionary
# - set
# - List/Array
# space complexity: O(n)

# Problem 1
def is_valid_post_format(posts):
    stack = []
    opening_tags = {"(", ")","{}"}

#print(is_valid_post_format("()"))
#print(is_valid_post_format("()[]{}")) 
#print(is_valid_post_format("(]"))

#problem 3
def is_symmetrical_title(title):
    title = title.lower()
    title = title.replace(" ", "")
    left, right = 0 , len(title)-1 
    while left < right:
        if title[left] != title[right]:
            return False
        else:
            left += 1
            right -=1
    return True

#print(is_symmetrical_title("A Santa at NASA"))
#print(is_symmetrical_title("Social Media")) 

#problem 2

def reverse_comments_queue(comments):
    reverse_queue = []
    while comments:
        element = comments.pop()
        reverse_queue.append(element)

    return reverse_queue

#print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

#print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

#problem 4




    