class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s ={}
        count_t = {}

        for char in s:
            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1
        
        for i in t:
            if i in count_t:
                count_t[i] += 1
            else:
                count_t[i] = 1
        return count_s == count_t
            
        