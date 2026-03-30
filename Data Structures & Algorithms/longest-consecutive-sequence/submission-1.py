class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest = 0 

        for num in nums:
            # check if there's a number left of it, to know beginning 
            if (num-1) not in numSet:
                length = 1
                while (num+length) in numSet:
                    length = length +1
                longest = max(length,longest)    
        return longest