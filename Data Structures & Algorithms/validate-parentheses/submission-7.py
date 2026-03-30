class Solution:
    def isValid(self, s: str) -> bool:
       tags = []
       opening = set('([{')
       closing = set(')]}')
       pair = {')' : '(' , ']' : '[' , '}' : '{'}
       for i in s:
            if i in opening:
                tags.append(i)
            if i in closing:
                if len(tags)==0:
                    return False
                elif tags.pop()!= pair[i]:
                    return False  
                else:
                    continue
       
       if len(tags)==0:
            return True
       else:
            return False                

