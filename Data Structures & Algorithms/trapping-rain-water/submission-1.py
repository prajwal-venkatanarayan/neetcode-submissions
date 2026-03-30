class Solution:
    def trap(self, height: List[int]) -> int:

        l=0
        r=len(height)-1

        max_l=height[l]
        max_r=height[r]
        total=0

        while l<r:
            if max_l < max_r:
                l= l+1
                max_l = max(max_l,height[l])
                total = total + max_l - height[l]
            elif max_l>=max_r:
                r = r-1
                max_r = max(max_r,height[r])
                total = total + max_r - height[r]

        return total            
