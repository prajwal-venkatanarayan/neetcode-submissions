class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}

        for num in nums:
            count[num] = 1+count.get(num,0)

        heap=[]
        for num in count.keys():
            heapq.heappush(heap,(count[num],num))

        res=[]
        ans=heapq.nlargest(k,heap)
        for i in ans:
            res.append(i[1])
        return res