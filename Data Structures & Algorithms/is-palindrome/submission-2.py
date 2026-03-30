class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(x for x in s if x.isalnum())
        i = 0
        j = len(cleaned)-1
        while i <j:
            if cleaned[i].lower() == cleaned[j].lower():
                i = i+1
                j = j-1
            else:
                return False    
        return True    