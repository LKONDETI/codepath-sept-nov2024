# Remove duplicates in sorted array
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for j in range(0, len(nums)):
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1
        return i

#contains Duplicates
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = 1
        nums.sort()
        for i in range(1, len(nums)):
                count += 1
                if nums[i] == nums[i - 1]:
                    return True
        
        return False

#best time to buy and sell stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit
#move zeros to the end of the list
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] , nums[j] = nums[j] , nums[i]
                i += 1
        return nums
#Two sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)-1):
            for j in range(i +1, len(nums)):
                if nums[i] + nums [j] == target:
                    result = [i,j]
        return result

#remove element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_index = 0
        for read_index in range(len(nums)):
            if nums[read_index] != val:
                nums[write_index] = nums[read_index]
                write_index += 1
        return write_index
#first unique character
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
