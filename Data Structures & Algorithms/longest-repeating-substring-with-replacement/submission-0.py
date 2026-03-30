class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l=0
        maxf=0

        for r in range(len(s)):
            '''
            Update the counter, check from the existing table, if it doesn't exist then return 0
            using dictionary.get(keyname, value), where value is the return value
            '''

            count[s[r]] = 1 + count.get(s[r],0)
            maxf = max(maxf,count[s[r]])

           # window size is r-l+1, because when l and r at same index the window size is 1
            while (r-l+1) - maxf > k:
                count[s[l]] = count[s[l]] -1
                l = l+1
            res = max(res,r-l+1)    

        return res    

        