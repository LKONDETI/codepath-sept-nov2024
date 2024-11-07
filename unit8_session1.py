# write a function that takes a string s and returns the string in reverse order
#space complexity : O(n)
#time complexity : O(n)

#     4
#    /  \
#   2    7
#  / \
# 1   3

def BinarySearchTree(root):
    def dfs(node, low, high):
        if not node:
            return True
        if(low is not None and node.val <= low) or (high is not None and node.val >= high):
            return False
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    return dfs(root, None, None)
#root = TreeNode(4)
#root.left = TreeNode(2)
#root.right = TreeNode(7)
#root.left.left = TreeNode(1)
#root.left.right = TreeNode(3)
    
#problem 1
from collections import deque
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

root = TreeNode('Trunk')
root.left = TreeNode('Mcintosh')
root.right = TreeNode('Granny Smith')
root.left.left = TreeNode('Fuji')
root.left.right = TreeNode('Opal')
root.right.left = TreeNode('Crab')
root.right.right = TreeNode('Gala')
#print_tree(root)

#problem 2
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
    if not root:
        return "Empty"
    if root.val == "+":
        result = root.left.val + root.right.val
        return result
    elif root.val == "*":
        result = root.left.val * root.right.val
        return result
    elif root.val == "-":
        result = root.left.val - root.right.val
        return result
    elif root.val == "/":
        result = root.left.val * root.right.val
        return result
apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

#print(calculate_yield(apple_tree))

#session2
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
  
def count_odd_splits(root):
    if not root:
        return "Empty"
    result = 0
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            if node.val % 2 == 1:
                result += 1
            queue.append(node.left)
            queue.append(node.right)
        return result

values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))

#session1
#problem 3
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
'''
def right_vine(root):
  if not root:
      return "Empty"
  current = root
  result = []
  while current:
        result.append(current.val)
        current = current.right
    return result'''
def right_vine(root):
    if not root:
      return "Empty"
    result = []
    root_transverse(root, result)
    return result

def root_transverse(root, result):
    if not root:
        return
    result.appen(root.val)
    root_transverse(root.result, result)
    

    

    




