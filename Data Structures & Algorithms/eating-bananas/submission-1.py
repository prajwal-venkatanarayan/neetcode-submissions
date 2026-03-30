class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res= r

        while l<=r:
            k = l+(r-l)//2
            #k = (l+r)//2
            hours = 0
            for p in piles:
                hours = hours + math.ceil(p/k)
            if hours <= h:
                res = min(res,k)
                #move the right pointer to left half
                r = k-1   
            else:
                 #move the left pointer to right half
                l = k+1

        return res                      