#write a function that takes an array of numbers and returns the sum of the numbers
'''
def sum(arr):
    i = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            arr[j] = arr[i] + arr[j]
    return arr[j]

print(sum([1,2,1]))'''

#write a function that finds the longest word in a list  of words
#write a function that determines if a string is balance

class TreeNode():
     def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right

def merge_orders(order1, order2):
    if not order1 and not order2:
        return None
    if not order1 and order2:
        return order1
#time and space: O(n+m)

#problem 2
# time and space complixity: O(n)

#problem 3
#time complixity: O(n)
#space complixity:O(1) logn = n =2 because it has two recursions 

#problem 4


