class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) < 2:
            return len(s)
        
        occurence = dict()
        longest = 0
        sub_beg = 0
        
        for i in range(len(s)):
            
            if s[i] in occurence:
                if occurence[s[i]] >= sub_beg:
                    sub_beg = occurence[s[i]] + 1
                    
            temp = i - sub_beg + 1
            longest = max(longest, temp) 
                
            occurence[s[i]] = i
            
        print(occurence)
            
        return longest
                