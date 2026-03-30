"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        hash_map = defaultdict(int)

        for i in intervals:
            hash_map[i.start] = hash_map[i.start] + 1
            hash_map[i.end] =  hash_map[i.end] - 1

        prev,res = 0,0

        for i in sorted(hash_map.keys()):
            prev = prev + hash_map[i]
            res = max(res,prev)    

        return res    

        