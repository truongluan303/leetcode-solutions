class Solution:
    
    def reverse(self, x: int) -> int:
        neg = False
        
        if x < 0:
            neg = True

        s = str(x).replace('-', '')
        
        s = s[::-1]
        num = int(s)
        
        if num > 2**31:
            return 0
        
        if neg:
            num *= -1

        return num