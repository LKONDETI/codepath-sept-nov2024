
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

#problem 6

def edit_post(post):
    words = post.split()
   
    reversed_words = [word[::-1] for word in words]
 
    return ' '.join(reversed_words)

#print(edit_post("Boost your engagement with these tips")) 
#print(edit_post("Check out my latest vlog")) 

#problem 7

def post_compare(draft1, draft2):
    def process_draft(draft):
        result = []
        for char in draft:
            if char == "#":
                if result:
                    result.pop() 
            else:
                result.append(char)
        return ''.join(result)

    return process_draft(draft1) == process_draft(draft2)

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 
'''
def post_compare(draft1, draft2):
    draft1 = draft1.split()
    draft2 = draft2.split()
    count1 = 0
    count2 = 0
    for i in draft1:
        if i == "#":
            count1 += 1

    for j in draft2:
        if j == "#":
            count2 += 1
    if count1 == count2:
        return True
    else:
        return False
'''


        
    

    