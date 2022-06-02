class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ''
        prefix = ''
        
        for chars in zip(*strs):

            if len(set(chars)) == 1:
                prefix += chars[0]
                longest_prefix = prefix if len(longest_prefix) < len(prefix) else longest_prefix
            else:
                break
            
        return longest_prefix