class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1
        max_area = 0

        while l<r:
            area = (r-l)*min(heights[l],heights[r])
            print("------",r,l,min(heights[l],heights[r]),area)
            max_area = max(area,max_area)
            if heights[l]<heights[r]:
                l=l+1
            elif heights[l]>=heights[r]:
                r=r-1

        print("---",max_area)
        return max_area            