# Recursion Patterns
# Tail Recursion
#Divide and conquer: eg. is merge sort
#backtracking

#eg for tail recursion 

def factorial_tail(n, accumulator = 1):
    if n == 0:
        return accumulator
    else:
        return factorial_tail(n-1,accumulator * n)
    
#print(factorial_tail(5))

#problem1
 #first bad version  

