class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list)

        for i in strs:
            temp_str = "".join(sorted(i))
            final[temp_str].append(i)
        return list(final.values())   