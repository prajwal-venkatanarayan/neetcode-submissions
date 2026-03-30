class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        res = len(nums)

        for i in range(len(nums)):
            print("---",res,"+",i,"-,",nums[i])
            res = res + i - nums[i]
        return res    
        