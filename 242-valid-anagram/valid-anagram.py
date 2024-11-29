class Solution:
    def isAnagram(self, s, t):
        #Checking if the lengths are different
        if len(s) != len(t):
            return False
        
        #Counting character frequencies in both strings
        count_s, count_t = {}, {}
        
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        
        #Comparing the frequency dictionaries
        return count_s == count_t
