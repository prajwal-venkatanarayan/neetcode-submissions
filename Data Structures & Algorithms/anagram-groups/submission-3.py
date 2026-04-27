class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list)

        for i in strs:
            temp = ''.join(sorted(i))
            final[temp].append(i)

        return list(final.values())    