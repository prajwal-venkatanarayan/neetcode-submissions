class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r= len(heights)-1
        max_cap =0

        while l<r:
            cap = (r-l)*min(heights[l],heights[r])
            max_cap=max(cap,max_cap)
            if heights[l]<heights[r]:
                l=l+1
            else:
                r=r-1

        return max_cap        
