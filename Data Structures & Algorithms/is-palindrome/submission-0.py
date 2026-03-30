class Solution:
    def isPalindrome(self, s: str) -> bool:
        l1 = list(s.strip().lower())
        l1 = [x for x in l1 if x.isalnum()]
        l2= list(reversed(l1))
        print(l1)
        print(l2)
        for i,j in zip(l1,l2):
            if i!=j:
                return False
        return True        
        