#given an array of integers sorted in non-decreasing order, find and last position of a given target element. If the target is not fount in array, return [-1, -1]
'''
def binarysearch(array, low,high,x):
    if low <= high :
        mid = low +(high - low)//2
        if array[mid]== x:
            return mid
        if array[mid] > x :
            return'''
        
from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sweet_difference(chocolates):
    if not chocolates:
        return []
        
    result = []
    queue = deque([chocolates])
    while queue:
        level_diff = 0
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            
            level_sum -= node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_sum)
    return result