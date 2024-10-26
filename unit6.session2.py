def twoSum(nums):
    hashMap = {}
    for i in range(len(nums)):
        diff = abs(target - nums[i])
        if diff in hashMap:
            return[i, hashMap[diff]]
        
        hashMap[nums[i]] = i
    return [-1,-1]

nums = [2,7,11,15]
target = 4
#print(twoSum(nums))

#koko likes to eat slowly but still wants to finish eating all the bananas before guards come
# return the minimum integer k such that she can eat all the bananas within h hours.

def minEatingSpeed(piles, h):
    l,r = 1, max(piles)
    res = r
    while l <= r:
        k = (l +r)//2
        time = 0
        for i in range(len(piles)):
            if piles[i] <= k:
                time += 1
            else:
                time += math.ciel(piles[i] / k)
        
        if time <= h :
            r = k -1
            res = min(res, k)
        else:
            l = k+1
        
        return res
                

#l         k          r
#1 2 3 4 5 6 7 8 9 10 11
#k =6
#piles = [3,6,7,11], h =8

#res =6
