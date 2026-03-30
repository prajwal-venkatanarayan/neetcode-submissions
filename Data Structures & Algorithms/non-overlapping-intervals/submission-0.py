class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        prev_end = intervals[0][1]
        res=0

        for new_start, new_end in intervals[1:]:
            if new_start >= prev_end:
                prev_end=new_end
            else:
                res=res+1
                prev_end=min(prev_end,new_end)

        return res        

        