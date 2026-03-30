class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def sumOfSquares(n):
            output = 0
            while n:
                digit = n%10
                digit = digit**2
                output = output + digit
                n = n//10
            return output

        while n not in visited:
            visited.add(n)
            n = sumOfSquares(n)
            if n == 1 :
                return True
        return False


            

        